import sys
import json
import os
import re

# we are using pprint for making the output more readable.

#read file
f2 = open ('EPALL20910.csv', 'w')

with open('EPALL20910.json', 'r') as jsonfile:
#with open('epg_test.json', 'r') as jsonfile:
  jsonobj = json.load(jsonfile)

for imdata in jsonobj:
    for fvCEp in imdata.values():
                               policy_groupe = "neverSHOW"
                               node_id = "neverSHOW"
                               ip = "neverSHOW"
                               mac = "neverSHOW"
                               dn = fvCEp['attributes']['dn']   
                               mac = fvCEp['attributes']['mac']
                               ip = fvCEp['attributes']['ip']
                               if 'children' in fvCEp.keys(): # Children  est le second niveau de l'extract
                                               for fvRsCEpToPathEp in fvCEp['children']:
                                                               if 'fvRsCEpToPathEp' in fvRsCEpToPathEp.keys()  :
                                                                               tDn = fvRsCEpToPathEp['fvRsCEpToPathEp']['attributes']['tDn']
                                                                               node_id = re.findall(r"[0-9]+-?[0-9]+",tDn)
                                                                               node_id = node_id[0]
                                                                               policy_groupe = re.findall(r"\[\w+\S+]",tDn)
                                                                               policy_groupe = policy_groupe[0].strip('[').strip(']')
                               else :
                                               policy_groupe = "NA"
                                               node_id = "NA"
                               #tDn = fvCEp['children'][0]['fvRsCEpToPathEp']['attributes']['tDn']
                               epg_name = re.findall(r"epg-\w+[1-9]+",dn)
                               f2.write (ip + ';' + mac + ';' + node_id + ';' + policy_groupe + '\n')


 
##print (dir(jsonobj)) 
#for obj in jsonobj:
#  #print (obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'])
#  i= obj["fvCEp"]
#  #print (type(i))
#  #print (i.keys())
#  if 'children' in i:
#    ii = i['children']
#    #print (type(ii))
#    for i_sub in ii:
#      if 'fvRsCEpToPathEp' in i_sub:
#        ii_sub=i_sub['fvRsCEpToPathEp']['attributes']
#        keylist = []
#        #print (obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'],ii_sub['tDn'])
#        keylist = [obj["fvCEp"]["attributes"]['dn'],obj["fvCEp"]["attributes"]['mac'],obj["fvCEp"]["attributes"]['ip'],ii_sub['tDn']]
#        keylist
#
#
#
#  
#
#    
#
#    
#  #for child_atri in epg_child:
#  #  gran_child= (child_atri['fvRsCEpToPathEp']['attributes']['tDn'])
#  #  print (gran_child)