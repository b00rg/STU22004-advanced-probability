from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
sigma = 1  # volatility
time = 1  # total simulation time
delta_ts = [0.01, 0.009, 0.008, 0.007, 0.006, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001]  # step sizes

# Initialize tracking variables
results = []  # To store probability and max temperature for each delta_t
probabilities = []
max_temperatures = []
# Start the simulation
for delta_t in delta_ts:
    num_steps = int(time / delta_t)  # Total steps for this delta_t
    temperature = 0.0   # Continue from last state
    max_temperature = -float('inf')
    above_zero_count = 0.0

    for step in range(num_steps):
        Z = np.random.standard_normal()  # Random variable for simulation
        temperature_change = sigma * sqrt(delta_t) * Z
        temperature += temperature_change

        if temperature > 0.0:
            above_zero_count += 1.0
        if temperature > max_temperature:
            max_temperature = temperature

    # Store results for this delta_t
    probability = above_zero_count / num_steps
    probabilities.append(probability)
    max_temperatures.append(max_temperature)
    results.append({
        "delta_t": delta_t,
        "probability": probability,
        "max_temp": max_temperature,
    })

# Display results
for result in results:
    print(
        f"Delta_t: {result['delta_t']:.4f}, Probability: {result['probability']:.4f}, "
        f"Max Temperature: {result['max_temp']:.4f}"
    )


# Plot 1: Probability vs Time Step (Delta_t)
plt.subplot(1, 3, 1)
plt.plot(delta_ts, probabilities, marker='o', linestyle='-', color='b')
plt.xlabel('Delta_t (Time Step)')
plt.ylabel('Probability (P)')
plt.title('Probability vs Time Step (Delta_t)')

# Plot 2: Max Temperature vs Time Step (Delta_t)
plt.subplot(1, 3, 2)
plt.plot(delta_ts, max_temperatures, marker='o', linestyle='-', color='r')
plt.xlabel('Delta_t (Time Step)')
plt.ylabel('Max Temperature')
plt.title('Max Temperature vs Time Step (Delta_t)')

# Plot 3: Max Temperature vs Probability (P)
plt.subplot(1, 3, 3)
plt.plot(probabilities, max_temperatures, marker='o', linestyle='-', color='g')
plt.xlabel('Probability (P)')
plt.ylabel('Max Temperature')
plt.title('Max Temperature vs Probability')

# Show the plots
plt.tight_layout()
plt.show()
