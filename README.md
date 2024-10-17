Project Name: Electoral Map Shift Visualizer

Overview: The purpose of this project is to predict how electoral votes for each state are going to change from 2020 to 2030. To achieve this, two Kaggle datasets were
used including a dataset containing U.S. state populations from 1900 to 2017, and another dataset containing U.S. state populations for 2020. These two datasets were
merged to form a DataFrame containing U.S. state populations from 1970 to 2020 for every five years. Then, a polynomial regression of degree 2 was applied to the 
DataFrame to make predictions of the population for each state in 2030. These predicted populations were then processed through the Method of Equal Proportions to
estimate how the 538 electoral votes would be distributed in 2030, and the results were stored in a dictionary. Then, another dictionary to track the difference
in electoral votes for each state from 2020 to 2030 was created and made by taking the difference of the state's predicted electoral vote in 2030 and the state's
recorded electoral vote in 2020. This new dictionary was then processed in Matplotlib and two bar graphs containing all of the states with a non-zero electoral
vote change were plotted.

Explanation of Computing Apportionment using the Method of Equal Proportions: The total amount of electoral votes is 538. The District of Columbia (Washington D.C.) 
is automatically granted 3 electoral votes as per Amendment 23, leaving only 535 electoral votes remaining. As all of the 50 states are guarenteed to have 
2 senators each, another 100 electoral votes is deducted from the total leading to 435 electoral votes remaining. Each state is also guarenteed to have at least 
1 House of Representative, leading to another 50 electoral votes being deducted leading to only 385 electoral votes left. The remaining 385 electoral votes are 
distibuted through the Method of Equal Proportions which entails calculating the priority value of a state to gain another seat based on the number of seats it 
currently has, and granting a seat to the state with the greatest priority.

The formula for calculating priority is as follows -> Priority = P / √(n * (n - 1)) where P is a state's population and n is the nth seat in the House of
Representative that the state is targetting. A max-oriented priority queue was created to effectively track the state with the greatest priority and a dictionary
was created to store  the number of electoral votes that each state has. Each state initially started out with 3 electoral votes (2 Senates and 1 House of Representative).
After granting each state 1 free seat, each state is added to the priority queue with n being set to 2 for each state since each state is now targetting a second seat in 
the House of Representataives. In this project, a for loop was implemented to distribute the remaining 385 electoral votes where state with the greatest priority was 
popped from the queue and the dictionary made the apropriate increment to the state's number of electoral votes while also decrementing the remaining amount of seats 
left to distribute by 1 during each iteration. Thus, at the end of the for loop, the dictionary stored the approximate number of electoral votes that each state
will have in 2030 along with Washington D.C.'s 3 electoral votes, which all sum up to the original total of 538 electoral votes.

Sources for Explanation:
https://www.census.gov/topics/public-sector/congressional-apportionment/about/computing.html
https://www.census.gov/content/dam/Census/library/factsheets/2021/apportionment-101.pdf

Kaggle Datasets:

Historical State Populations from 2000 to 2017
https://www.kaggle.com/datasets/hassenmorad/historical-state-populations-19002017

Population of USA as a whole from 1950 to 2020
https://www.kaggle.com/datasets/anandhuh/population-data-usa

Programming Languages: Python

Libraries:
Matplotlib
NumPy
Pandas
Scikit-learn




