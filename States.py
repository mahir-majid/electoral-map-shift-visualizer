import pandas as pd

# Creating a single Dataframe to store the population of U.S. states from 1970 to 2020

# Reading in Kaggle Datasets that store the population of U.S. states from 1900 to 2017 
# and the population for the year 2020 separately
USA_STATES_DATA_1900_2017 = pd.read_csv('./Data/States_Data_1900_2017.csv')
USA_STATES_DATA_2020 = pd.read_csv('./Data/States_Data_2020.csv')

# Gathering data on individual U.S. state populations from 1970 to 2015
row_indices = list(range(70, 116, 5))
USA_STATES_POP_1970_2015_df = USA_STATES_DATA_1900_2017.iloc[row_indices].reset_index(drop=True)
USA_STATES_POP_1970_2015_df.drop(columns=['D.C.'], inplace=True)

# Gathering data on individual U.S. state populations for 2020
df_50_states_length = len(USA_STATES_DATA_2020) - 1
USA_STATES_POP_2020_df = USA_STATES_DATA_2020.iloc[0:df_50_states_length][['state', '2020_census']]
USA_STATES_POP_2020_df = USA_STATES_POP_2020_df.sort_values(by='state').reset_index(drop=True).T

# Reformatting the 2020 U.S. state population data to match the 1970 to 2015 dataset structure
USA_STATES_POP_2020_df.reset_index(inplace=True)
USA_STATES_POP_2020_df.columns = USA_STATES_POP_2020_df.iloc[0]
USA_STATES_POP_2020_df = USA_STATES_POP_2020_df.drop(index=0).reset_index(drop=True)
USA_STATES_POP_2020_df.drop(columns=['DC', 'state'], inplace=True)
USA_STATES_POP_2020_df['Year'] = 2020
USA_STATES_POP_2020_df.loc[:, USA_STATES_POP_2020_df.columns != 'Year'] *= 1e-6

# Merging the 2020 U.S. state population data with the data from 1970 to 2015
USA_STATES_DATA_1970_2020 = pd.concat([USA_STATES_POP_1970_2015_df, USA_STATES_POP_2020_df], ignore_index=True)

print("DataFrame on U.S. States Population from 1970 to 2020 (in millions)")
print(USA_STATES_DATA_1970_2020 )