'''
In models.py, we have a model fin_Organization, which has ManytoMany fields: Segment and Country, connected to different models. 

Step 1: Fill the model with all NON-ManyToMany fields (orgnization_name) 
Step 2: For each entry, 'add' the id/pk of ManytoMany field

'''

import os, csv
from fintech.models import fin_Country, fin_Segment, fin_Organization # First two are the related ManytoMany fields

o_list = [ ]
with open('orgnn.csv') as csvfile: # CSV with organization name, country, and segment
	reader = csv.DictReader(csvfile)
	for row in reader:
		o_list.append(row)

orgs = fin_Organization.objects.all()
segs = fin_Segment.objects.all()
conts = fin_Country.objects.all()


for a in orgs: # Read one entry from the model
	comp = a.orgnization_name
	for one in o_list: # Read eveury dict from the list
		t = one['Company']
		if comp == t:
			o_seg = one['Segment'].split(',') #Split by coma and convert into a list. Else it will take each alphabet
			# print(len(o_seg))
			d = len(o_seg) # helps in assigning more than one entry.
			if d>0 : # ingnore empty/null values
				for s in range (0, d):
					seg_count = o_seg[s]
					print(t, seg_count)
					o_seg_id = segs.get(segment = seg_count).id #Gets the id/pk
					a.orgnization_segment.add(o_seg_id) #adds the id/pk. Here, we are giving field of fin_Organization (orgnization_segment), and not the parent model
					a.save()
			else: 
        pass
        
        
        
 for a in orgs:
	comp = a.orgnization_name
	for one in o_list:
		t = one['Company']
		if comp == t:
			o_cont = one['Country'].split(',')
			# print(len(o_seg))
			d = len(o_cont)
			if d>0 :
				for s in range (0, d):
					cnt_count = o_cont[s]
					print(t, cnt_count)

					try:
						o_cnt_id = conts.get(country = cnt_count).id
						a.orgnization_country.add(o_cnt_id)
						a.save()
					except :
						pass
			else: 
        pass
        
## We are using a try/except here as some of the countries for organizations are not mentioned in our Country model (e.g. Isle of man).
## Else, it will give this error: DoesNotExist: fin_Country matching query does not exist.
