import json, urllib.request, urllib.error, urllib.parse

sum=0

with urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_744844.json") as url:
    data = json.loads(url.read().decode())
    print(data)
print("\n\n\n Length of data",len(data))
print("\n\n\n___________________________________________\n\n\n")

for item in data['comments']:
    sum = sum + int(item['count'])

print("SUM >>", sum)


