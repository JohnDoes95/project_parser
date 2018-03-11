from django.shortcuts import render
from scrapy_project.spiders.stackoverflow import StackoverflowSpider
from scrapy_project.spiders.starting_crawler import crawl
from django.http import HttpResponseRedirect,HttpResponse
from questions.models import Questions,Yandex_metricks
from questions.forms import PostForm



result = {}
resultkey = {}
resultdesc = {}
resultlink = []
resulth1 = {}
resulttext = {}
resultgoogl={}

def list_view(request):
    items = Questions.objects.all()

    return render(request, 'questions/indes.html', {
        """'title': ScrapyProjectPipeline.result,
        'keyword':ScrapyProjectPipeline.resultkey,
        'description':ScrapyProjectPipeline.resultdesc,
        'link':ScrapyProjectPipeline.resultlink,
        'h1':ScrapyProjectPipeline.resulth1,
        'text':ScrapyProjectPipeline.resulttext,
        'resultgoogl':ScrapyProjectPipeline.resultgoogl,
        'resultyandex':ScrapyProjectPipeline.resultyandex
    """
        'title': result,
        'description': resultdesc,
        'resultgoogl':resultgoogl,

    })

def contacts_view(request):
    return render(request, 'questions/contact.html', {

    })

def about_view(request):
    return render(request, 'questions/about.html', {

    })
def result_ruk(request):
    return render(request,'questions/result_ruk.html',{

    })

def result_ruk_seo(request):
    return render(request,'questions/result_ruk_seo.html',{
        'title': result,
        'keyword': resultkey,
        'description': resultdesc,
        'link': resultlink,
        'h1': resulth1,
        'text': resulttext,
        'resultgoogl': resultgoogl,
        #'resultyandex': resultyandex

    })

def result_ruk_index(request):
    return render(request,'questions/result_ruk_index.html',{

    })
def exportdate(request):
    return render(request,'questions/exportdate.html',{

    })
def start_proccess(request):
       pass

        # os.environ.setdefault("SCRAPY_SETTINGS_MODULE", "whereyourscrapysettingsare")

def result_view(request):
    test = Yandex_metricks.objects.all()

    return render(request, 'questions/result.html', {
        'title': result,
        'keyword': resultkey,
        'description': resultdesc,
        'link': resultlink,
        'h1': resulth1,
        'text': resulttext,
        'resultgoogl': resultgoogl,
        #'resultyandex': test
    })


def send_form(request):
    if request.method == 'POST':
        url = request.POST['url']
        s=StackoverflowSpider()
        crawl()

        return HttpResponseRedirect('/result/')

    else:
        form = PostForm()
        return render(request, 'questions/form.html', {
            'form': form
        })

    # Create your views here.
