import datetime as dt
from django.shortcuts import render,redirect
from .models import Article
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect
# Create your views here.


def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()

    return render(request, 'all-news/todays-news.html', {"date": date,"news":news,"letterForm":form})

def past_days_news(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)
    news = Article.day_new(date)
    return render(request, 'all-news/past-news.html', {"date": date,"news":news})
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

  
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})  

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})