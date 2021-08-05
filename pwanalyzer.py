#!/usr/bin/env python3 

import re 
import os 
import sys
import time
import pprint
import logging 
import subprocess

class PwAnalyzer(): 
    # initialize root logger 
    logging.basicConfig( 
        stream  = sys.stderr, 
        level   = logging.INFO, 
        format  = '%(asctime)s %(message)s', 
        datefmt = '%Y%m%d_%H:%M:%S')

    def __init__(self, name, src, header, compiler, cflags=[], ldflags=[], run_cmd=''): 
        self.src       = src
        self.header    = header
        self.compiler  = compiler
        self.level     = '-O2'
        self.cflags    = cflags
        self.ldflags   = ldflags
        self.run_cmd   = run_cmd
        self.bin       = name
        self.output    = 'output.dat'
        self.error     = [] 
        self.pwr       = []
        self.opp       = []

    def build(self): 
        self.syscmd(
            f'{self.compiler} '
            f'{self.level} '
            f'{" ".join(self.cflags)} ' 
            f'{" ".join(self.ldflags)} '
            f'{" ".join(self.src)} ' 
            f'-o {self.bin}' )

    def run(self): 
        self.syscmd(self.run_cmd, self.output)

    def gprof(self, line=0): 
        if line: 
            self.syscmd(f'gprof -b -p -l ./{self.bin}', 'gprof_line.dat')
            self.parse_gprof('gprof_line.dat')
        else: 
            self.syscmd(f'gprof -b -p ./{self.bin}', 'gprof_func.dat')
            self.parse_gprof('gprof_func.dat')

    def profile(self): 
        self.run_cmd  = self.run_cmd.replace(self.bin, f'{self.bin}_pg')
        self.level    = '-O0'
        self.ldflags += ['-pg', '-g']
        self.bin     += '_pg'
        self.output   = 'output_pg.dat'
        
        self.build() 
        self.run() 
        self.gprof() 
        self.gprof(line=1)
        
    def pwreport(self, hotspot='', level=2): 
        if hotspot: 
            self.syscmd(f'pwreport --level {level} {hotspot} -- {" ".join(self.cflags)}', 'report.dat')
        else: 
            self.syscmd(f'pwreport --level {level} --summary --detail .', 'report.dat')
        
        # metric summary
        with open('report.dat', 'r') as fh: 
            for line in fh: 
                if re.search('\[ ERROR \]', line): 
                    self.error.append(line.strip())

                if re.search('\[PWR\d+\]', line):  
                    self.pwr.append(line.strip())
                
        if self.error:
            logging.info('Error:')
            [print(f'{i.strip()}') for i in sorted(list(set(self.error)))]
            print() 

        if self.pwr: 
            logging.info('Remarks:')
            [print(f'{i.strip()}') for i in sorted(list(set(self.pwr)))]
            print() 

    def pwloops(self, hotspot='', level=2): 
        if hotspot: 
            self.syscmd(f'pwloops --verbose --brief {level} {hotspot} -- {" ".join(self.cflags)}', 'loop.dat')
        else: 
            self.syscmd(f'pwloops --verbose --brief . -- {" ".join(self.cflags)}', 'loop.dat')
        
        with open('loop.dat', 'r') as fh: 
            for line in fh: 
                print(line.rstrip())
            
            print()

    def parse_gprof(self, gprof_output): 
        with open(gprof_output, 'r') as fh: 
            # skip lines
            [fh.readline() for i in range(0,3)] 
            
            # print table header
            print(f'{fh.readline().rstrip()}')
            print(f'{fh.readline().rstrip()}')

            for gline in fh.readlines()[:5]:
                print(f'{gline.rstrip()}')
            
            print() 
            
    def syscmd(self, cmd, output=None):
        logging.info(f'{cmd}')

        try:
            pout = subprocess.check_output(cmd, stderr=subprocess.PIPE, shell=True).decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            logging.error(f'{e.stderr.decode("utf-8").strip()}')
            sys.exit()
        else:
            if output:
                with open(output, "w") as output_fh:
                    output_fh.write(pout)
            else:
                return pout
    def wait(self, period): 
        time.sleep(period)
    
    def debug(self):  
        pprint.pprint(vars(self))
