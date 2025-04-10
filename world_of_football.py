"""
A company operating in the world of football wishes to analyse the statistics of the English Premier League. 
A service provider has sent them information on certain matches in the English league. For various technical reasons and to simplify the exercise, 
we only have information for one team in one match.
"""

# loading the data
from load_data import load_data

team_names, team_possession, team_total_pass, ratings_player, pass_player, role_player = load_data()

# In the first part we will look at the first match with the id 1190418. What is the name of the team?
print(team_names[1190418])

# What was the team's possession for the match?
print(team_possession[1190418][1])

# Store in a ratings list the scores of the players obtained on the match. Display the list.
    # option 1, faster and more efficient
ratings = [float(i[1]) for i in ratings_player[1190418]]

print(ratings)

    # option 2
ratings = []
for i in ratings_player[1190418]:
    ratings.append(float(i[1]))

print(ratings)

# Display the name of the player with the highest score.

    #Set two variables maximum_index and maximum to 0
maximum_index = 0
maximum = 0

    # Browse the ratings list using enumerate, updating maximum_index and maximum.
for i, j in enumerate(ratings):
    if j > maximum:
        maximum = j
        maximum_index = i

print(f"The player with the highest score is {ratings_player[1190418][maximum_index][0]}.")

# Some players have a score of 0. What were their positions?
# idea: using zip 