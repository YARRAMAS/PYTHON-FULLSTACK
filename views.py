from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import EmployeeForm
import pymongo
from django.core.paginator import Paginator
from bson import ObjectId
import hashlib

client = pymongo.MongoClient('mongodb://localhost:27017/')  
db = client['emp']  
collection = db['employees']

def home(request):
    return render(request,'base/home.html')

def sha256_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        stored_email = "training@jalaacademy.com"
        stored_password_hash = sha256_hash("jobprogram") 
        
    
        entered_password_hash = sha256_hash(password)

        if email == stored_email and entered_password_hash == stored_password_hash:
            return redirect('signin')
        else:
            return HttpResponse("Invalid Credentials. Please Enter Valid Details.....")
        
    return render(request, 'base/signin.html')
    
def logout(request):
    return redirect('home')

def forgot(request):
    return render(request,'base/forgotPassword.html')


def admin(request):
    return render(request,'base/adminPage.html')

def create(request):
    return render(request,'base/Create_Employee.html')

def search(request):
    return render(request,'base/Search_Employee.html')

def cancel(request):
    return render(request,'base/signin.html')

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_data = {
                "first_name": form.cleaned_data['first_name'],
                "last_name": form.cleaned_data['last_name'],
                "email_id": form.cleaned_data['email_id'],
                "mobile_no": form.cleaned_data['mobile_no'],
                "gender": form.cleaned_data['gender'],
                "birth_date": form.cleaned_data['birth_date'].strftime('%d/%m/%Y'),
                "country": form.cleaned_data['country'],
                "city": form.cleaned_data['city'],
                "skills": form.cleaned_data['skills'],
                "address": form.cleaned_data['address']
            }

            collection.insert_one(employee_data)
            return redirect('search_employee')  
        else:
            messages.error(request, "Please correct the errors below.")
            print("Form errors:", form.errors)  
    else:
        form = EmployeeForm()
    return render(request, 'base/Create_Employee.html', {'form': form})

def search_employee(request):
    query = {}
    
    if 'mobile_no' in request.GET and request.GET['mobile_no']:
        query['mobile_no'] = {'$regex': request.GET['mobile_no'], '$options': 'i'}
    
    if 'name' in request.GET and request.GET['name']:
        query['first_name'] = {'$regex': request.GET['name'], '$options': 'i'}
    
    employee_data = list(collection.find(query))
    paginator = Paginator(employee_data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for employee in employee_data:
        employee['id'] = str(employee['_id'])
    return render(request, 'base/search_employee.html', {'page_obj': page_obj})

def edit_employee(request, employee_id):
    employee = collection.find_one({'_id': ObjectId(employee_id)})

    if request.method == 'POST':
        updated_data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email_id': request.POST.get('email_id'),
            'mobile_no': request.POST.get('mobile_no'),
            'gender': request.POST.get('gender'),
            'birth_date': request.POST.get('birth_date'),
            'country': request.POST.get('country'),
            'city': request.POST.get('city'),
            'skills': request.POST.get('skills'),
            
            'address': request.POST.get('address'),
        }
        
        collection.update_one({'_id': ObjectId(employee_id)}, {'$set': updated_data})
        return redirect('search_employee')

    context = {'employee': employee}
    return render(request, 'base/edit_employee.html', context)

def delete_employee(request, employee_id):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['emp']
    collection = db['employees']

    collection.delete_one({'_id': ObjectId(employee_id)})
    return redirect('search_employee')

def tabs(request):
    return render(request,'base/multiple_tabs.html')

def menu(request):
    return render(request,'base/menu.html')

def auto(request):
    return render(request,'base/auto.html')

def collapsible(request):
    return render(request,'base/collapsible.html')

def images(request):
    return render(request,'base/images.html')

def slider(request):
    return render(request,'base/slider.html')

def tooltips(request):
    return render(request,'base/tooltips.html')

def iframes(request):
    return render(request,'base/iframes.html')

def popups(request):
    return render(request,'base/popups.html')

def links(request):
    return render(request,'base/links.html')

def cssprops(request):
    return render(request,'base/cssprops.html')
