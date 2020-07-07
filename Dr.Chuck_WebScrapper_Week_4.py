from bs4 import BeautifulSoup
import urllib.request

url = 'http://py4e-data.dr-chuck.net/known_by_Kane.html'
count = 7
position = 18
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # input('Enter the URL: ')
# count = 4 # int(input('Enter the count: '))
# position = 3 # int(input('Enter the position: '))
for i in range(count + 1):
    print('Getting:', url)
    with urllib.request.urlopen(url) as webFile:
        soup = BeautifulSoup(webFile.read(), 'html.parser')

    url = soup.find_all('a')[position - 1].get('href')

print(soup.h1.string.split()[2])
       


