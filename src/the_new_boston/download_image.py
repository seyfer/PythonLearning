import random
import urllib.request

def download(url):
    name = random.randrange(1, 1000)
    fullName = str(name) + ".gif"
    urllib.request.urlretrieve(url, fullName)

download('https://cdn.37img.com/global/c4559d4c45cad9726a87e16a09fbb6b10010/original.c4559d4c45cad9726a87e16a09fbb6b10010.gif?r=3');
