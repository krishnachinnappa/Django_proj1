from django.shortcuts import render
from django.http import HttpResponse
from Trains_Info.models import train_details
from Trains_Info import form
# Create your views here.

def home(Request):
    return render(Request,"Trains_Info/home.html")
def train_info(Request):
    form = form.train_form()
    return render(Request,"Trains_Info/Train_info.html",context = dict({'form_d':form}))
def report(Request):
    train_mdl_details = train_details.objects.order_by('train_num')
    train_details_dict = {'insert_train_details':train_mdl_details}

    return render(Request,"Trains_Info/report.html",context = train_details_dict)