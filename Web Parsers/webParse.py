import requests
from bs4 import BeautifulSoup
'''
result = requests.get("https://www.google.com")

#print(result.status_code)

#print(result.headers) # html <head> tags

src = result.content

soup = BeautifulSoup(src, 'html.parser') # not worry about 2nd parameter

links = soup.find_all("a")
#print(links)
#print('\n')

for link in links:
    if "About" in link.text:
        print(link) # print whole link including <a> tags and href attribute
        print(link.attrs['href']) # access just the href attribute

''' 

briefing_page = requests.get("https://www.whitehouse.gov/briefings-statements/")

briefing_contents = briefing_page.content

soup = BeautifulSoup(briefing_contents, 'html.parser')

url = []

for h2_tag in soup.find_all("h2"):  # return a list with the said parameters
    a_tag = h2_tag.find('a')    # returns a single element of said parameters
    url.append(a_tag)
    url.append(a_tag.attrs['href'])

print(url)
''' 
soup.prettify() -> prints out nicely formatted HTML

soup.b -> finds the first occurence of usage for a <b> tag (bold)

soup.p -> finds the first occuence of <p> tag

soup.find("b") -> also finds the first occurence of <b> tag

soup.find_all("b") -> returns a list of all the occurence of <b> tag, can add a [#] to find the nth 
    occurence of the tag
soup.find_all("a")[1]['id'] -> will return value of id in the 2nd occurence of <a> tag
    if want to find all attributes in the tags -> soup.attrs -> returns a dictionary of the 
    attribute of the tag ({attribute: 'key', ...})
Can change attributes value like .name below

del -> remove element or attribute from html

soup.b.name -> name of tag (we can also change name of tags to anything we want)
soup.b.name = " " -> then in the html, the <b> will be replaced by <" ">

.string -> returns text in between tags
.replace_with("string") -> replace string between tags with new string


'''

