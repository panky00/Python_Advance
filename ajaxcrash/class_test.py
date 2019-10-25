import json
import csv
import sys
from pprint import pprint
# we are using pprint for making the output more readable.

#read file
class jsonacsv:
    def __init__(self,input_file,output_file):
        self.input_file = sys.argv[1]
        print('input file is: %s' %input_file)
        self.output_file = sys.argv[2]
        print('output file is: %s' %output_file)



    def jsontocsv(self):
        #input_file = sys.argv[1]
        #output_file = sys.argv[2]
        with open(self.input_file, 'r') as jsonfile:
            data=jsonfile.read()
        jsonobj = json.loads(data)
        keylist = []
        for key in jsonobj[0]:
          keylist.append(key)
        f = csv.writer(open(self.output_file, "w"))
        f.writerow(keylist)
        for record in jsonobj:
            currentrecord = []
        #Iterate through each key in the keylist and add the data to our current record list
            for key in keylist:
                currentrecord.append(record[key])
            f.writerow(currentrecord)
        #return output_file
class_input = jsonacsv(sys.argv[1],sys.argv[2])
#class_input = jsonacsv()
class_input.jsontocsv()


if __name__ == "__main__":
    pass