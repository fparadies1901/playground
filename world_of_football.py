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
