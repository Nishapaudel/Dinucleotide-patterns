import sys
import os
import holoviews as hv
from holoviews import dim

from  bokeh.sampledata.autompg import autompg
hv.extension('bokeh')
import numpy as np
import pandas as pd

import sys
import os
import py2bit
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter1d
from scipy import stats
import statistics as stat
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from collections import Counter
from scipy.signal import find_peaks


violin_data = sys.argv[1]

df = pd.read_csv(violin_data, sep = '\t')

violin = hv.Violin(df, ('Dinucleotide', 'Dinucleotides'), ('ratio', 'Ratio')).redim.range(ratio=(0, 2))
violin.opts(height=500, width=900, violin_fill_color=dim('Dinucleotides').str(), cmap='Set1', title= 'Mitochondria_exon_UCSC')

hv.save(violin, 'Mitochondria_exon_UCSC', fmt = 'png' )
#hv.opts(violin, 'Promo_violin_plot.png', fmt = 'png' )

