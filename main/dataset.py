# This file relates to dealing with netCDF data and utilising it appropriately

import importlib

try:
    import netCDF4
except ImportError:
    print("netCDF4 module not found. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "netCDF4"])
    importlib.invalidate_caches()
    import netCDF4

import numpy as np

f = netCDF4.Dataset('../dataset/pottmp.mon.ltm.1981-2010.nc')  ## local path to a dataset, in gitignore currently

#print(f)

print(f.variables.keys()) 

shum= f.variables['valid_yr_count']
print(shum)



## The above code was an attempt to have a sneek peek at the dataset, the authors of the paper that we are trynna implement never mentioned any sought of link to the dataset 
# So it's really difficult to make a move and look out for an exact dataset. Alteast, it's something I couldn't find after an hour of scrolling through NCEP's website. There wasn't any data that resonanted so well with the one from the paper
## I'll be just implementing the model and will try to train it on one among the above data and then use some random sat images to see how well it works on image dataset
