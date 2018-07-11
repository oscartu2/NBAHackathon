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
periods = play_by_play_df.Period.unique()
games_list = []
count = 1

# Repeat for every game	
for game_number in game_ids:
	player_maps = {}
	print('GAME: ' + str(count))
	current_game = play_by_play_df.loc[play_by_play_df['Game_id'] == game_number]

	# Repeat for every p eriod
	for period in periods:
		current_period = current_game.loc[current_game['Period'] == period]
		event_msg_type = current_period['Event_Msg_Type']
		action_type = current_period['Action_Type']

		for index, events in current_period.iterrows():
			event_msg_type_description = event_codes_df.loc[(event_codes_df['Event_Msg_Type'] == event_msg_type[index]) & (event_codes_df['Action_Type'] == action_type[index])]['Event_Msg_Type_Description']

			input(event_msg_type_description)
			# IF event is related to points
			# GET current players and add +/- to player_maps
		
		

		count += 1