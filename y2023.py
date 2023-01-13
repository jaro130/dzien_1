import xml.etree.ElementTree as ET

tree = ET.parse('dane.xml')

root = tree.getroot()

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)

xmen = root.find("./genre/decade/movie/[@title='X-Men']")
xmen.attrib['year'] = '2023'
print(xmen.attrib)
tree.write('y2023.xml')