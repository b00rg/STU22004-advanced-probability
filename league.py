import numpy as np
import pandas as pd
import match

data=pd.read_csv("Book1.csv",index_col="Stat name")

NUMBER_OF_TEAMS = 20
NUMBER_OF_MATCHES_SIMULATED = 100

# John's match function (couldn't figure out how to import it)

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

teamScores = [0] * NUMBER_OF_TEAMS
teams = data.index.tolist()
print("Results of Each Match:")
for i in range(0,NUMBER_OF_TEAMS-1):
    for j in range(i+1,NUMBER_OF_TEAMS-1):
        homeAndAway=False
        while homeAndAway==False:
            matchResult=match(teams[i],teams[j],NUMBER_OF_MATCHES_SIMULATED)
            print(matchResult)
            if(matchResult[0] > matchResult[1]):
                teamScores[i]+=3
            elif (matchResult[0] < matchResult[1]):
                teamScores[j]+=3
            else:
                teamScores[i]+=1
                teamScores[j]+=1
            homeAndAway=True
    
print("\nResults of Each Team:")
predictedChampionAndScore=["",0]
for i in range(0,NUMBER_OF_TEAMS-1):
    print(teams[i]+": ",teamScores[i])
    if(predictedChampionAndScore[1]<teamScores[i]):
        predictedChampionAndScore=[teams[i],teamScores[i]]

print("\nPremiere League Predicted Champion: "+predictedChampionAndScore[0])
print(teamScores)

