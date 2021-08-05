#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'pf', 
    src      = ['pathfinder.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = '/usr/bin/time -p ./pf 1000000 500')

rodinia.build() 
rodinia.run()
