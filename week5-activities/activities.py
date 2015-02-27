import os
import numpy as np
from xml.etree import ElementTree
import glob

fname = 'weather-cwop3-2014-12-26T13:00:00Z.xml'
l = []

for filename in os.listdir ('./weather'):
   if glob.fnmatch.fnmatch(filename, '*.xml'):
      doc = ElementTree.parse(path+filename)
      for report in doc.getroot().iter('{http://weather.milowski.com/V/APRS/}report'):
# If the attribute isn't available, we'll get a dictionary key exception
# so we check for its existence
         if "temperature" in report.attrib:
            l.append(int(report.attrib["temperature"]))

print np.mean(l)


import json
fname = 'weather-cwop3-2014-12-26T13:00:00Z.json'
lj = []
for filename in os.listdir(path):
   if glob.fnmatch.fnmatch(filename,'*.json'):
      json_data = open(path+fname).read()
      data = json.loads(json_data)
      for feature in data['features']:
         cor = feature['geometry']['coordinates']
         if cor[0] > -120 and cor[0] < 40 and cor[1] > -120 and cor[1] < 35:
            tmp = feature['properties']['temperature']
            if tmp.isdigit():
               lj.append(int(feature['properties']['temperature']))

print np.mean(lj)
