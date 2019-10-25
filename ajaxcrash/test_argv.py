import json
import csv
import sys
from pprint import pprint
# we are using pprint for making the output more readable.

#read file
def jsontocsv(input_file,output_file):
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as jsonfile:
        data=jsonfile.read()
    jsonobj = json.loads(data)
    keylist = []
    for key in jsonobj[0]:
      keylist.append(key)
    f = csv.writer(open(output_file, "w"))
    f.writerow(keylist)
    for record in jsonobj:
        currentrecord = []
    #Iterate through each key in the keylist and add the data to our current record list
        for key in keylist:
            currentrecord.append(record[key])
        f.writerow(currentrecord)
    return output_file
if __name__ == "__main__":
    pass
