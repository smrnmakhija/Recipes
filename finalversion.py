import requests
from bs4 import BeautifulSoup
import urllib
	

try:
	inp = raw_input("Enter ingredients (seperated by commas): ")
	p1 = inp.split(",")
except("TypeError,ValueError"):
	print "error"

url = 'https://recipeland.com/recipes/ingredients/search?utf8=%E2%9C%93&search_type=Ingredients&q='

for item in p1:
	n_url = url + item + '+'
	url = n_url


url = url + '&sort=r'
sc = requests.get(url)
pt = sc.text
soup = BeautifulSoup(pt,"html.parser")

#title
d1 = {}
l1 =[]
print ("\n\n List of possible recipes:\n")	
for link in soup.findAll("a",{"target":"_parent"}):
	href = link.get('href')
	title = link.get('title')
	print (title)
	print (href)
	print ("\n")
	d1[title]=href
l1.append(d1)


#ingredients
try:
	title_inp = raw_input("\nEnter the title:")
	link_inp = (d1[title_inp])
except(NameError,KeyError):
	print "error"
	
sc2 = requests.get(link_inp)
pt2 = sc2.text
soup = BeautifulSoup(pt2,"html.parser")


ing = []
am=[]
me=[]
print ("\n\nIngredients:")
for link7 in soup.findAll("td",{"class":"amount"}):
	amt = link7.string
	am.append(amt)
for link8 in soup.findAll("td",{"class":"measure"}):
	meas = link8.string
	me.append(meas)
for link2 in soup.findAll("span",{"class":"ingredient"}):
	ingredient = link2.string
	#print (ingredient)
	ing.append(ingredient)
l=len(ing)
for i in range(0,l-1):
	print (am[i] + "\t"+ me[i] + "\t\t" + ing[i])

print ("\n\n Cooking instructions to guide you:\n")	
#for link6 in soup.findAll("div",{"itemprop":"recipeInstructions"}):
for link5 in soup.findAll('p'):
	direct = link5.string
	if direct == ' ':
		continue
	print (direct)



#grocery

#print (ing)
print ("\n\n Missing some ingredients? Find the grocery links here:\n")			
for i in ing:
	flag=0
	for j in p1:
		if i == j:
			flag=1
			break
	if flag == 0:
			print('http://www.bigbasket.com/ps/?q=' +i)



#youtube

tw=title_inp.split()
url_yt = 'https://www.youtube.com/results?search_query='

for item in tw:
	n_url_yt = url_yt + item + '+'
	url_yt = n_url_yt
	
sc3 = requests.get(url_yt)
pt3 = sc3.text
soup = BeautifulSoup(pt3,"html.parser")
#print url_yt
print ("\n\nFeel free to assist yourselves with these videos:\n")	
for link3 in soup.findAll("a",{"class":"yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 spf-link "}):

	href = "https://www.youtube.com/"+ link3.get('href')
	#title = link.get('title')
	print (href)






	


