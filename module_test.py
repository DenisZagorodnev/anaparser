#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:50:38 2019

@author: deniszagorodnev
"""

from anaparser import anaplan_parser

fname = 'M61.51.1 Финансовые показатели.xls'
dict_name = 'М60.01_CONS.csv'
path = '/Users/deniszagorodnev/Desktop/'

anaplan_parser.file_parser(path + dict_name, Input_path = path, Output_path = path).parse_file(fname)