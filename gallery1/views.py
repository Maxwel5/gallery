# from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Gallery Shop')

def create_album(request):
    html = f'''
        <html>
            <body>
                <h1> TFTFTF </h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
