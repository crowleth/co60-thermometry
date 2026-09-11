import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import odr

# If this line fails, your ROOTSYS/PYTHONPATH variables (from the previous step) are not set correctly.
import ROOT 

print(f"Python Version: {sys.version}")
print(f"Numpy Version: {np.__version__}")
print(f"ROOT Version: {ROOT.gROOT.GetVersion()}")
print("SUCCESS: All modules imported correctly!")