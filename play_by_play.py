import pandas as pd

# Get data into a dataframe object
play_by_play_df = pd.read_csv('NBA Hackathon - Play by Play Data Sample (50 Games).txt', sep="\t")
event_codes_df = pd.read_csv('NBA Hackathon - Event Codes.txt', sep="\t")

# Sort the events in order specified in prompt
play_by_play_df.sort_values(['Period', 'PC_Time', 'WC_Time', 'Event_Num'], ascending=[True, False, True, True])

# Create map of event codes
#print(event_codes_df[:10])

print(play_by_play_df[:10])

'''
# Go through and parse games

file = 'NBA Hackathon - Play by Play Data Sample (50 Games)' + '.txt'


# Get list of games
games_list = []

with open(file) as f:
	next(f)
	for line in f:
		#print(line)
		current_lines_game = line.split('\t')[0]
		if current_lines_game not in games_list:
			games_list.append(current_lines_game)
	print(games_list)

'''