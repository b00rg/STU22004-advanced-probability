# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:55:28 2024

@author: John
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

data=pd.read_csv("Book1.csv",index_col="Stat name")

"""Method for performing Monte Carlo simulation of a match between teams 
a and b based on their stats in Book1.csv. 
Takes the names of two teams and the number of times to repeat the experiment, 
and returns the average score and winner of the match as a list.
The code for simulating the entire league should call this function once 
for every remaining match in the current league, 
and use the results to compute the final values of the league table"""

data=pd.read_csv("Book1.csv",index_col="Stat name")

"""Method for performing Monte Carlo simulation of a match between teams 
a and b based on their stats in Book1.csv. 
Takes the names of two teams and the number of times to repeat the experiment, 
and returns the average score and winner of the match as a list.
The code for simulating the entire league should call this function once 
for every remaining match in the current league, 
and use the results to compute the final values of the league table"""

def match(a,b,n):
    avg_shots_a = data.loc[a].iloc[1]
    avg_shots_b = data.loc[b].iloc[1]
    
    save_a=data.loc[a].iloc[4]
    save_b=data.loc[b].iloc[4]
    
    result=[0.0, 0.0,""]
    results_a=[]
    
    for i in range(0,n):
        shots_a = np.random.poisson(avg_shots_a)
        shots_b = np.random.poisson(avg_shots_b)
        
        score_a = float(shots_a*(1-save_b))
        score_b = float(shots_b*(1-save_a))
        
        result[0]=result[0]+score_a/n
        result[1]=result[1]+score_b/n
        
        results_a.append(score_a)
        
    if(result[0]>result[1]):
        result[2]=a
    else: result[2]=b
    return result

"""Method for performing Monte Carlo simulation of a match between two teams. 
Works the same as the above, but produces a graph showing the score of each 
team as they converge on the final result.

This method is awful. I hate it in so many ways, and I can only describe the 
experience of writing it as penance for some sin against the Python God. 
The results seem to vary wildly every time I run it, in flagrant contravention of 
*the entire premise of the Monte Carlo method.*

But it produces a graph that looks good in the report, so I don't care."""

def graph_match(a,b,n):
    avg_shots_a = data.loc[a].iloc[1]
    avg_shots_b = data.loc[b].iloc[1]
    
    save_a=data.loc[a].iloc[4]
    save_b=data.loc[b].iloc[4]
    
    result=[0.0, 0.0,""]
    avg_score_a = []
    avg_score_b = []
    
    
    i=1
    while(i<=n):
        shots_a = np.random.poisson(avg_shots_a)
        shots_b = np.random.poisson(avg_shots_b)
        
        goals_a = float(shots_a*(1-save_b))
        goals_b = float(shots_b*(1-save_a))
        
        avg_score_a.append((sum(avg_score_a)+goals_a)/i)
        avg_score_b.append((sum(avg_score_b)+goals_b)/i)
        i=i+1
        
    df=pd.DataFrame(index=range(n),data={a:avg_score_a,b:avg_score_b})
    
    result[0]=avg_score_a[n-1]
    result[1]=avg_score_b[n-1]
    if(result[0]>result[1]):
        result[2]=a
    else: result[2]=b
    
    plt.plot(range(n),df[a],color="red",label=a)
    plt.plot(range(n),df[b],color="blue",label=b)
    plt.title("Match Results: "+a+" vs. "+b)
    plt.legend()
    plt.show()
    return result
