import numpy as np
import os

alphas=np.linspace(0.1,1.0,5)
l1_ratios=np.linspace(0.1,1.0,5)

for alpha in alphas:
    for l1 in l1_ratios:
        os.system(f'python model.py -a {alpha} -l1 {l1}')