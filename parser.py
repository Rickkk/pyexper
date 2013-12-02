#задача - получить все ссылки со страницы
import urllib.request
import webbrowser
from bs4 import BeautifulSoup
root='http://mds.altervision.ru/mds/Robert_Shekley'
out=''
html_page= urllib.request.urlopen(root)
#f = open("c:\output.txt", "w")
#print(f.read())
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	#if "Shakley" in link.get('href'):
	if str(link.get('href')).find("Shekley")!=-1:
		print(root+str(link.get('href')))
		webbrowser.open(root+str(link.get('href')),new=2)
		out=out+root+str(link.get('href'))

with open("c:\\Python33\\Shekley.txt","w") as my_file:
    my_file.write(out)
    my_file.close()