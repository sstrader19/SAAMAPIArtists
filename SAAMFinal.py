import json
import csv 

with open('SAAM_ArtistTable.csv', 'w') as csvfile: 
	
	fieldnames =['firstname','lastname','gender','library_of_congress_id','ulan_id','viaf_id','wikiDataID','birth_place','birth year', 'death_year', 'nationalities']
	
	writer = csv.writer(csvfile)
	writer.writerow(fieldnames)
	#writer.writeheader()
	
	file = 0

	for file in range (0,73): 

		with open('A_JSON/Artist' + str(file) + '.json','r') as f:
			
			data = json.load(f)
			
			for artist in data: 
				# for info, stuff in artist['attributes'].items(): 
				# 	print
				artist_info = []
				
				firstname = artist['attributes']['firstname']
				artist_info.append(firstname)
 
				lastname = artist['attributes']['lastname']
				if lastname != None:
					artist_info.append(lastname)

				gender = artist['attributes']['gender']
				if gender != None:
					artist_info.append(gender)

				locID = artist['attributes']['library_of_congress_id']
				if 'library_of_congress_id' != None:
					artist_info.append(locID)

				ulanID = artist['attributes']['ulan_id']
				if 'ulan_id' != None: 	
					artist_info.append(ulanID)

				viafID = artist['attributes']['viaf_id']
				if 'viaf_id' != None:	
					artist_info.append(viafID)

				wikiDataID = artist['attributes']['wikidata_id']
				if 'wikidata_id' != None:
					artist_info.append(wikiDataID)

				birthPlace = artist['attributes']['birth_place']
				if 'birth_place' != None: 
					artist_info.append(birthPlace)

				birthYear = artist['attributes']['birth_year']
				if 'birth_year' != None: 
					artist_info.append(birthYear)


				deathYear = artist['attributes']['death_year']
				if 'birth_year' != None: 
					artist_info.append(deathYear)



				#relationships dictionary, and inside that a nationalities dictionary 
				#i was referencing what wasn't there 
				if 'data' in artist['relationships']['nationalities']:
					if artist['relationships']['nationalities']['data'] != None: 
						#if 'id' in artist['relationships']['nationalities']['data']:
						nationalities = artist['relationships']['nationalities']['data']['id']
						if 'nationalities' != None: 
							artist_info.append(nationalities)
				
				writer.writerow(artist_info)

				file = file + 1
				

				# for key, value in artist_infoz.items():
				# writer.writerow(key,value)
				#print(artist_info)

				# for data in artist_info: 
				# 	for k, v in data.items(): 
				# 		

				






