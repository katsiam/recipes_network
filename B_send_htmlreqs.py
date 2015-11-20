'''
Title: Script to pull some data from HTMLs 
Subtitle: Step 2 out of ___
Language: Python 3.4
Author: Katsia M
Date: 11/10/2015
'''

#import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
import re


#TODO: loop through multiple files
with open('out20140101') as f:
 data  = json.load(f)

#Ex. 
type(data) #list

type(data[i]) #list of dictionaries in case of several recipes per day

type(data[i][j]) #nth recipe as dict per day

print(data[0][0]['web_url_']) #url inside the dict
#end if Ex.

#pull unique urls from stored dictionaries in STEP 1
web_url_uniq=[]
for i in range(len(data)):
 for j in range(len(data[i])):
  if (data[i][j]['web_url_'][0:26]=="http://cooking.nytimes.com"):
   print(data[i][j]['web_url_'])
   #create a unique list of urls
   web_url_uniq.append(data[i][j]['web_url_'])
  else:
   print('Not from Cooking')
 else:
  pass
else:
 print('End of script')
 
web_url_uniq1=list(set(web_url_uniq))

#create a list of dictionaries by url
startdata=[]

#create and parse html requests
for links in web_url_uniq1:
 r = requests.get(links)
 soup = BeautifulSoup(r.text, 'html.parser')
 newdic={}
 #store url, cooktime, special diets tags, ratingvalue, ratingCount, ingredients
 newdic['url']=links

 if soup.header.div.ul.li.meta['itemprop']=='cookTime':
  newdic['cookTime']=soup.header.div.ul.li.get_text()
 else:
  newdic['cookTime']="None"
  
 specdiet=[]
 zz=soup.find_all("p", 'special-diets tag-block')
 for i in range(1,len(str(zz).split('special-diet\">'))):
  a_=re.search('</a>', str(zz).split('special-diet\">')[i]).start()
  b_=str(zz).split('special-diet\">')[i][0:a_]
  print(b_)
  specdiet.append(b_)
 else:
  specdiet.append("None")

 newdic['specialDiet']=specdiet
 
 newdic['ratingVlue']=soup.find(itemprop="ratingValue").get_text()
 newdic['ratingCount']=soup.find_all(itemprop="ratingCount").get_text()
 
 ingredients=[]
 zz1 = soup.find_all("span", attrs={"itemprop": "name"})
 for i in range(1,len(zz1)):
  c_=zz1[i].get_text()
  if c_ != "The New York Times Company":
   ingredients.append(c_)

 newdic['recipeIngredient']=ingredients

startdata.append(newdic)

with open('links'+infile, "w") as outfile:
  json.dump(startdata, outfile, indent=4)
  
print('Job #2 is done, madam') 


