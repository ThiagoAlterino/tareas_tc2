#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:59:39 2026

@author: thiago
"""
#Librerias Externas
from scipy import signal

#Libreria TC2
from pytc2.sistemas_lineales import pretty_print_lti

#  Bessel-Thompson de orden 2, 3 y 4

# Bessel-Thompson de orden 2
z2,p2 = signal.bessel(2, Wn=1, btype='low', analog=True, norm='delay')
pretty_print_lti(z2,p2)

# Bessel-Thompson de orden 3
z3,p3 = signal.bessel(3, Wn=1, btype='low', analog=True, norm='delay')
pretty_print_lti(z3,p3)

# Bessel-Thompson de orden 4
z4,p4 = signal.bessel(4, Wn=1, btype='low', analog=True, norm='delay')
pretty_print_lti(z4,p4)

