import requests
import urllib.request
import glob
from PIL import Image
import time

#pip3 install pillow

url = 'https://mangadex.org/api/chapter/819831'

resp = requests.get(url=url)
data = resp.json()

imagelist = []

for i in data['page_array']:
    print(data['server_fallback'] + data['hash'] + '/' + i)
    url = data['server_fallback'] + data['hash'] + '/' + i
    file_name = i
    urllib.request.urlretrieve(url, file_name)
    imagelist.append(i)
    time.sleep(1.5)

print(imagelist)
converted_img = []
for image in imagelist:
    curr_img = Image.open(image)
    curr_img = curr_img.convert('RGB')
    converted_img.append(curr_img)
converted_img[0].save('SAVE.pdf', save_all=True, append_images=converted_img[1:])

