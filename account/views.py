from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import UserAccount
from authentication.views import RequestPasswordResetEmail
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# from .forms import UserAccountForm, UserAccountForm
# Create your views here.


def index(request):
    
    current_user = User.objects.get(username=request.user)
    account_details = UserAccount.objects.get(user=request.user)
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        fisrt_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        
        current_user.first_name = fisrt_name
        current_user.last_name = last_name
        current_user.email = email
        print (fisrt_name, last_name,phone_number)
        # import pdb
        # pdb.set_trace()
        account_details.phone_number = phone_number
        account_details.birth_date = birth_date
        # UserAccount.objects.create(user =request.user, phone_number = phone_number, birth_date = birth_date)
        current_user.save()
        account_details.save()
    
    context = {
        'current_user' : current_user,
        'account_details' : account_details
    }
    
    return render(request,'account/edit-account-details-tab.html', context)


def password_reset(request):
    # view = RequestPasswordResetEmail.as_view()
    # return view(request)
    if request.method == "GET":
        return render(request,'account/password-reset-tab.html')
    if request.method == "POST":
        user = User.objects.get(username=request.user)

        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        if check_password(old_password, user.password):
            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password was changed successfuly, you can login with your new password.')
                return redirect('login')
            else:
                messages.error(request, 'Confirm password does not match')
                return render(request, 'account/password-reset-tab.html')

        else : 
            messages.error(request, 'Old passwords entered was different')
            return render(request, 'account/password-reset-tab.html')

        
