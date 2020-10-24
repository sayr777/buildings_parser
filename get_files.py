

import requests
import zipfile
import os

for element in range (1,200):

    url = 'https://www.reformagkh.ru/opendata/export/' + str(element)

    myfile = requests.get(url)

    open('./files/101.zip', 'wb').write(myfile.content)


    with zipfile.ZipFile("./files/101.zip","r") as zip_ref:
        zip_ref.extractall("./files")

    os.remove("./files/101.zip")