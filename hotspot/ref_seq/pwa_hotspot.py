#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'hotspot', 
    src      = ['hotspot.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = './hotspot 1024 1024 2 4 ../input/temp_1024 ../input/power_1024 output.dat')

rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport()
rodinia.pwloops() 
