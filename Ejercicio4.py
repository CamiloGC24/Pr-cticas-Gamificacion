from urllib import request
from urllib.error import URLError

def words(url):

    try:
        file = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = file.read()
        return len(content.split())

print(words('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(words('https://no-existe.txt'))