
from django.shortcuts import render
from . import conversion_model
from . import ml_predict



def home(request):
    return render(request,'index.html')

def result(request):
    pclass = int(request.GET["pclass"])
    sex_str = request.GET["sex"]
    sex = int(conversion_model.sex(sex_str))

    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = int(request.GET["fare"])
    embarked_str = request.GET["embarked"]
    embarked =int(conversion_model.embarked(embarked_str))

    title_str = request.GET["title"]
    title = int(conversion_model.title(title_str))

    prediction = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request,'result.html', {"prediction":prediction})

def graphs(request):
    return render(request,'graphs.html')
