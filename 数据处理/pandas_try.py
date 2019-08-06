#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

import numpy as np
from pandas import DataFrame
import pandas as pd

df = DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus')
               )