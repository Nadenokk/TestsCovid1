import os
import shutil

from bs4 import BeautifulSoup

dir_name = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\med\\kuba"
dir_l2 = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\med\\ladya2021"
names = os.listdir(dir_name)
count = len(names)
print('Всего протоколов ', count)
for name in names:
    with open(dir_name + "\\"+name,  encoding="utf8") as fd:
        print(name)
        #fd = open('C:\\Users\\user\\PycharmProjects\\TestsCovid1\\med\\kuba\\4001270928519.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        #print(soup)
        quotes = soup.find_all('mb:testingdate')

        for quote in quotes:
            result=quote.text
            year = result.split('.')[-1]
            print(year)
            if year=="2021": shutil.copy(dir_name + "\\" + name, dir_l2 + "\\" + name)
        count = count - 1
        print('Осталось загрузить ', count)





