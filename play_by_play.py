import pandas as pd

pd.set_option('expand_frame_repr', False)

# Get data into a dataframe object
play_by_play_df = pd.read_csv('NBA Hackathon - Play by Play Data Sample (50 Games).txt', sep="\t")
event_codes_df = pd.read_csv('NBA Hackathon - Event Codes.txt', sep="\t")
game_lineup_df = pd.read_csv('NBA Hackathon - Game Lineup Data Sample (50 Games).txt', sep="\t")


# Sort the events in order specified in prompt
play_by_play_df.sort_values(['Period', 'PC_Time', 'WC_Time', 'Event_Num'], ascending=[True, False, True, True])

# Create map of event codes
#print(event_codes_df[:10])
game_ids = play_by_play_df.Game_id.unique()
games_list = []
count = 1
for game_number in game_ids:
	player_maps = {}
	print('GAME: ' + str(count))
	current_game = play_by_play_df.loc[play_by_play_df['Game_id'] == game_number]
	current_players = game_lineup_df.loc[game_lineup_df['Game_id'] == game_number]
	input(current_players)
	#for event in current_game:
		# If player has +/- event in same period, perform calculation

	#print(games_list)
	#input("er")
	count += 1




#print(play_by_play_df[:10])

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