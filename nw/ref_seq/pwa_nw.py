#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'nw', 
    src      = ['needle.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = './nw 8192 10 1')

rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport('needle.cpp:nw_optimized')
rodinia.pwloops('needle.cpp')
