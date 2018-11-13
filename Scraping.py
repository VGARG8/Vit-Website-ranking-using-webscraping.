from rank import calculate_rank
from pprint import pprint
from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
 
try:
 
    html = urlopen("http://www.vit.ac.in/")
    html1=urlopen("http://www.vit.ac.in/ap")
    html2=urlopen("https://peopleorbit.vit.ac.in/" )
    html3=urlopen("http://vitbhopal.ac.in/")
    html4=urlopen("http://www.vitaa.org/")
    html5=urlopen("https://vtopbeta.vit.ac.in/vtop/")
    html6=urlopen("http://info.vit.ac.in/guesthouse")
    html7=urlopen("https://vtop9.vit.ac.in/selfcare/")
    html8=urlopen("http://chennai.vit.ac.in/")
    html9=urlopen("http://careers.vit.ac.in/")
 
except HTTPError as e:
 
    print(e)
 
except URLError:
 
    print("Server down or incorrect domain")

else:
    Links={}
    l=set()
    m=set()
    n=set()
    o=set()
    p=set()
    q=set()
    r=set()
    s=set()
    t=set()
    u=set()
    z={"https://peopleorbit.vit.ac.in/","http://careers.vit.ac.in/","http://chennai.vit.ac.in/","http://www.vit.ac.in/","http://www.vit.ac.in/ap",
       "http://vitbhopal.ac.in/","http://www.vitaa.org/","http://info.vit.ac.in/guesthouse","https://vtopbeta.vit.ac.in/vtop/","https://vtop9.vit.ac.in/selfcare/"}
    res = BeautifulSoup(html.read(),"html5lib")
    res1 = BeautifulSoup(html1.read(),"html5lib")
    res2 = BeautifulSoup(html2.read(),"html5lib")
    res3 = BeautifulSoup(html3.read(),"html5lib")
    res4 = BeautifulSoup(html4.read(),"html5lib")
    res5 = BeautifulSoup(html5.read(),"html5lib")
    res6 = BeautifulSoup(html6.read(),"html5lib")
    res7 = BeautifulSoup(html7.read(),"html5lib")
    res8 = BeautifulSoup(html8.read(),"html5lib")
    res9 = BeautifulSoup(html9.read(),"html5lib")
    
    
    for link in res.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            if(link.attrs['href']!="" or link.attrs['href']!="#" ):
                l.add(link.attrs['href'])
    
    l=l-(l-z)
    #print(l)
    for link in res1.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            m.add(link.attrs['href'])
    m=m-(m-z)
    #print(m)
    for link in res2.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            n.add(link.attrs['href'])
    n=n-(n-z)
    for link in res3.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            o.add(link.attrs['href'])
    o=o-(o-z)
    for link in res4.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            p.add(link.attrs['href'])
    p=p-(p-z)
    for link in res5.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            q.add(link.attrs['href'])
    q=q-(q-z)
    for link in res6.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            r.add(link.attrs['href'])
    r=r-(r-z)
    for link in res7.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            s.add(link.attrs['href'])
    s=s-(s-z)
    for link in res8.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            t.add(link.attrs['href'])
    t=t-(t-z)
    for link in res9.find_all('a'):
        if link.has_attr('href'):
            #print(link.attrs['href'])
            u.add(link.attrs['href'])
    u=u-(u-z)
    #print(u)
Links["http://www.vit.ac.in/"]=l
Links["http://www.vit.ac.in/ap"]=m
Links["https://peopleorbit.vit.ac.in/" ]=n
Links["http://vitbhopal.ac.in/"]=o
Links["http://www.vitaa.org/"]=p
Links["https://vtopbeta.vit.ac.in/vtop/"]=q
Links["http://info.vit.ac.in/guesthouse"]=r
Links["https://vtop9.vit.ac.in/selfcare/"]=s
Links["http://chennai.vit.ac.in/"]=t
Links["http://careers.vit.ac.in/"]=u
#print(Links)
print(l,'\n',m,'\n',n,'\n',o,'\n',p,'\n',q,'\n',r,'\n',s,'\n',t,'\n',u,'\n')
links = {
    'webpage-1': {'webpage-2', 'webpage-4', 'webpage-5', 'webpage-6', 'webpage-8', 'webpage-9', 'webpage-10'},
    'webpage-2': {'webpage-5', 'webpage-6'},
    'webpage-3': {'webpage-10'},
    'webpage-4': {'webpage-9'},
    'webpage-5': {'webpage-2', 'webpage-4'},
    'webpage-6': set(), # dangling page
    'webpage-7': {'webpage-1', 'webpage-3', 'webpage-4'},
    'webpage-8': {'webpage-1'},
    'webpage-9': {'webpage-1', 'webpage-2', 'webpage-3', 'webpage-8', 'webpage-10'},
    'webpage-10': {'webpage-2', 'webpage-3', 'webpage-8', 'webpage-9'},
}

pprint(calculate_rank(Links)[:10])
