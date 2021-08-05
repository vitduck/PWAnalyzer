#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'srad',
    src      = ['srad.cpp'], 
    compiler = 'g++',
    header   = [],
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = 'OMP_NUM_THREADS=4 ./srad 2048 2048 0 127 0 127 2 0.5 2')

#rodinia.debug() 
rodinia.build() 
rodinia.run()
