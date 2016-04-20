##url = 'https://www.google.com/'
##instan = webdriver.Firefox()
###instan.set_window_size(1280, 1024)
##instan.get(url)
##
##search = instan.find_element_by_name('q')
##search.send_keys("saudi arabia data portal bulk download")
##search.send_keys(Keys.RETURN)
##
##
##
##
##
##htmlfile = requests.get(instan.current_url)
##htmlfile.raise_for_status()
##strh = htmlfile.text
##soup = BeautifulSoup(strh, 'lxml')
##print(instan.current_url)
##for p in soup.find_all('a'):
##    print(p)
##links = []

##for link in soup.find_all('a', href = True):
##    if link['href'] == '' or link['href'].startswith('#'):
##        continue
##        
##    thislink = { 'url': link['href'],'title' :  link.string }
##    linkl = thislink['url'].strip()
##    if (linkl not in links): 
##        links.append(linkl)

##print(soup.getText())

##def googlesearch():
##    br = mechanize.Browser()
##    br.set_handle_robots(False)
##    br.set_handle_equiv(False)
##    br.addheaders = [('User-agent', 'Mozilla/5.0')] 
##    br.open('http://www.google.com/')   
##
##    # do the query
##    br.select_form(name='f')   
##    br.form['q'] = 'scrapy' # query
##    data = br.submit()
##    soup = BeautifulSoup(data.read())
##    for a in soup.find_all('a', href=True):
##        print( "Found the URL:", a['href'])
##googlesearch()
#---------------------python 2.7 mechanize code---------------------------
##import mechanize
##import re
##from bs4 import BeautifulSoup
##br = mechanize.Browser()
##br.addheaders = [('User-agent','Mozilla/5.0')]
##br.set_handle_robots(False)
##html1= br.open('https://www.google.com/search?q=saudi+arabia+bulk+download')
##html2=html1.read().lower()
###html3 = unicode(html2,errors = 'ignore')
##soup = BeautifulSoup(html2, "lxml")
##links = []
##linkname =[]
##for link in soup.find_all('a', href=True):
##if link['href'] == '' or link['href'].startswith('#'):
##continue
##thisLink = {
##'url': link['href'],
##'title': link.string
##}
##linkname.append(thisLink['title'])
##link1= (thisLink['url'].strip())
##if (link1 not in links) and ('bulkdownload' in link1) and ('/url?q=http:' in link1) and ('google' not in link1):
##links.append(link1)
##
##link2 = links[0].split('&')[0]
##link3 = link2.split('q=')[1]
