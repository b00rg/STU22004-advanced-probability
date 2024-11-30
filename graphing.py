# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:01:26 2024

@author: John
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
league_stats = data=pd.read_csv("Book1.csv",index_col="Stat name")
data = pd.read_csv("Book12ElectricBoogaloo.csv",index_col="Team")

# Aston Villa
def graph_team(team):
    team_shots = data.loc[team]
    plt.hist(team_shots,bins=int(np.nanmax(team_shots)), edgecolor="black")
    
    pdist=np.random.poisson(lam=league_stats.loc[team].iloc[1],size=10000)
    x,y=np.unique(pdist,return_counts=True)
    y=y*11/10000
    plt.scatter(x,y,color="red")
    
    plt.xlabel("No. shots on target")
    plt.ylabel("Frequency")
    plt.title(team)
    plt.show()
    
    
teams=["Arsenal","Aston Villa","Bournemouth","Brentford","Brighton","Chelsea",
"Crystal Palace",
"Everton",
"Fulham",
"Ipswich Town",
"Leicester City",
"Liverpool",
"Manchester City",
"Manchester United",
"Newcastle United",
"Nottingham Forest",
"Southampton",
"Spurs",
"West Ham United",
"Wolverhampton Wanderers"]
def graph_all():
    for team in teams:
        graph_team(team)