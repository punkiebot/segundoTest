import requests

url= "www.nasa.gov"

try:
	get_response= requests.get("http://"+url)
	print(get_response)

except requests.exceptions.ConnectionError:	
	print("There is no website")