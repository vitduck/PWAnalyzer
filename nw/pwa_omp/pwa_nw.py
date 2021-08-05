#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'nw', 
    src      = ['needle.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = 'OMP_NUM_THREADS=4 ./nw 8192 10 1')

rodinia.build() 
rodinia.run()
rodinia.profile() 
rodinia.pwreport('needle.cpp:nw_optimized')
