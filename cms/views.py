from django.shortcuts import render
from . import views
from .models import Staff
# Create your views here.
def index (request):
    staff_members=Staff.objects.all
    return render(request,"index.html",{'staff_members':staff_members})