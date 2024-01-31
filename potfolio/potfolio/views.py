from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import About
from django.contrib import messages
import re
import random
from django.core.signing import Signer
from django.core.mail import send_mail
from datetime import datetime
from django.utils.html import format_html

def login(request):
    if 'user_id' in request.session:
        return redirect('about')
    else:
        return render(request, 'login.html')
    
def logout(request):
    request.session.flush()
    return redirect('login')

def login_admin(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    log_data = About.objects.get(email=email)
    if(log_data.password==password and log_data.v_status== '1'):
        request.session['user_id'] =log_data.id
        request.session['user_name'] = log_data.u_name
        return redirect('about')
    else:
        return redirect('login')


def demo(request):

    title = "This is a demo html"
    name = "SHAWON"
    prodect_name = ['p1', 'p2', 'p3']
    data = {'t': title, 'name': name, 'prod': prodect_name}
    return render(request,'portfolio.html',data)
def demo1(request):
    a = 20
    b = 3
    c = a - b
    print(c)
    return HttpResponse(c)

def about_index(request):
    #if 'user_id' in request.session:
    all_data = About.objects.all()

    msg = messages.get_messages(request)

    data = {'d': all_data, 'msg':msg}

    return render(request,'admin/about.html', data)
# else:
    #     return render(request, 'login.html')
def reg_confin(request):
    return redirect('login')

def email_verify(request,id):
    data = About.objects.get(v_c=id)
    bool_var = False
    if data.v_status=='0':
        bool_var = False
        
        data.v_status = 1
        data.save()
        
        #return HttpResponse('This is zero')
    else:
        bool_var = True
    bool_dic = {'d': bool_var}
    return render(request, 'success.html', bool_dic)
    # data.v_status = 1
    # data.save()
    # return redirect('about')

def about_insert(request):
    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    no_exp = request.POST.get('no_exp')
    no_cus = request.POST.get('no_cus')
    no_proj = request.POST.get('no_proj')
    no_award = request.POST.get('no_award')
    desc = request.POST.get('desc')
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%d %b %Y-%I:%M %p")
    pattarn = r"^[a-zA-Z0-9_.]+@gmail.com"
    password = request.POST.get('password')

    
    # if not all([name, dob, phone, email, no_exp, no_cus, no_proj, no_award, desc]):
    #     messages.clear()
    #     messages.success(request, 'The field can not be empty')
    #     #return HttpResponse("All fields are required.")

    # else:
    # if not re.match(pattarn, email):
    #     messages.success(request, "Your emalil is not gmail")
    # elif len(phone)!= 11:
    #     messages.success(request, "Your Mobile Number must have 11 digit")
    # else:
    #     data = About.objects.all()
    #     len_data = len(data)
    #     if(len_data>=1):
    #         messages.success(request, "You can not entry more then onen data")
    #     else:

    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time.split(':'))
    h, m, s = map(int, current_time.split(':'))
    t_s = h*3600 + m*60 + s
    random_number = random.choices('1234567890',k=4)
    random_number = ''.join(random_number)
    t_s = str(t_s)
    c_v = t_s + random_number
    signer = Signer()
    encrypted_value = signer.sign(c_v).split(':')[1]

    link = f"<p>Congrtulations Mr {name} ! For registering as a user in our portfolio System. To confirm the registration </p><a href ='http://127.0.0.1:8000/admin/user/email_verification/"+encrypted_value+"' target ='_bland'>pleases click this Activation link</a>"

    send_mail(f"Mr. {name} please Confirm Your Registration - portflolio panel", encrypted_value, 'shawonshakib420@gmail.com',[email],html_message=link)
    print(encrypted_value)
    about_obj = About()  
    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = no_exp
    about_obj.no_happy_customers = no_cus
    about_obj.no_project_finished = no_proj
    about_obj.no_digital_awards = no_award
    about_obj.description = desc
    about_obj.date_time = current_date_time
    about_obj.v_c = encrypted_value
    about_obj.v_status = 0
    about_obj.password = password
    about_obj.save()


    return redirect('about')

def edit_index(request,id):
    data = About.objects.get(id=id)
    d = {'data':data}
    return render(request, 'admin/edit.html', d)

def about_edit(request):

    id = request.POST.get('id')

    name = request.POST.get('uname')
    dob = request.POST.get('dob')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    no_exp = request.POST.get('no_exp')
    no_cus = request.POST.get('no_cus')
    no_proj = request.POST.get('no_proj')
    no_award = request.POST.get('no_award')
    desc = request.POST.get('desc')
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%d %b %Y-%I:%M %p")

    about_obj = About.objects.get(id=id)

    about_obj.u_name = name
    about_obj.dob = dob
    about_obj.phone = phone
    about_obj.email = email
    about_obj.no_exp = no_exp
    about_obj.no_happy_customers = no_cus
    about_obj.no_project_finished = no_proj
    about_obj.no_digital_awards = no_award
    about_obj.description = desc

    about_obj.save()
    return redirect('about')