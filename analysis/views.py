from django.shortcuts import render
import requests
from .forms import Sentiment
from django.shortcuts import redirect
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
import pickle
from keras.preprocessing.sequence import pad_sequences
import numpy as np

model = keras.models.load_model('D:/Programiranje/web/sentiment/models/tf_model')



def home(request):
    form = Sentiment()
    result='text not yet analised'
    if request.method == "POST":
        form = Sentiment(request.POST)
    if form.is_valid():
        text = form.cleaned_data.get('text')
        ######
        test = (text)
        prediction = model.predict(np.array([test]))
        pred = prediction[0][0]
        if pred<0:
            result='negative'
        else:
            result='positive'


 

    else:
        form = Sentiment()
    args = {'form':form, 'result':result}
    return render(request, 'analysis/home.html', args)