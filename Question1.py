from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

mu = 0.00 # drift -> in this case 0 as the temperature is constant
initial_temperature = 0.0
number_of_steps = 0.0
num_simulations = 1000
sigma = 0.2 #volatility
delta_ts = [0.01, 0.001, 0.0001, 0.00001, 0.000001] # time increments 

for t in range(1, num_simulations):
    Z = np.random.standard_normal(num_simulations) # standard normal random variable 
    temperature_change = mu*delta_ts[0] + sigma*sqrt(delta_ts[0])*Z  # this is based off a stochastic process

print(temperature_change)
