import csv
import urllib
import json
import pprint
def main():
	writeto = open("datafile.txt", "w")
	with open('school1.csv', 'rb') as fh:
		reader = csv.DictReader(fh)
		for row in reader:
			dictionary = row
			address = row['Program Address']
			address = address.split()
			zipcode = row['Program Zip']
			address = '+'.join(address)
			address = address + '+' + 'NYC' + '+' + 'NY' + '+' + zipcode
			URL2 = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&sensor=false"
			googleResponse = urllib.urlopen(URL2)
			jsonResponse = json.loads(googleResponse.read())
			#pprint.pprint(jsonResponse)
			test = json.dumps([s['geometry']['location'] for s in jsonResponse['results']], indent=3)
			if (test):
				x = test
				x = x.split()
				try:
				    lat = x[3].strip(',')
				except IndexError:
				    lat=''
				try:
				    lng = x[5]
				except IndexError:
				    lng='' 
				dictionary['lat'] = lat
				dictionary['lng'] = lng
			string = ''
			for key, value in dictionary.iteritems():
				string = string + ',' +value
			string = string + '\n'
			writeto.write(string)
	writeto.close()
if __name__ == "__main__":
	main() 