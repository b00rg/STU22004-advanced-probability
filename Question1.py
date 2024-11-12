from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

number_of_steps = 0.0
sigma = 0.2 #volatility
delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001] # time increments 
num_simulations = 100
time = 1 

for delta in delta_ts:
    temperature = 0.0 # starting temperature at 0
    above_zero_count = 0.0 # track how many times temp is above 0
    num_steps = int(1 / delta) # change delta_ts index for different values 
    max_temperature = -float('inf')
    for _ in range(num_steps): 
        Z = np.random.standard_normal()  
        temperature_change = sigma*sqrt(delta)*Z  # this is based off a stochastic process. change delta_ts[x] for different time increments
        temperature += temperature_change 
        if temperature > 0.0:
            above_zero_count += 1.0
        if temperature > max_temperature:
            max_temperature = temperature
    p = above_zero_count/float(num_steps) 
    print(f"P for delta_ts = {delta} is: {p}") 
    print(f"Max temperature is {max_temperature}")

