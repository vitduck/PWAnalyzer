#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'bfs', 
    src      = ['bfs.cpp'],
    compiler = 'g++', 
    header   = [], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = './bfs 1 ../input/graph1MW_6.txt')

rodinia.build() 
rodinia.run()
