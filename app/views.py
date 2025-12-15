from django.shortcuts import render,redirect
from .forms import studentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Student,FeePayment
from . modules import get_cookies,get_slug,get_profile_matches,extract_cricket_stats
from django.contrib import messages
from datetime import date

def home(req):
    return render(req,'app/home.html')

@login_required(login_url='login')
def registerStudent(req):
    if req.method == 'POST':
        form = studentForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data['name'])
            form.save()
            return redirect('students')
        else:
            return render(req,'app/regStu.html',{'form':form})
    form = studentForm()
    return render(req,'app/regStu.html',{'form':form})

@login_required(login_url='login')
def viewStudents(req):
    students = Student.objects.all()
    return render(req,'app/stu_list.html',{'students':students})


def calculate_age(birthdate):
    today = date.today()
    return today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

def loginView(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        print(email,password)
        user = authenticate(username = email,password=password)
        login(req,user)
        return redirect('home')
    return render(req,'app/login.html')

@login_required(login_url='login')
def student_detail(request,id):
    student = Student.objects.get(pk=id)
    today = date.today()
    paid = FeePayment.objects.filter(
        student=student,
        month=today.month,
        year=today.year
    ).exists()
    if request.method == "POST" and 'run_python' in request.POST:
        print(request.POST)
        if student.player_id and student.player_name:
            cookies = get_cookies()
            slug = get_slug()
            resp = get_profile_matches(slug,student.player_id,student.player_name,cookies)
            player_data = resp['pageProps']['playerInfo']['data']
            bowling_style = player_data.get('bowling_style')
            batting_hand = player_data.get('batting_hand')
            batter_category = player_data.get('batter_category')
            bowler_category = player_data.get('bowler_category')
            playing_role = player_data.get('playing_role')
            dob = player_data.get('dob')
            total_matches = player_data.get('total_matches')
            total_wickets = player_data.get('total_wickets')
            total_runs = player_data.get('total_runs')
            student.total_matches = total_matches
            student.total_wickets = total_wickets
            student.total_runs = total_runs
            extracted = extract_cricket_stats(player_data['player_statement'])
            student.innings = extracted['turns']
            student.top_score = extracted['top_score']
            student.average = extracted['average']
            student.strike_rate = extracted['strike_rate']
            student.sixes = extracted['sixes']
            student.fours = extracted['fours']
            student.overs = extracted['overs']
            student.economy = extracted['economy']
            student.innings = extracted['turns']
            student.save()
        else:
            print('Player id or player name is not saved')
            messages.error(request,'Player id or player name is not saved')

    if request.method == "POST" and 'add_fee' in request.POST:
        date_ = request.POST.get('paid_on')        
        amount = request.POST.get('amount')   
        print(date_,amount)
        year = date_.split('-')[0]
        month = date_.split('-')[1]
        try:
            obj = FeePayment.objects.create(
                    student=student,
                    amount=amount,
                    paid_on=date_,
                    month=month,
                    year=year
                )
            message = "fees added successfully"
        except:
            message = "fees already paid for the current month"
        return render(request,'app/stuInfo.html',{'student':student,'today_date':date.today().strftime("%Y-%m-%d"),'paid':paid,'message':message})
    return render(request,'app/stuInfo.html',{'student':student,'today_date':date.today().strftime("%Y-%m-%d"),'paid':paid})

def logoutView(req):
    logout(req)
    return redirect('home')