from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index2.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    
    removepunctu = request.POST.get('removepunct','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    if removepunctu == "on":
        punctuationlist = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuationlist:
                analyzed += char
        params = {'purpose':'remove punctuation' , 'analyzed_text': analyzed}
        return render(request,'analyze2.html', params)
    elif fullcaps == 'on':
        anal = ''
        for char in djtext:
            anal += char.upper()
        params = {'purpose':'changed to capital','analyzed_text': anal}
        return render(request,'analyze2.html',params)
    elif newlineremover == 'on':
        anal = ''
        for char in djtext:
            if char != '\n' and char!= '\r':
                anal += char
        params = {'purpose':'new line removed','analyzed_text': anal}
        return render(request,'analyze2.html',params)
    elif extraspaceremover == 'on':
        anal = ''
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                anal += char            
        params = {'purpose':'space removed','analyzed_text': anal}
        return render(request,'analyze2.html',params)
    elif charcount == 'on':
        anal = len(djtext)       
        params = {'purpose':'space removed','analyzed_text': anal}
        return render(request,'analyze2.html',params)
    
    else:
        return HttpResponse('errorr')


