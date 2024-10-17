from matplotlib import pyplot as plt
import numpy as np
from Electoral2020 import states_electoral_map_2020
from ElectoralPrediction import states_electoral_map_2030

# Producing a bar graph visual of states whose electoral votes are 
# forecasted to change from 2020 to 2030

# Initializing a dictionary to store electoral vote differences for 
# each state from their recorded value in 2020 to the forecasted value in 2030
states_electoral_map_changes = dict()

states_chart = np.array([])
change_magnitude_chart = np.array([])
colors_chart = np.array([])

# Updating the dictionary with the apropriate electoral vote difference for each state
for key in states_electoral_map_2030:
    electoral_change = states_electoral_map_2030[key] - states_electoral_map_2020[key]
    states_electoral_map_changes[key] = electoral_change

    # Ensuring that all states with a non-zero electoral vote change will get ploted, and that the
    # states with a positive change will be shown in green while those those with a negative change
    # will be shown in red
    if electoral_change != 0:
        states_chart = np.append(states_chart, key)
        change_magnitude_chart = np.append(change_magnitude_chart, states_electoral_map_changes[key])

        if electoral_change > 0:
            colors_chart = np.append(colors_chart, 'green')
        else:
            colors_chart = np.append(colors_chart, 'red')

# Plotting two bar graphs consisting of states that have a 
# non-zero electoral vote change from 2020 to 2030
plt.title("Electoral Vote Changes")
plt.ylabel("Electoral Vote Change Magnitude")

halfway_length = len(states_chart) // 2
states_chart_first_half = states_chart[0:halfway_length]
states_chart_second_half = states_chart[(halfway_length + 1):len(states_chart)]
change_magnitude_chart_first_half = change_magnitude_chart[0:halfway_length]
change_magnitude_chart_second_half = change_magnitude_chart[(halfway_length + 1):len(states_chart)]
colors_chart_first_half = colors_chart[0:halfway_length]
colors_chart_second_half = colors_chart[(halfway_length + 1):len(states_chart)]

# Plotting the first half of changing states
plt.axhline(0, color='black', linestyle='-')
plt.bar(states_chart_first_half, change_magnitude_chart_first_half, color = colors_chart_first_half)
plt.show()

# Plotting the second half of changing states
plt.axhline(0, color='black', linestyle='-')
plt.bar(states_chart_second_half, change_magnitude_chart_second_half , color = colors_chart_second_half)
plt.show()



