import pandas as pd
import json

#TODO: loop through multiple files
with open('out20140101') as f:
 data  = json.load(f)

#Ex. 
type(data) #list

type(data[i]) #list of dictionaries in case of several recipes per day

type(data[i][j]) #nth recipe as dict per day

print(data[0][0]['web_url_']) #url inside the dict
#end if Ex.

#pull urls from stored dictionaries in STEP 1
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
###

#create html requests

