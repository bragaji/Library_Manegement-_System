

#from difflib import get_close_matches

'''def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()'''

'''

def closeMatches(patterns, word): 
	print(get_close_matches(word, patterns)) 

a="harry potter"
b="har"
print closeMatches(a,b)	'''

'''
import re
	
def check(string):
	regex=re.compile("h+\w*")
	match_object=regex.findall(string)

	if(len(match_object) != 0):
		for word in match_object:
			print word

check()'''

'''
import difflib

my_str = 'harry'
str_list = ['harry potter' , 'hello word', 'famous five', 'potter hari', 'crushing it']
#best_match = difflib.get_close_matches(my_str,str_list,1)[0]
#score = difflib.SequenceMatcher(None, my_str, best_match).ratio()
for word in str_list:
    print "score for: " + my_str + " vs. " + word + " = " + str(difflib.SequenceMatcher(None, my_str, word).ratio())'''


import csv
#import re

test_input= "The Alchemist"	

with open('test_books.csv','r') as csv_file:
	
	data= csv.DictReader(csv_file)
	current_author=""
	reccomendation_based_on_current_author=[]
	reccomendation_based_on_average_ratings=[]

	for line in data:
		if(test_input == line['title']):
			current_author=line['authors']

	print "Current authors:  ", current_author 						#### Current authors based on selected book 

	csv_file.seek(0)												#### Set DictReader back to start of file

		###############  Books From Similar author


	for line in data:
		if(line['title'] == test_input):
			continue
		if(len(set(line['authors'].split(',')).intersection(set(current_author.split(',')))) > 0 ):
			reccomendation_based_on_current_author.append(line['title'])		

	if(len(reccomendation_based_on_current_author) > 0):
		print " \n Also from :",  current_author 
		print "\n", reccomendation_based_on_current_author								######   Reccomends books based on atleast one author
		print " \n Enjoy your Book ! \n "	
	else:
		print " \n Enjoy your Book ! \n "	

	print "*****************************************************************************************************************************************"
	csv_file.seek(0)

			#####################   Top Rated Books 
	next(data)																				### We dont want the headers in list		

	for line in data:
		if(line['average_rating'] >= str(4.5) ):
			reccomendation_based_on_average_ratings.append(line['title'])					######   Recommends books based on average ratings of all books

	if(len(reccomendation_based_on_average_ratings) > 0):
		print "\n Also Check Out Top Rated Books in all Categories : \n"
		print reccomendation_based_on_average_ratings
		print "\n Thanks & Keep Reading \n"		
	
	print "*****************************************************************************************************************************************"

'''	for line in data:
		if(len(set(ine['authors'].split(',')).intersection(set(current_author.split(',')))) > 0 ):
			reccomendation_based_on_current_author.append(line['title'])



	print reccomendation_based_on_current_author		
'''
'''	print "Also from ", current_author
	print "\n"
	for rec_buk in reccomendation_based_on_current_author:
		 
		print rec_buk, "\n"					'''							###### Printing other buks based on current author of searched buk
			 
			
			

