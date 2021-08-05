#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'kmeans', 
    src      = ['cluster.c', 'getopt.c', 'kmeans.c', 'kmeans_clustering.c'], 
    compiler = 'gcc',
    header   = ['getopt.h', 'kmeans.h', 'unistd.h'], 
    cflags   = [], 
    ldflags  = ['-fopenmp'], 
    run_cmd  = './kmeans -i ../input/819200.txt')

rodinia.build() 
rodinia.run()
rodinia.profile()
rodinia.pwreport('kmeans_clustering.c:kmeans_clustering')
rodinia.pwloops('kmeans_clustering.c')
