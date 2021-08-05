#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'pf', 
    src      = ['pathfinder.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = [], 
    run_cmd  = 'time -p ./pf 1000000 500')

rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport('pathfinder.cpp:init')
rodinia.pwloops('pathfinder.cpp')
