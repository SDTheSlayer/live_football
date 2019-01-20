import bs4 as bs
from selenium import webdriver

url = 'http://m.livescore.com/'
browser = webdriver.Chrome()
browser.get(url)
sauce = browser.page_source
browser.quit()
soup = bs.BeautifulSoup(sauce,'lxml')
 # for i in range(len(soup.select('#soccer_scores')[0].select('.sep'))):
 #     if soup.select('#soccer_scores')[0].select('.sep')[i].find("span", {'class' : "lsName"} ):
 #         print(soup.select('#soccer_scores')[0].select('.sep')[i].find("span", {'class' : "lsName"} ).getText())

for i in range(len(soup.select('#soccer_scores')[0].select('.ete'))):
    for j in range(len(soup.select('#soccer_scores')[0].select('.ete')[i].select('li'))):
        print(soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsTNames')[0].select('dd')[0].getText())
        print(soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsScore')[0].select('dd')[0].getText())
        print(soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsTNames')[0].select('dd')[1].getText())
        print(soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsScore')[0].select('dd')[1].getText())