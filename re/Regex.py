import re
import json

with open('pin.json', 'r') as json_file:
	pin_data = json.load(json_file)

for PIN in pin_data:
	PIN = PIN['PIN']
	if PIN:
		a = re.search(r"\d{4}|\d{6}", PIN)
		if a:
			print("{} matched !".format(PIN))
		else:
			print("{} is not valid PIN !".format(PIN))


