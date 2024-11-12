from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

temperature = 0.0
number_of_steps = 0.0
sigma = 0.2 #volatility
delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001] # time increments 
num_simulations = 100
above_zero_temp = 0 

for t in range(1, num_simulations):
    Z = np.random.standard_normal() # standard normal random variable 
    temperature_change = sigma*sqrt(delta_ts[0])*Z  # this is based off a stochastic process. change delta_ts[x] for different time increments
    temperature += temperature_change # over time, temp changes with respect to temperature_change
    if temperature > 0.0:
        above_zero_temp += 1
    print(temperature)

print ("P is: " + str(above_zero_temp/num_simulations))
