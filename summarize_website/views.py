from django.shortcuts import render
from transformers import pipeline
from .forms import textForm
from .models import summarize_data
from fpdf import FPDF

def summarize(text):
    summarizer = pipeline("summarization")
    return summarizer(text, max_length=100, min_length=10, do_sample=False)

def save_summarize_text_textFile(summarize_text):
        with open('summarized_text.txt', 'w') as file:
                file.write(summarize_text)
        return file

def convert_summarize_text_pdf(file):
    pdf = FPDF()
    pdf.add_page()
    for text in file:
        if len(text) <= 20:
            pdf.set_font("Arial","B",size=18) 
            pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            pdf.set_font("Arial",size=15) 
            pdf.multi_cell(w=0,h=10,txt=text,align="L")
    pdf.output("output.pdf")
    print("Successfully converted!")

 
def index(request):
    summarize_text=None
    if request.method=='POST':
        form=textForm(request.POST)
        if form.is_valid():
            form.save()
            text=form.cleaned_data['text']
            summarize_text=summarize(text)
            file=save_summarize_text_textFile(summarize_text)
            convert_summarize_text_pdf(file)            
    else:
        form=textForm()
    return render(request,'index.html',{'form':form,'summarize':summarize_text})



