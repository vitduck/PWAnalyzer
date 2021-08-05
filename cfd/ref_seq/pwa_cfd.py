#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'cfd', 
    src      = ['euler3d_cpu.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-Dblock_length=1', '-fopenmp'], 
    run_cmd  = './cfd ../input/fvcorr.domn.193K')

#  rodinia.build() 
#  rodinia.run()
#  rodinia.profile() 
rodinia.pwreport()
rodinia.pwloops()
