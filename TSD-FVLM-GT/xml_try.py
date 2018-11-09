
# from  xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np
import csv

# load .xml by using parse
DOMTree = xml.dom.minidom.parse('TSD-FVLM-00140-GT.xml')
root = DOMTree.documentElement

#  get Tag = 'locations' from .xml
locations = root.getElementsByTagName('Location')

#  locations form: <Location>1.8622216682356125e+01 3.0736232912503629e+00</Location>
aa = locations[0].firstChild.data

Dy = []
Dx = []

for l in range(240):  # 240 is the number of locations in .xml, should be greater 
	dy_dx = locations[l].firstChild.data # load each value of locations
	dy = dy_dx.split( )[0] 
	# print(dy)
	dx = dy_dx.split( )[1]
	print(dx)
	# Dy.append(dy)
	# Dx.append(dx)


# Dy_array = np.array(Dy).reshape((72,1))
# print(Dy_array)
# Dx_array = np.array(Dx).reshape((72,1))
# print(Dx_array)

# Dy_array.to_csv('/home/drl/nxr/vehicle_data/TSD-FVLM-GT/Dy_output.csv')
# resultsDy = records.RecordCollection(iter(Dy_array))
# with open('demo.xlsx','wb') as f:
# 	f.write(resultsDy.export('xlsx'))
