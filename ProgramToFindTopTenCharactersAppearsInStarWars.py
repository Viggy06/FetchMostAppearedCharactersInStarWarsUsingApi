#Program to find the ten characters who appear in the most Star Wars films

import requests
import json
import pandas as pd

unique_dict = []
res = requests.get("https://swapi.dev/api/people/").text
jdata = json.loads(res)
cnt = jdata["count"]

def fetch_data(cnt):
	for i in range(1,cnt+1):
			print("Processing", i)
			res = requests.get("https://swapi.dev/api/people/{}".format(i)).text
			jdata = json.loads(res)
			r = jdata.get('species')
			def sp(r):
				if len(r) == 1:
					spr = requests.get(r[0]).text
					j_sp = json.loads(spr)
					species = j_sp['name']
					return species
				else:
					return "Unknown or Human"
			try:
				unique_dict.append(
					{"Name": jdata['name'], "Height": jdata['height'], "Appearance": len(jdata['films']), "Species": sp(r)})
			except Exception as e:
				pass
	appearance_sorted = []
	for i in range(len(unique_dict)):
		for j in range(i+1,len(unique_dict)):
				if int(unique_dict[i]['Appearance']) <= int(unique_dict[j]['Appearance']):
					unique_dict[i], unique_dict[j] = unique_dict[j], unique_dict[i]
	appearance_sorted = unique_dict[:10]
	for i in range(len(appearance_sorted)):
		for j in range(i+1,len(appearance_sorted)):
			try:
				if int(appearance_sorted[i]['Height']) < int(appearance_sorted[j]['Height']):
					appearance_sorted[i],appearance_sorted[j] = appearance_sorted[j],appearance_sorted[i]
			except Exception as e:
				# print("Exception",e)
				pass

	df = pd.DataFrame(appearance_sorted)
	column_name = ["Name","Height","Species","Appearance"]
	df.to_csv('F:\Assignment\StarWarsApi\starwars.csv',index=False,columns=column_name) #Set location to create a csv file

#call fetch_data function
fetch_data(cnt)