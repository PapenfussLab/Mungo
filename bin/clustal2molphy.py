#!/usr/bin/env python

"""
clustal2molphy.py

Author: Tony Papenfuss
Date: Mon Mar 19 16:56:44 EST 2007

"""

import os, sys
from mungo.align import Alignment


alignment = Alignment.loadClustal(sys.argv[1])
alignment.saveMolphy(sys.argv[2])