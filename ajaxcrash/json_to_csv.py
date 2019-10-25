import json
import csv
import sys
from pprint import pprint
# we are using pprint for making the output more readable.

#read file

if __name__ == "__main__":


  with open('gituser.json', 'r') as jsonfile:
    data=jsonfile.read()
  
  jsonobj = json.loads(data)
  
  
  keylist = []
  for key in jsonobj[0]:
    keylist.append(key)
  
  f = csv.writer(open("test.csv", "w"))
  f.writerow(keylist)
  
  
  for record in jsonobj:
      currentrecord = []
  #Iterate through each key in the keylist and add the data to our current record list
      for key in keylist:
          currentrecord.append(record[key])
      f.writerow(currentrecord)