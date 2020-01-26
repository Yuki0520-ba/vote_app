from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Avg
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Band,Vote
from .forms import BandForm,VoteForm

from django.urls import reverse_lazy

# Create your views here.
class BandListView(ListView):
    model = Band

class BandDetailView(DetailView):
    model=Band

class BandCreateView(LoginRequiredMixin,CreateView):
    model=Band
    form_class=BandForm

    login_url="/login"
    success_url=reverse_lazy("band_index")

class BandUpdateView(LoginRequiredMixin,UpdateView):
    model=Band
    form_class=BandForm
    template_name="mysite/band_update.html"

    login_url="/login"
    success_url=reverse_lazy("band_index")


class BandDeleteView(LoginRequiredMixin,DeleteView):
    model=Band
    login_url="/login"
    success_url=reverse_lazy("band_index")



def index_top(request):
    return TemplateResponse(request,'band_top.html')

@login_required
def all_delete_check(request):
    return TemplateResponse(request,'band_delete_check.html')

@login_required
def all_delete(request):
    Band.objects.all().delete()  
    return TemplateResponse(request,'band_delete.html')


def band_vote(request,pk):
    get_band=Band.objects.get(id=pk)
    name=get_band.band_name

    vote=Vote()
    vote.band=get_band
    
    if request.method=='POST': 
        print('post :',request.POST)
        form=VoteForm(request.POST,instance=vote)
        if form.is_valid():
            vote.save()
            return HttpResponseRedirect(reverse('band_list'))
    else:
        vote_form=VoteForm(instance=vote)
        return TemplateResponse(request,'vote_update.html',{'form':vote_form,'band_name':name})


@login_required
def aggregate(request):
    result_list=[]
    bands=Band.objects.all()

    for band in bands:
        point=Vote.objects.filter(band=band).aggregate(Avg('count'))
        ex_dic={}
        ex_dic['name']=band.band_name
        
        if point['count__avg']!=None:
            ex_dic['point']=point['count__avg']+band.point
            result_list.append(ex_dic)

    if result_list:
        result_list.sort(key=lambda x: x['point'],reverse=True)    

    return TemplateResponse(request,'aggregate.html',{'result_list':result_list})






