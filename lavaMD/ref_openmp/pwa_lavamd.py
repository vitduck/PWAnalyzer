#!/usr/bin/env python3 

from pwanalyzer import PwAnalyzer

rodinia = PwAnalyzer( 
    name     = 'lavaMD', 
    src      = [
        './main.c', 
        './kernel/kernel_cpu.c', 
        './util/num/num.c', 
        './util/timer/timer.c'], 
    header   = [
        './main.h', 
        './kernel/kernel_cpu.h', 
        './util/num/num.h', 
        './util/timer/timer.h'], 
    compiler = 'gcc', 
    cflags   = [], 
    ldflags  = ['-fopenmp -lm'], 
    run_cmd  = './lavaMD -cores 4 -boxes1d 10')

rodinia.build() 
rodinia.run()
#  rodinia.profile() 
#  rodinia.pwreport('./kernel/kernel_cpu.c:kernel_cpu')
