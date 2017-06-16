import csv
import os 

d = os.getcwd() 
print ("Current directory: ",d)
path =  "C:\\djangoenv\\djproject" # Set path of new directory here
os.chdir(path)
new_d = os.getcwd() 
print ("New directory: ",new_d)

from dashboard.models import Country


'''
Adding data from CSV to model object
'''

with open('countries_continents.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Country'], row['Continent'])
		p = Country(country=row['Country'], continent=row['Continent'])
		p.save()


from fintech.models import fin_News

with open('Fintech_up.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		o = fin_News( news_organization=row['Company'])
		o.save()
		p = fin_News(news_title=row['Title'], news_link=row['Link'],news_snippet=row['Snippet'], news_source=row['Source'],news_main_text=row['MainText'], news_trend=row['Trend'],news_date=row['Date'],news_segment=row['Segment'],news_country=row['Country'])
		p.save()
    
    

