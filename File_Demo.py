# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 01:16:23 2018

"""

import os
path = "C:\\Users\\RPS\\Desktop\\Ashok\\Ashok"
for (dirpath,dirname,filename) in os.walk(path):
    print (filename)