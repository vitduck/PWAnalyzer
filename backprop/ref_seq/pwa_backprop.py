#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'backprop', 
    src      = ['backprop.c', 'backprop_kernel.c', 'facetrain.c*', 'imagenet.c*'],
    compiler = 'gcc',
    header   = ['backprop.h'],
    cflags   = [], 
    ldflags  = ['-lm'], 
    run_cmd  = './backprop 65536')

rodinia.build() 
rodinia.run()
rodinia.wait(3.0)
rodinia.profile() 
rodinia.pwreport() 
rodinia.pwloops() 
