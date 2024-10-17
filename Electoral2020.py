# Electoral Votes Distribution in 2020
# Source: https://www.archives.gov/electoral-college/allocation

states_electoral_map_2020 = {
    'District of Columbia': 3,
    'Alabama': 9,
    'Kentucky': 8,
    'North Dakota': 3,
    'Alaska': 3,
    'Louisiana': 8,
    'Ohio': 17,
    'Arizona': 11,
    'Maine': 4,
    'Oklahoma': 7,
    'Arkansas': 6,
    'Maryland': 10,
    'Oregon': 8,
    'California': 54,
    'Massachusetts': 11,
    'Pennsylvania': 19,
    'Colorado': 10,
    'Michigan': 15,
    'Rhode Island': 4,
    'Connecticut': 7,
    'Minnesota': 10,
    'South Carolina': 9,
    'Delaware': 3,
    'Mississippi': 6,
    'South Dakota': 3,
    'Missouri': 10,
    'Tennessee': 11,
    'Florida': 30,
    'Montana': 4,
    'Texas': 40,
    'Georgia': 16,
    'Nebraska': 5,
    'Utah': 6,
    'Hawaii': 4,
    'Nevada': 6,
    'Vermont': 3,
    'Idaho': 4,
    'New Hampshire': 4,
    'Virginia': 13,
    'Illinois': 19,
    'New Jersey': 14,
    'Washington': 12,
    'Indiana': 11,
    'New Mexico': 5,
    'West Virginia': 4,
    'Iowa': 6,
    'New York': 28,
    'Wisconsin': 10,
    'Kansas': 6,
    'North Carolina': 16,
    'Wyoming': 3
}

electoralVoteSum = 0

for key in states_electoral_map_2020:
    electoralVoteSum += states_electoral_map_2020[key]

print("2020 Electoral Vote Sum (Expected 538): " + str(electoralVoteSum))