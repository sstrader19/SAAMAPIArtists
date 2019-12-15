import requests 

import json 

#previous api key before i got locked out
#headers = {'X-Api-Key' :'FM4v9vsf3xtqxzRhriDdaUms6DFF7ChdCETaI0Fx', 'Accept': 'application/vnd.api+json'}

headers = {'X-Api-Key' :'hgvdqGXVwgpBar4dWm2O5r7WrP3cY0RSxUJkdL0n', 'Accept': 'application/vnd.api+json'}

offset_value = 0

page = 0 

while offset_value < 8220: 

	r = requests.get('https://api.si.edu/saam/v1/artists?page[offset]='+ str(offset_value)+ '&page[limit]=50?sort=-alphabetical_name', headers=headers) # + ?', headers=headers) #?page[limit]=20&page[offset]=' + str(offset_value)+ '&sort=-title', headers=headers)
		
	data = json.loads(r.text)

	data_source = data['data']

	json.dump(data_source, open('Artist' + str(page)+ '.json', 'w'), indent=2)

	offset_value = offset_value + 50

	page = page + 1 
