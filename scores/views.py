from django.shortcuts import get_object_or_404, render
from django.db import models
from background_task import background
from .models import scores
import bs4 as bs
from selenium import webdriver

@background(schedule = 1)
def get_scores():
    print("Check")
    all = scores.objects.all()
    url = 'http://m.livescore.com/'
    browser = webdriver.Chrome()
    browser.get(url)
    sauce = browser.page_source
    browser.quit()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    ete = soup.select('#soccer_scores')[0].select('.ete')
    for i in range(len(ete)):
        li = ete[i].select('li')
        for j in range(len(li)):
            score = scores()
            score.time = li[j].select('.lsTime')[0].select('dd')[0].getText()
            name = li[j].select('.lsTNames')[0].select('dd')
            Sc = li[j].select('.lsScore')[0].select('dd')
            score.team1 = name[0].getText()
            score.score1 = Sc[0].getText()
            score.team2 = name[1].getText()
            score.score2 = Sc[1].getText()
            score.save()
    for score in all:
        score.delete()


def score_list(request):
    current = scores.objects.exclude(time__contains=':').exclude(time='FT').order_by('time')
    finished = scores.objects.filter(time='FT')
    upcoming = scores.objects.filter(time__contains=':').order_by('time')
    return render(request, 'scores/scores.html', {'Current': current, 'Finished': finished, 'Upcoming': upcoming})