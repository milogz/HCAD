# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 11:11:40 2021

@author: joesc
"""

### Generador Base de datos BID-Cornell. 
import pandas as pd
df = pd.read_stata("pooled_data_public.dta") 
df.index = df.iloc[:,0]
df2 = df.iloc[:,range(113,122)]
df3 = pd.concat([df.iloc[:,1:1],df.iloc[:,range(112,122)]], axis=1)
df3 = df3[~df3.eq(-99).any(1)]
df3 = df3[~df3.eq('NR').any(1)]
df3.to_csv("BID-Cornell.csv")