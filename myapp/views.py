from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from myapp.models import Subject
from myapp.forms import SubjectForm

GRADE_POINTS = {'A': 90-100, 'A-':86-89, 'B+':82-85, 'B': 78-81, 'B-': 74-77,
                'C+': 70-73, 'C':65-69, 'c-':62-65, 'D+': 58-61, 'D':55-57, 'F':0-55}


@login_required(login_url='/login/')
def cgpa_calculator(request):
    subjects = Subject.objects.all()
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')

    #Calculate Cgpa
    total_credit = 0
    total_grade_points = 0

    for subject in subjects:
        total_credit += subject.credit
        total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

    if total_credit != 0:
        cgpa = total_grade_points/total_credit
    else:
        cgpa = 0

    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')
    else:
        form = SubjectForm(instance=subject)

    context = {
        'form': form,
        'subject_id': subject_id,
    }
    return render(request, 'edit_subject.html', context)

# Delete subject
@login_required(login_url='/login/')
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        subject.delete()
        return redirect('cgpa_calculator')

# Result
@login_required(login_url='/login/')
@login_required(login_url='/login/')
def result(request):
    subjects = Subject.objects.all()
    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')

    # Calculate CGPA
    total_credit = 0
    total_grade_points = 0
    for subject in subjects:
        total_credit += subject.credit
        total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)

    cgpa = total_grade_points / total_credit if total_credit else 0

    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }
    return render(request, 'pdf.html', context)


#Login page
def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, 'Username not found.')
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('cgpa_calculator')
            messages.error(request, 'Username or password is incorrect.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, 'login.html')

#Registation page
def register_page(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, 'Username already taken.')
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, 'Account created.')
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, 'register.html')

# Logout views
def logout_page(request):
    logout(request)
    return redirect('login')