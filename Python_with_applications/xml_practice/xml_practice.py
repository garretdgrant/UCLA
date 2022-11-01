import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

tree = ET.parse('plant_catalog.xml')
root = tree.getroot()

id = 1
for plant in tree.findall('PLANT'):
    plant.set('id', str(id))
    id += 1

tree.write('plant_catalog.xml')
