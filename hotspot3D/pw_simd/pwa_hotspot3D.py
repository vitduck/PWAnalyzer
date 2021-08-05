#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'hotspot3D', 
    src      = ['3D.c'],
    compiler = 'gcc', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp', '-lm'], 
    run_cmd  = './hotspot3D 512 8 100 ../input/temp_512x8 ../input/power_512x8 hot.dat')

rodinia.build() 
rodinia.run()
