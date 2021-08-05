#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'streamcluster', 
    src      = ['streamcluster_omp.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = './streamcluster 10 20 256 65536 65536 1000 none output.txt 4')

rodinia.build() 
rodinia.run()
