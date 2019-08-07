#Import the Necessary Libraries
import csv, json
from collections import defaultdict

#Create an Address Book of all Contacts (items)
address_book = []  # this accumulates all of the lines

#Import the File Name here
with open("template.csv") as csv_file:
	reader = csv.reader(csv_file)
	#Loop through Contacts
	for row in reader:
		my_data = defaultdict(list)    
		#If they're in an organization
		my_data.update({"organizationId": None})
		#Folder ID (found from Export)
		my_data.update({"folderId": "Enter FolderId Here"})
		#Type of Entry (Identity)
		my_data.update({"type": 4})
		#Name of Entry
		my_data.update({"name": row[0]})
		#Notes
		my_data.update({"notes": None})
		#Favorites
		my_data.update({"favorite": "false"})
		#Entry Data for Identity
		my_data["identity"] = ({"title": None, "firstName": row[1], "middleName": row[2], "lastName": row[3], "email": row[5], "phone": row[7], "address1": row[12], "city": row[13], "state": row[14], "postalCode": row[15], "country": row[16], "address2": None, "address3": None, "company": None, "ssn": None, "username": None, "passportNumber": None, "licenseNumber": None})
		'''Optional Data Begin'''
		#Birthday
		if row[4] != "":
			my_data["fields"].append({"name": "Birthday", "value": row[4], "type": 0})
		#Phone 1 Type
		if row[6] != "":
			my_data["fields"].append({"name": "Phone1 Type", "value": row[6], "type": 0})
		#Phone 2 Type
		if row[8] !=  "":
			my_data["fields"].append({"name": "Phone2 Type", "value": row[8], "type": 0})
		#Phone 2
		if row[9] != "":
			my_data["fields"].append({"name": "Phone2", "value": row[9], "type": 0})
		#Phone 3 Type
		if row[10] != "":
			my_data["fields"].append({"name": "Phone3 Type", "value": row[10], "type": 0})
		#Phone 3
		if row[11] != "":
			my_data["fields"].append({"name": "Phone3", "value": row[11], "type": 0})
		'''Optional Data End'''
		#Append Contact to Address Book
		address_book.append(my_data)
#Output Data to JSON		
with open("contacts.json", "w") as out_file:
	#Output Adress Book with 2 indents
	json.dump(address_book, out_file, indent=2)