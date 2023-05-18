# Modules to be imported

import   requests
import   pydot, os
import   subprocess, sys
import   pickle, graphviz
import   json, re, nltk
import   pandas as pd
import   numpy as np
from     pyopenie import OpenIE5
from     unidecode import unidecode
from     nltk.tokenize import sent_tokenize


pd.options.mode.chained_assignment = None 


print("All imported")