import xml.dom.minidom
from xml.etree import ElementTree as ET
import numpy as np
import csv
import os

image_subdirectory = '/home/drl/nxr/vehicle_data/Annotation/TSD-FVLM-00140'
FrameNumber = '0' 

for i in range(85):
	if int(FrameNumber) < 10 :
		annotation_subdirectory = os.path.join('TSD-FVLM-00140-0000' + FrameNumber)
	else:
		annotation_subdirectory = os.path.join('TSD-FVLM-00140-000' + FrameNumber)

	Annotation_dir = os.path.join(image_subdirectory, annotation_subdirectory + '.xml')
	# print(annotation_subdirectory)
	# print(Annotation_dir)
	# DOMTree = xml.dom.minidom.parse(Annotation_dir)
	Tree = ET.parse(Annotation_dir)
	root = Tree.getroot()
	childs = root.getchildren()
    # for elem in Tree.iter(tag ='object'):
	Object_Number = '0'
	for elem in Tree.iter(tag = 'object'):
		Object_Number = int(Object_Number) + 1
	l = Object_Number + 7

	for i in range(7, l):		
		if root[i][0].text == '1':
			print(root[i][4][3].text)
	for i in range(7, l):
		if root[i][0].text == '2':
			print(root[i][4][3].text)
	for i in range(7, l):
		if root[i][0].text == '3':
			print(root[i][4][3].text)
	for i in range(7, l):
		if root[i][0].text == '4':
			print(root[i][4][3].text)
	FrameNumber = str(int(FrameNumber) + 1)
