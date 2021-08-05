#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'lud', 
    src      = ['lud.c', 'lud_base.c', '../include/common.c'],  
    compiler = 'gcc',
    header   = [],
    cflags   = ['-I../include'], 
    ldflags  = ['-lm'], 
    run_cmd  = './lud -i ../input/1000.dat')

rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport('lud_base.c:lud_base') 
rodinia.pwloops('lud_base.c:lud_base') 
