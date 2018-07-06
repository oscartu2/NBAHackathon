import pandas as pd

file = 'NBA Hackathon - Event Codes.txt'

df = pd.read_csv(file, sep='\t', skiprows=(0))

print(df)