import pandas as pd

dictionary_grocery = {"Name": ["Jars of honey", "Packets of flour", "Bottles of wine"],
                      "Expiration Date": ["08/10/2025", "09/25/2024", "10/15/2023"],
                      "Quantity": [100, 55, 1800],
                      "Price per unit": [2, 3, 10]}

df_grocery = pd.DataFrame(dictionary_grocery)

