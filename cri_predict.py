# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 20:08:35 2023

@author: NAVEEN
"""

import numpy as np
import pandas as pd
import pickle
cricket_model=pickle.load(open('C:/models/cricket_model.sav','rb'))
input_data=([[174,54,88,8.0,6,24,3,2,3,4,56]])
input_data_as_numpy_array=np.array(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
value=cricket_model.predict(input_data_reshaped)
print(value)