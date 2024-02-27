from django.shortcuts import redirect, render
import requests
from django.utils import timezone
from .forms import ContactForm
from .models import Email
from django.urls import reverse_lazy
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, 'views/index.html')

def about(request):
    return render(request, 'views/aboutMe.html')

def blog(request):
    return render(request, 'views/blogMainPage.html')

def contact(request):
    return render(request, 'views/contactPage.html')

def policy(request):
    return render(request, 'views/privacyPolicy.html')

def terms(request):
    return render(request, 'views/termsAndconditions.html')

def dfgs(request):
    return render(request, 'views/dialogFlowToGoogleSheets.html')

def search(request):
    if request.POST['CityName']:
        url = "https://api.openweathermap.org/data/2.5/weather?q="+ request.POST['CityName']+"&appid=" + settings.API_KEY +"&units=metric"
        response = requests.get(url)
        weatherdata = response.json()
        if weatherdata['cod'] == 200:
            wid = str(weatherdata['weather'][0]['id'])
            renderData = {'temperature': weatherdata['main']['temp'], 'city': request.POST['CityName'] , 'des': weatherdata['weather'][0]['description'], 'icon': weatherdata['weather'][0]['icon']}
            if wid[0] == '3' or wid[0] == '5':
                return render(request, 'views/rain.html', renderData)
            elif wid[0] == '2':
                return render(request, 'views/thunder.html', renderData)
            elif wid == '801' or wid == '802' or wid == '803' or wid == '804':
                return render(request, 'views/clouds.html', renderData)
            elif wid == '600' or wid == '601' or wid == '602':
                return render(request, 'views/snow.html', renderData)
            elif wid[0] == '6':
                return render(request, 'views/snowrain.html', renderData)
            elif wid == '701' or wid == '741':
                return render(request, 'views/mist.html', renderData)
            elif wid == '771' or wid == '781':
                return render(request, 'views/tornado.html', renderData)
            elif wid == '711' or wid == '721' or wid == '731' or wid == '751' or wid == '761':
                return render(request, 'views/dust.html', renderData)
            elif wid == '800' and weatherdata['weather'][0]['icon'] == '01d':
                return render(request, 'views/clearskyday.html', renderData)
            elif wid == '800' and weatherdata['weather'][0]['icon'] == "01n":
                return render(request, 'views/clearskynight.html', renderData)
            else:
                return render(request, 'views/nopair.html', renderData)
        else:
            return render(request, 'views/404.html')
    else:
        return render(request, 'views/404.html')



def contactMe(request):
    dateset = Email(pub_date = timezone.now())
    form = ContactForm(request.POST, instance = dateset)
    if form.is_valid():
        form.save()
        u = reverse_lazy('weather:contactSuccess')
        return redirect(u)
    else:
        u = reverse_lazy('weather:contactError')
        return redirect(u)

def contactSuccess(request):
    return render(request, 'views/success.html')

def contactError(request):
    return render(request, 'views/error.html')
