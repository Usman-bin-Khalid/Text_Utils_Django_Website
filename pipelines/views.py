from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'name' : 'Usman' , 'place' : 'Pakistan'}
    return render(request, 'index.html', params)

# def analyze(request):
#     # Get the text from the user
#     djtext = request.GET.get('text', 'default')
#     analyzed = djtext
#     # Check the checkbox values
#     removepunc = request.GET.get('removepunc', 'off')
#     fullcaps = request.GET.get('fullcaps', 'off')
#     newLineRemover = request.GET.get('newlineremover', 'off')
#     extraSpaceRemover = request.GET.get('extraspaceremover', 'off')
#     # Check which checkbox is on
#     if removepunc == 'on':
#         punctuations = '''.,:;?!-–—'"‘’()[]{}…/\@#*&^_=+<>|~`%'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
        
 
#         params = {'purpose' : 'Remove Punctuation', 'analyzed_text' : analyzed} 
#         return render(request, 'analyze.html' , params) 
#     elif(fullcaps == "on"):
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params = {'purpose' : 'Change to Uppercase', 'analyzed_text' : analyzed}
#         return render(request, 'analyze.html', params )     
#     elif(newLineRemover == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char !='\n':
#                 analyzed = analyzed + char
#         params = {'purpose' : 'Remove New Lines', 'analyzed_text' : analyzed}  
#         return render(request, 'analyze.html', params) 
#     elif(extraSpaceRemover == "on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not(djtext[index] ==' ' and djtext[index + 1] == ' '):
#                 analyzed = analyzed + char
#             else:
#                 analyzed = analyzed + char
#         params = {'purpose' : 'Remove Extra Space', 'analyzed_text' : analyzed}
#         return render(request, 'analyze.html', params)        
   

#     else:
#         return HttpResponse('Error')


def analyze(request):
    # Get the text from the user
    djtext = request.POST.get('text', 'default')  # ✅ use POST

    # Check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newLineRemover = request.POST.get('newlineremover', 'off')
    extraSpaceRemover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''.,:;?!-–—'"‘’()[]{}…/\@#*&^_=+<>|~`%'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newLineRemover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if extraSpaceRemover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and index + 1 < len(djtext) and djtext[index + 1] == ' '):
                analyzed += char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    if(removepunc !='on' and fullcaps != 'on' and newLineRemove != 'on' and extraSpaceRemover !='on'):
        return HttpResponse('Please select the operation you want to perform')   

    # else:
    #     return HttpResponse('Error')
    return render(request, 'analyze.html', params)


def ex(request):
    return HttpResponse('''<a href='https://youtu.be/lcpqpxVowU0?si=WgvjSprdoYJyoeji'>Code With harry</a><br><a href='https://chatgpt.com/g/g-cZPwvslfA-flutter/c/688d0671-3030-800d-8927-35c6158d00b9'>Chat GPT</a>''')


    


def capFirst(request):
    return HttpResponse("Capitalize First")

def newLineRemove(request):
    return HttpResponse("Remove New Lines")
def spaceRemover(request):
    return HttpResponse("Remove Extra Spaces")



