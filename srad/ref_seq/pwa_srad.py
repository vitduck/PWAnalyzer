#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'srad',
    src      = ['srad.cpp'], 
    compiler = 'g++',
    header   = [],
    cflags   = [], 
    ldflags  = [''], 
    run_cmd  = './srad 2048 2048 0 127 0 127 2 0.5 2')

#rodinia.debug() 
rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport() 
rodinia.pwloops() 
