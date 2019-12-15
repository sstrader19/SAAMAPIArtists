#Pulls ULAN data based on IDs in Artist Table, creates a CSV with Nationalities Data
import json 
import csv 
import requests

url_list = []
afam = []

#stores 



with open ('ULAN_Table.csv', 'w') as csvfile: 
	fieldnames = ['ULAN_ID','artist_name', 'nationality']
	writer = csv.writer(csvfile)
	writer.writerow(fieldnames)

	with open('SAAM_ArtistTable.csv', 'r') as f: 

		reader = csv.reader(f)
		headers = next(reader)

		for row in reader: 
			
			if row[4] == ' ': 
				
				continue

			else: 

				ulan_number = row[4]

				url_list.append(ulan_number)


				for url in url_list:
					source = 'http://vocab.getty.edu/ulan/' + str(url) + '.json'
					#gets rid of data that does not have ULAN ID
					if source != 'http://vocab.getty.edu/ulan/.json':

						r = requests.get(source)

						data = json.loads(r.text)

						#accesses first dictionary 
						dictionary = data['results']

						#accesses list in the dictionary
						for results in dictionary['bindings']: 

							subject = results['Subject']['value']

							predicate = results['Predicate']['value']

							object_value = results['Object']['value']

							if predicate == 'http://vocab.getty.edu/ontology#nationalityNonPreferred':
								#afam.append(subject)
								
								afam.append(object_value)

								print(object_value)
								 


							

# def get_afam():
# 	dictionary = data['results']
# 	for results in dictionary['bindings']: 
# 		object_value = results['Object']['value']
# 		if object_value == 'http://vocab.getty.edu/aat/300018125': 
# 			print(subject)

# get_afam()
		






							# object_value = results['Object']['value']

							# print(object_value)










				# for url in url_list: 
					
				# 	data = requests.get(url)

				# 	dictionary = json.loads(data.text)

				# 	for results in dictionary['results']['bindings']: 
						
				# 		subject = results['Subject']['value']
					
				# 		predicate = results['Predicate']['value']			 

				# 		object_value = results['Object']['value']

				# 		if subject == 'http://vocab.getty.edu/ulan/' + str(url): 
				# 			demo_list.append(subject)

				# 		if predicate == 'http://schema.org/nationality': 
				# 			demo_list.append(predicate)

				# 		if object_value == 'http://vocab.getty.edu/ontology#nationalityNonPreferred': 
				# 			demo_list.append(object_value)

				# 		writer.writerow(demo_list)
							





			
			#print(test)






		# 		print(key, values)

		# for results in dictionary: 

		# 	for bindings in dictionary[results]:

		# 		for data in dictionary[results][bindings]: 
				




			# if ULAN_ID != None: 
			# 	newdata_list.append

			# artist_name= 
			# if artist_name != None: 
			# 	newdata_list.append

			# nationality= 
			# if nationality != None: 
			# 	newdata_list.append