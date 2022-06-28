import sys
import os
import holoviews as hv
from holoviews import dim
from  bokeh.sampledata.autompg import autompg
hv.extension('bokeh')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statistics as stat
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


 
violin_data = sys.argv[1] #The input for this file is output file form supplementary file 5 code.


df = pd.read_csv(violin_data, sep = '\t')

violin = hv.Violin(df, ('Dinucleotide', 'Dinucleotides'), ('ratio', 'Ratio')).redim.range(ratio=(0, 2))
violin.opts(height=500, width=900, violin_fill_color=dim('Dinucleotides').str(), cmap='Set1', title= 'violin_plot')

hv.save(violin, 'violin_plot.png', fmt = 'png' )
hv.opts(violin, 'violin_plot.png', fmt = 'png' )

