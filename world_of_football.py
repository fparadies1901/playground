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
# idea: using zip # fast solution

position = [j[1] for i, j in zip(ratings_player[1190418], role_player[1190418]) if float(i[1]) == 0]
print(position)

# normal solution
position = []

for i, j in zip(ratings_player[1190418], role_player[1190418]):
    if float(i[1]) == 0: # using tuples
        position.append(j[1])

print(position)

# Create a ratings_no_zero list containing all the ratings scores except those equal to 0.
# creating ratings again
ratings = [float(i[1]) for i in ratings_player[1190418]]

# comprehension
ratings_no_zero = []
ratings_no_zero = [i for i in ratings if i > 0]
print(ratings_no_zero)

# long version
ratings_no_zero = []
for score in ratings:
    if score > 0:
        ratings_no_zero.append(score)

print(ratings_no_zero)

# What is the average score? Use the ratings_no_zero list.
# using for loop 
sum_score = 0
for i in ratings_no_zero:
    sum_score += i

count_score = len(ratings_no_zero)

avg_score = round(sum_score / count_score,2)
print(avg_score)

# using sum
avg_score = sum(ratings_no_zero ) / len(ratings_no_zero )
print(round(avg_score, 2))

# Create a mean_ratings function that takes as its parameter the id of a match and returns the average of the player ratings.
def mean_ratings(id_match):
    # creating list of ratings without zero value
    ratings_no_zero = []
    ratings_no_zero = [float(i[1]) for i in ratings_player[id_match] if float(i[1]) != 0]
    
    # creating the average 
    sum_score = 0
    
    for i in ratings_no_zero:
        sum_score += i

    avg_score = round(sum_score / len(ratings_no_zero),2)
    
    return avg_score

print(mean_ratings(1190424))

# Display the result for the second match whose id is 1190424. Is this average higher than in the first match?
print(mean_ratings(1190424) > mean_ratings(1190418))

# Check that by summing up the number of passes of each player we get the total number of passes made by the team.
"""
team_total_pass = 0
    
for i in pass_player[1190418]:
        team_total_pass += int(i[1])

print(team_total_pass)
"""

def total_pass_team(id_match):
    team_total_pass = 0
    
    for i in pass_player[id_match]:
        team_total_pass += int(i[1])
    
    return team_total_pass

total_pass_team(1190418)

# More generally, which team had the most possession in a match?
max_possession = 0
top_team = None

for match_id, (team, possession) in team_possession.items():
    possession_float = float(possession)
    
    if possession_float > max_possession:
        max_possession = possession_float
        top_team = team

"""
for i in team_possession.keys() :
    if float(team_possession[i][1]) > maximum : 
        maximum = float(team_possession[i][1])
        team = team_possession[i][0]
"""

print(f"{top_team} had the most possession with {max_possession}%")

'''
Now let's assume that the company wants to have quick access to basic information about a team for any match. For example, it wants to have access to the 
list of players who have participated in a match.
'''

# Create a function team_player_names that returns a list of the names of the players in the team for a given match and their positions. 
# Display the result for the match 1190496.
def team_player_names(id_match):
    list_player = []
    
    if id_match in role_player:
        for player, position in role_player[id_match]:
            list_player.append((player, position))
    
    return list_player

team_player_names(1190496)

# Create a midfielders_name function that returns the names of the central midfielders (MC) of the team for a given match. Display the result for the match 1190422.
def midfielders_name(id_match):
    list_player = []
    
    if id_match in role_player:
            for player, position in role_player[id_match]:
                if position == 'MC':
                    list_player.append((player))
    
    return list_player

midfielders_name(1190422)

# Create a worst_player function that returns, for a given match, the worst player in the team. Display the result for the match 1190496.
def worst_player(id_match):
    worst_score = float('inf')
    worst_player_name = None
    
    if id_match in ratings_player:
        for player, score in ratings_player[id_match]:
            if score < worst_score and score > 0:
                worst_score = score
                worst_player_name = player
    
    return worst_player_name

worst_player(1190496)

