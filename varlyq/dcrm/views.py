from django.shortcuts import render, redirect
from .forms import CreateUserForm, Loginform, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record 
from django.contrib import messages

def home(request):
    return render(request, 'dcrm/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect("my-login")
    context = {'form': form}
    return render(request, 'dcrm/register.html', context=context)

def my_login(request):
    form = Loginform()
    if request.method == "POST":
        form = Loginform(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form': form}
    return render(request, 'dcrm/my-login.html', context=context)

def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout success")
    return redirect("my-login")

@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'dcrm/dashboard.html', context=context)

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            reassign_sequence_ids()  
            messages.success(request,"Your record was created")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, 'dcrm/create-record.html', context=context)

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            reassign_sequence_ids() 
            messages.success(request,"Your record was updated")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, 'dcrm/update-record.html', context=context)

@login_required(login_url='my-login')
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'dcrm/view-record.html', context=context)

def reassign_sequence_ids():
    records = Record.objects.all().order_by('id')
    for index, record in enumerate(records, start=1):
        record.sequence_id = index
        record.save()

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    reassign_sequence_ids() 
    messages.success(request,"Your record was deleted")
    return redirect("dashboard")

@login_required(login_url='my-login')
def user_info(request):
    user = request.user
    context = {'user': user,}
    return render(request, 'dcrm/user-info.html', context=context)



