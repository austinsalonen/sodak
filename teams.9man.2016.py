from random import randint

teams = [ \
	("Webster Area", 46.875, 8, 0), \
	("Britton-Hecla", 44.500, 7, 1), \
	("Clark/Willow Lake", 40.750, 4, 4), \
	("Ipswich/Edmunds Central", 39.375, 3, 5), \
	("Great Plains Lutheran", 39.000, 3, 5), \
	("Dakota Hills", 38.000, 2, 6), \
	("Florence/Henry", 37.625, 2, 6), \
	("Tiospa Zina", 37.625, 2, 6), \
	("Baltic", 46.125, 8, 0), \
	("Chester Area", 44.125, 7, 1), \
	("Canistota", 43.000, 7, 1), \
	("Deuel", 42.125, 5, 3), \
	("Garretson", 40.500, 3, 5), \
	("Arlington/Lake Preston", 40.375, 4, 4), \
	("Deubrook Area", 36.625, 1, 7), \
	("Wolsey-Wessington", 44.125, 7, 1), \
	("Mt. Vernon/Plankinton", 43.750, 7, 1), \
	("Bon Homme", 42.875, 5, 3), \
	("Kimball/White Lake", 42.250, 4, 4), \
	("Woonsocket/Wess. Springs/Sanborn Central", 41.750, 5, 3), \
	("Miller", 39.750, 3, 5), \
	("Gregory", 47.250, 8, 0), \
	("Stanley County", 44.625, 6, 2), \
	("Hill City", 42.125, 5, 3), \
	("Lyman", 40.375, 4, 4), \
	("Herreid/Selby Area", 39.500, 2, 6), \
	("McLaughlin", 37.125, 3, 5), \
	("RC Christian", 36.375, 0, 8), \
	("Potter County", 46.500, 8, 0), \
	("Warner", 46.125, 8, 0), \
	("Castlewood/Estelline", 43.375, 7, 1), \
	("Eureka/Bowdle", 38.375, 2, 6), \
	("Waverly-South Shore", 38.000, 2, 6), \
	("Tri-State", 36.625, 1, 7), \
	("Colman-Egan", 43.750, 7, 1), \
	("Gayville-Volin", 42.375, 6, 2), \
	("Parker", 40.750, 4, 4), \
	("Irene-Wakonda", 39.125, 2, 6), \
	("Viborg-Hurley", 36.875, 2, 6), \
	("Elkton-Lake Benton", 35.625, 0, 8), \
	("Scotland", 40.750, 4, 4), \
	("Hanson", 38.750, 2, 6), \
	("Platte-Geddes", 38.000, 2, 6), \
	("Andes Central/Dakota Christian", 36.250, 1, 7), \
	("Menno/Marion", 36.250, 1, 7), \
	("Tripp-Delmont/Armour", 35.250, 0, 8), \
	("Sully Buttes", 44.500, 7, 1), \
	("Philip", 43.500, 6, 2), \
	("Lemmon/McIntosh", 42.500, 5, 3), \
	("New Underwood", 41.500, 4, 4), \
	("Kadoka Area", 38.375, 2, 6), \
	("Newell", 38.375, 2, 6), \
	("Langford Area", 43.750, 7, 1), \
	("Hamlin", 43.500, 6, 2), \
	("Faulkton Area", 41.875, 4, 4), \
	("Leola/Frederick", 40.375, 4, 4), \
	("Northwestern", 39.000, 3, 5), \
	("Hitchcock-Tulare", 37.125, 0, 8), \
	("Oldham-Ramona/Rutland", 40.625, 5, 3), \
	("Howard", 40.125, 3, 5), \
	("Alcester-Hudson", 39.750, 3, 5), \
	("Dell Rapids St. Mary", 39.375, 3, 5), \
	("De Smet", 39.375, 3, 5), \
	("Corsica-Stickney", 46.125, 8, 0), \
	("Colome", 44.125, 7, 1), \
	("Burke/South Central", 39.000, 3, 5), \
	("Sunshine Bible Academy", 39.000, 3, 5), \
	("Avon", 37.625, 2, 6), \
	("Lower Brule", 36.750, 3, 5), \
	("Harding County", 46.875, 8, 0), \
	("Wall", 43.500, 6, 2), \
	("Bison", 42.750, 6, 2), \
	("Faith", 39.889, 4, 5), \
	("Timber Lake", 38.625, 3, 5), \
	("Edgemont", 37.250, 2, 6), \
	("Dupree", 34.600, 1, 4), \
	("Crazy Horse", 33.375, 0, 8) ]

qualifiers = zip(sorted(teams, key=lambda x: (x[1], randint(0, 10)), reverse=True)[:16], range(1, 17))
home_teams = qualifiers[:8]
away_teams = sorted(qualifiers[8:], key=lambda x: x[1], reverse=True)

matchups = zip(away_teams, home_teams)
for (away, a_seed), (home, h_seed) in matchups:
	print ("({8: >2}): {0} ({1}, {2}-{3})\n({9: >2}): {4} ({5}, {6}-{7})\n".format(away[0], away[1], away[2], away[3], home[0], home[1], home[2], home[3], a_seed, h_seed))
	
