from PopulationPrediction import States_Population_Prediction_2030_df, states
import math
import heapq

# Predicting electoral votes for each state in 2030 using the Method of Equal Proportions
total_electoral_votes = 538
seats_left = total_electoral_votes  

# Initializing a dictionary to store the # of electoral votes for each state
states_electoral_map_2030 = {
    # District of Columbia always receives 3 electoral votes
    'District of Columbia': 3,
}

seats_left -= 3

for i in range(len(states)):
    # Each state is granted 2 electoral votes as there are 2 senators per state
    states_electoral_map_2030[states[i]] = 2

# The number of seats left now equals 435
seats_left -= (50 * 2)  

pop_prediction_array = States_Population_Prediction_2030_df.to_numpy()

# Initializing a maximum oriented priority queue for efficient calculations 
# involving the distribution of electoral votes to states
seat_priority = []
seat = 2

# Each state is automatically granted one seat from the House of Representatives, 
# resulting in 1 additional electoral vote
for i in range(len(pop_prediction_array[0])):
    state_population = pop_prediction_array[0][i]
    priority = state_population / math.sqrt(seat * (seat - 1))
    stateIndex = i
    heapq.heappush(seat_priority, (-1 * (priority), stateIndex, seat))
    states_electoral_map_2030[states[stateIndex]] += 1

# The number of seats left now equals 385
seats_left -= 50  

# Distributing seats to states until there are no more seats left
while seats_left > 0:
    # Finding the state with the greatest seat priority and removing it from 
    # the queue, and updating the electoral map votes count accordingly
    min_state = heapq.heappop(seat_priority)
    stateIndex = min_state[1]
    states_electoral_map_2030[states[stateIndex]] += 1

    # Inserting the removed state back into the queue with its updated seat priority
    state_population = pop_prediction_array[0][stateIndex]
    newSeat = min_state[2] + 1
    newPriority = state_population / math.sqrt(newSeat * (newSeat - 1))
    heapq.heappush(seat_priority, (-1 * (newPriority), stateIndex, newSeat))

    seats_left -= 1

print("Projected Electoral Map Votes in 2030:")
print(states_electoral_map_2030)

electoralVoteSum = 0

for key in states_electoral_map_2030:
    electoralVoteSum += states_electoral_map_2030[key]

print("2030 Electoral Vote Sum (Expected 538): " + str(electoralVoteSum))