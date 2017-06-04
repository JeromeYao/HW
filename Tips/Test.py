#!usr/bin/env python
# Filename:Test.py

"""
For test
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(10)
plt.plot(a, a*1.5, a, a*2.5, a, a*3.5, a, a*4.5)
plt.show()
