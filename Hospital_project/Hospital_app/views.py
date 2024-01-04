from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    show_drug = drug.objects.all()
    context  = {"drug_data" : show_drug}
    return render(request,'drug_data.html',context)

def add_drug(request):
    context = {"drug_type" : d_type.objects.all()}
    if request.method == "POST":
        table = drug()
        table.drug_name = request.POST['drug_name']
        table.drug_type = d_type.objects.get(type_id = request.POST['drug_type'])
        table.drug_qty = request.POST['drug_qty']
        table.drug_exp = request.POST['drug_expired']
        table.save()
        return redirect('/manage_drug')
    return render(request,'add_drug.html',context)


def add_type(request):
    if request.method == "POST":
        table = d_type()
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'add_type.html')

def manage_drug(request):
    show_drug = drug.objects.all()
    context  = {"drug" : show_drug}
    return render(request,'edit_drug.html',context)

def manage_type(request):
    show_type = d_type.objects.all() 
    context  = {"type" : show_type} 
    return render(request,'manage_type.html',context) 




def delete_drug(request,pk):
    table = drug.objects.get(drug_id=pk)
    table.delete()
    return redirect('/manage_drug')

def delete_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    table.delete()
    return redirect('/manage_type')

@login_required(login_url="/login")
def edit_drug(request,pk):
    table = drug.objects.get(drug_id=pk)
    table2 = d_type.objects.all()
    context = {"drug_data" : table , "drug_type" : table2}
    if request.method == "POST":
        table.drug_name = request.POST['drug_name']
        table.drug_type = d_type.objects.get(type_id = request.POST['drug_type'])
        table.drug_qty = request.POST['drug_qty']
        table.drug_exp = request.POST['drug_expired'] 
        table.save()
        return redirect('/manage_drug')
    return render(request,'edit_d.html',context)

@login_required(login_url="/login")
def edit_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    context = {"type_data" : table}
    if request.method == "POST":
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'edit_t.html',context)


def increase_drug(request,pk):
    print (pk)
    table = drug.objects.get(drug_id=pk)
    update_qty = table.drug_qty+1
    table.drug_qty = update_qty
    table.save()
    return redirect('/manage_drug') 


def decrease_drug(request,pk):
    print (pk)
    table = drug.objects.get(drug_id=pk)#ORM 
    update_qty = table.drug_qty-1
    table.drug_qty = update_qty
    table.save()
    return redirect('/manage_drug')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return redirect('/login')


from django.shortcuts import get_object_or_404, redirect

def buy_drug_view(request):
    show_report = report_buy.objects.all() 
    context  = {"report" : show_report} 
    return render(request, "buy_drug.html", context)


@login_required(login_url="/login")
def buy_drug(request):
    context = {"userbuy": userbuy.objects.all(), "drugs": drug.objects.all()}
    if request.method == "POST":
        table = report_buy()
        table.username = request.POST.get('Busername')
        table.address = request.POST.get('Baddress')
        table.tal = request.POST.get('Btal')
        table.drug_name = request.POST.get('drug_name')
        table.drug_qty = request.POST.get('quantity')
        table.save()
    return render(request, 'buy_drugu.html', context)



from django.contrib.auth.models import User
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()
        return redirect('/login') 
    return render(request, 'register.html')

def report_a(request):
    show_report = report_buy.objects.all() 
    context  = {"report" : show_report} 
    return render(request,'report_a.html',context) 