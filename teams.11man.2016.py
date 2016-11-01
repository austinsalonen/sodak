from random import randint

teams = [ \
	("SF Washington", 46.333, 9, 0), \
	("SF Roosevelt", 44.444, 8, 1), \
	("Brandon Valley", 42.667, 6, 3), \
	("SF O'Gorman", 42.000, 6, 3), \
	("Aberdeen Central", 39.556, 4, 5), \
	("RC Central", 39.000, 3, 6), \
	("SF Lincoln", 39.000, 3, 6), \
	("RC Stevens", 38.333, 3, 6), \
	("Watertown", 38.333, 3, 6), \
	("Mitchell", 43.111, 8, 1), \
	("Harrisburg", 42.889, 7, 2), \
	("Spearfish", 40.778, 5, 4), \
	("Douglas", 39.556, 4, 5), \
	("Pierre T.F. Riggs", 39.222, 4, 5), \
	("Huron", 39.222, 4, 5), \
	("Yankton", 38.667, 3, 6), \
	("Sturgis Brown", 35.333, 0, 9), \
	("Brookings", 35.000, 0, 9), \
	("Tea Area", 47.000, 9, 0), \
	("St. Thomas More", 45.667, 9, 0), \
	("Madison", 45.111, 8, 1), \
	("SF Christian", 44.111, 8, 1), \
	("Dell Rapids", 43.556, 7, 2), \
	("Milbank Area", 43.000, 6, 3), \
	("Hot Springs", 41.556, 7, 2), \
	("West Central", 41.444, 5, 4), \
	("Dakota Valley", 41.333, 6, 3), \
	("Cheyenne-Eagle Butte", 40.444, 5, 4), \
	("Canton", 39.889, 4, 5), \
	("Belle Fourche", 39.556, 4, 5), \
	("St. Francis Indian", 38.889, 4, 5), \
	("Pine Ridge", 38.000, 3, 6), \
	("Vermillion", 37.556, 1, 8), \
	("Todd County", 37.444, 2, 7), \
	("Lennox", 36.333, 0, 9), \
	("Groton Area", 43.000, 7, 1), \
	("Aberdeen Roncalli", 42.125, 5, 3), \
	("Mobridge-Pollock", 40.375, 4, 4), \
	("Redfield/Doland", 38.000, 2, 6), \
	("Sisseton", 37.000, 1, 7), \
	("Crow Creek", 34.125, 0, 8), \
	("Sioux Valley", 41.000, 5, 3), \
	("Tri-Valley", 40.000, 4, 4), \
	("McCook Central/Montrose", 39.625, 4, 4), \
	("Flandreau", 37.250, 2, 6), \
	("Beresford", 37.250, 2, 6), \
	("Elk Point-Jefferson", 37.000, 1, 7), \
	("Winner", 47.250, 8, 0), \
	("Chamberlain", 42.375, 6, 2), \
	("Bridgewater-Emery/Ethan", 42.125, 5, 3), \
	("Parkston", 41.750, 5, 3), \
	("Wagner", 37.000, 1, 7), \
	("Red Cloud", 40.625, 5, 3), \
	("Bennett County", 40.625, 5, 3), \
	("Lead-Deadwood", 39.375, 3, 5), \
	("Custer", 38.375, 2, 6), \
	("Little Wound", 36.875, 2, 6), \
	("Jones County/White River", 36.500, 2, 6)]

def print_bracket(skip, take):
	playoff_count = take
	playoff_teams = sorted(teams, key=lambda x: (x[1], randint(0, 10)), reverse=True)[skip:(skip + take)]

	qualifiers = zip(playoff_teams, range(1, playoff_count + 1))
	home_teams = qualifiers[:playoff_count // 2]
	away_teams = sorted(qualifiers[playoff_count // 2:], key=lambda x: x[1], reverse=True)

	matchups = zip(away_teams, home_teams)
	for (away, a_seed), (home, h_seed) in matchups:
		print ("({8: >2}): {0} ({1}, {2}-{3})\n({9: >2}): {4} ({5}, {6}-{7})\n".format(away[0], away[1], away[2], away[3], home[0], home[1], home[2], home[3], a_seed, h_seed))


print ('### Division I')
print ('```')
print_bracket(0, 8)
print ('```')
print ('--- \n')
print ('#### Division II')
print ('```')
print_bracket(8, 16)
print ('```')
