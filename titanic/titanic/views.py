
from django.shortcuts import render
from . import fake_model
import seaborn as sns
import pandas as pd
from . import ml_predict
import matplotlib.pyplot as plt
import io
import urllib, base64


def home(request):
    return render(request,'index.html')

def result(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request,'result.html', {"prediction":prediction})

def graphs(request):
    return render(request,'graphs.html')
