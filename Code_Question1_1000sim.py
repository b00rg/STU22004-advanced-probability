from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Parameters
sigma = 1  # volatility
time = 1  # total simulation time
delta_ts = [0.001, 0.0001, 0.00001, 0.000001]  # step sizes to experiment with
num_simulations = 1000  # number of Monte Carlo simulations

# Initialize results
results = {delta_t: {"P": [], "T_max": []} for delta_t in delta_ts}

# Monte Carlo Simulations
for delta_t in delta_ts:
    num_steps = int(time / delta_t)
    time_points = np.linspace(0, time, num_steps)
    
    for _ in range(num_simulations):
        temperature = 0.0
        max_temperature = -float('inf')
        max_temp_time = 0.0
        above_zero_count = 0.0

        # Simulate temperature over time
        for step, t in enumerate(time_points):
            Z = np.random.standard_normal()
            temperature += sigma * sqrt(delta_t) * Z
            if temperature > max_temperature:
                max_temperature = temperature
                max_temp_time = t
            if temperature > 0.0:
                above_zero_count += 1.0
        
        # Store results
        P = above_zero_count / num_steps
        results[delta_t]["P"].append(P)
        results[delta_t]["T_max"].append(max_temp_time)

# Create a figure for all plots
fig, axes = plt.subplots(len(delta_ts), 2, figsize=(2, 2 * len(delta_ts)))  # Smaller figure size

# Plot results for each delta_t
for i, delta_t in enumerate(delta_ts):
    P_values = results[delta_t]["P"]
    T_max_values = results[delta_t]["T_max"]

    # Plot histogram for P
    axes[i, 0].hist(P_values, bins=30, alpha=0.7, color='b', edgecolor='k')
    axes[i, 0].set_title(f'Distribution of P (Delta_t = {delta_t})', fontsize=10)
    axes[i, 0].set_xlabel('P (Proportion of Time Temp > 0)', fontsize=9)
    axes[i, 0].set_ylabel('Frequency', fontsize=9)

    # Plot histogram for T_max
    axes[i, 1].hist(T_max_values, bins=30, alpha=0.7, color='r', edgecolor='k')
    axes[i, 1].set_title(f'Distribution of T_max (Delta_t = {delta_t})', fontsize=10)
    axes[i, 1].set_xlabel('T_max (Time of Max Temp)', fontsize=9)
    axes[i, 1].set_ylabel('Frequency', fontsize=9)

    # Adjust font sizes for smaller plots
    axes[i, 0].tick_params(axis='both', labelsize=8)
    axes[i, 1].tick_params(axis='both', labelsize=8)

# Adjust layout for better visibility
plt.tight_layout(pad=1.0)
plt.show()
