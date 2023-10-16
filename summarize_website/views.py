from django.shortcuts import render
from transformers import pipeline
from .forms import textForm

def summarize(text):
    summarizer = pipeline("summarization")
    return summarizer(text, max_length=100, min_length=10, do_sample=False)

     
def index(request):
    summarize_data=None
    if request.method=='POST':
        form=textForm(request.POST)
        if form.is_valid():
            form.save()
            text=form.cleaned_data['text']
            summarize_data=summarize(text)
    else:
        form=textForm()
    return render(request,'index.html',{'form':form,'summarize':summarize_data})