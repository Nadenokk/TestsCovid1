import os
import io

from lxml import etree
projectPath="C:\\Users\\user\\PycharmProjects\\TestsCovid1\\med\\kuba"
with open(os.path.join(projectPath, '4001270928519.xml'), "r",
          encoding='UTF-8') as f:
    src = f.read()

parser = etree.XMLParser(remove_blank_text=True)
projectET = etree.parse(io.StringIO(src), parser)

#XML="C:\\Users\\user\\PycharmProjects\\TestsCovid1\\med\\kuba\\4001270928519.xml"
#xml = etree.XML(XML)  # type:
macStyle = projectET.find('testingDate')  # type: #etree._Element
print(macStyle.tag,macStyle.attrib)

for tag in soup.findAll("testingDate"):
    print(tag)
    print(tag["testingDate"])
    print(tag.text)
fd.close()