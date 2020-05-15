# Sample API code

# Tutorial from https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236

import requests


# sample api used: http://open-notify.org/

def nasa_API():
	
	response = requests.get('http://api.open-notify.org')
	
	# prints the text attribute of the response
	#print(response.text)
	
	# prints the status code attribute of the response
	print("Valid status code:", response.status_code)
	
	request2 = requests.get('http://api.open-notify.org/fake-endpoint')
	print("Invalid status code", request2.status_code)
	
	# returns json from the given endpoint
	people = requests.get('http://api.open-notify.org/astros.json')
	#print(people.text)
	
	# convert to json format (i.e.  python dictionary with key value pairs)
	people_json  = people.json()
	#print(people_json)
	
	#To print the number of people in space
	print("Number of people in space:", people_json['number'])
	
	#To print the names of people in space using a for loop
	for p in people_json['people']:
		print("Name:", p['name'], "Space Craft:", p['craft'])
	

# uses API: https://www.datamuse.com/api/

def vocab_API():
	
	# return data from the given endpoint with the given constraints
	# get words that rhyme with jingle
	# rel = related, rhy = rhyme
	# i.e. in the words end point, return words that rhyme with jingle
	parameter = {"rel_rhy":"jingle"}
	response = requests.get('https://api.datamuse.com/words',parameter)
	
	rhyme_json = response.json()
	
	print("Words that rhyme with Jingle:")
	
	# print the first 5 values returned
	for i in rhyme_json[0:5]:
		print(i['word'])
		
	print()
	
	# synonym for human
	
	parameter = {"rel_syn":"human"}
	response = requests.get('https://api.datamuse.com/words',parameter)
	syn_json = response.json()
	
	print("Synonyms for the word human")
	
	for i in syn_json[0:5]:
		print(i['word'])
	
	
def main():
	
	print("Running NASA API")
	print()
	nasa_API()
	print()
	
	print("Running vocab API")
	print()
	vocab_API()
	

# use main class by default

if __name__ == '__main__':
	main()

