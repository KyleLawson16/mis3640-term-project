import cv2
import numpy as np
import urllib.request

url_list = []

for i in range(1, 802):
    try:
        url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+ \
            '{:03d}'.format(i) +'.png'
        url_list.append(url)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        binary_str = response.read()
        byte_array = bytearray(binary_str)
        numpy_array = np.asarray(byte_array, dtype= "uint8")
        image = cv2.imdecode(numpy_array, cv2.IMREAD_UNCHANGED)
        cv2.imwrite("images/" + '{:03d}'.format(i) +'.png', image)
        print("Saved" + '{:03d}'.format(i) +'.png')
    except Exception as e:
        print(str(e))

print("Done")


with open('image_urls.txt', 'w') as f:
    for item in url_list:
        f.write("%s\n" % item)
