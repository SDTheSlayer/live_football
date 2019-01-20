from django.shortcuts import get_object_or_404, render
from django.db import models
from .models import scores
import bs4 as bs
from selenium import webdriver



def score_list(request):

    url = 'http://m.livescore.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    sauce = browser.page_source
    browser.quit()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    # for i in range(len(soup.select('#soccer_scores')[0].select('.sep'))):
    #     if soup.select('#soccer_scores')[0].select('.sep')[i].find("span", {'class' : "lsName"} ):
    #         print(soup.select('#soccer_scores')[0].select('.sep')[i].find("span", {'class' : "lsName"} ).getText())

    for i in range(len(soup.select('#soccer_scores')[0].select('.ete'))):
        for j in range(len(soup.select('#soccer_scores')[0].select('.ete')[i].select('li'))):
            score = scores()
            score.team1 = soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsTNames')[0].select('dd')[0].getText()
            score.score1 = soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsScore')[0].select('dd')[0].getText()
            score.team2 = soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsTNames')[0].select('dd')[1].getText()
            score.score2 = soup.select('#soccer_scores')[0].select('.ete')[i].select('li')[j].select('.lsScore')[0].select('dd')[1].getText()
            score.save()

    Scores = scores.objects.all()
    return render(request, 'scores/scores.html', {'scores': Scores})