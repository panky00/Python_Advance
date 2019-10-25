import json
import csv
from pprint import pprint
# we are using pprint for making the output more readable.

#read file
#f = csv.writer(open("epg.csv", "w"))
with open('EPALL20910.json', 'r') as jsonfile:
#with open('epg_test.json', 'r') as jsonfile:
  jsonobj = json.load(jsonfile)
count = 0
 
#print (dir(jsonobj)) 
for obj in jsonobj:
  #print (obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'])
  i= obj["fvCEp"]
  #print (type(i))
  #print (i.keys())
  if 'children' in i:
    ii = i['children']
    #print (type(ii))
    for i_sub in ii:
      if 'fvRsCEpToPathEp' in i_sub:
        ii_sub=i_sub['fvRsCEpToPathEp']['attributes']
        keylist = []
        #print (obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'],ii_sub['tDn'])
  keylist = [obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'],ii_sub['tDn']]
  keylist.append(key)
        #keylist.append
  print(keylist),
  count +=1
print((count))



  

    

    
  #for child_atri in epg_child:
  #  gran_child= (child_atri['fvRsCEpToPathEp']['attributes']['tDn'])
  #  print (gran_child)