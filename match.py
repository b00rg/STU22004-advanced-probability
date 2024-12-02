# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:55:28 2024

@author: John
"""

import numpy as np
import pandas as pd

data=pd.read_csv("Book1.csv",index_col="Stat name")

"""Method for performing Monte Carlo simulation of a match between teams 
a and b based on their stats in Book1.csv. 
Takes the names of two teams and the number of times to repeat the experiment, 
and returns the average score and winner of the match as a list.
The code for simulating the entire league should call this function once 
for every remaining match in the current league, 
and use the results to compute the final values of the league table"""

def match(a,b,reps):
    avg_shots_a = data.loc[a].iloc[1]
    avg_shots_b = data.loc[b].iloc[1]
    
    save_a=data.loc[a].iloc[4]
    save_b=data.loc[b].iloc[4]
    
    result=[0.0, 0.0,""]
    
    for i in range(0,reps):
        shots_a = np.random.poisson(avg_shots_a)
        shots_b = np.random.poisson(avg_shots_b)
        
        score_a = float(shots_a*(1-save_b))
        score_b = float(shots_b*(1-save_a))
        
        result[0]=result[0]+score_a/reps
        result[1]=result[1]+score_b/reps
        
    if(result[0]>result[1]):
        result[2]=a
    else: result[2]=b
    
    result[0] = round(result[0])
    result[1] = round(result[1])
        
    return result
