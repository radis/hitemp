# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:31:28 2021

@author: erwan
"""

from radis.io.hitemp import fetch_hitemp as fetch

# For the moment use the fetch_hitemp from RADIS. In the long term, include
# the RADIS code here so that it can be used without RADIS import

if __name__ == '__main__':
    import hitemp
    df = hitemp.fetch('OH')