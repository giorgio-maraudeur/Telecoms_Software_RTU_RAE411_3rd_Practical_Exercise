from django.shortcuts import render
from django.template.loader import get_template

# render() is a packaged function
# the 1st parameter is the request and the 2nd is the page

def Hello_index2(request):
    return render(request,'templates/ourapp2/https___ti.rtu.lv_.html')