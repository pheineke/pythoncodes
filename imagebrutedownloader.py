import os
import random
import requests
import shutil

def urlgenerator():
    number0 = str(random.randint(0,9))
    number1 = str(random.randint(130,131))
    number2 = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
    
    link = "https://" + "images" + number0 + ".alphacoders.com/" + number1 + "/" + number1 + number2
    return link

file_extensions = ['.jpeg', '.jpg', '.png']
file_name = str(random.randint(0,99999999))

# Hier kannst du den Pfad angeben, wohin die Bilder gespeichert werden sollen
path = 'C:/Users/heine/OneDrive/Documents/GitRepos/pythoncodes/testbilder'

while True:
    try:
        for ext in file_extensions:
            url1 = urlgenerator()
            url = url1 + ext
            length = len(url1)
            file_name = url1[length - 7:] + ext
            res = requests.get(url, stream = True)
            res.raise_for_status()

            with open(os.path.join(path, file_name),'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ', file_name)
            break
        else:
            print('Image Couldn\'t be retrieved. Trying again...')
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}. Trying again...')
