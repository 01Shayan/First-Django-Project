from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from account.models import Account
from django.core.mail import send_mail
from datetime import datetime
# from django.db.models import Q


def home(req):
    template = "home.html"
    return render(req, template)


# test page
def test(req):
    template = "test.html"
    return render(req, template)


def profile(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    template = "profile.html"
    return render(req, template)


def _login(req):
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        if False not in [username, password]:
            if req.user.is_authenticated:
                return redirect("/account")
            user = authenticate(req, username=username, password=password)
            if user:
                login(request=req, user=user)

                time = datetime.now()
                time = time.strftime("%c")
                subject = 'Login alert'
                message = f"login at {time}"
                from_email = 'info@shayanataei.co'
                to_email = user.email
                # send_mail(subject, message, from_email, [to_email], fail_silently=False)

                return redirect("/")
        return render(req, "login.html")
    else:
        if req.user.is_authenticated:
            return redirect("/account")
        template = "login.html"
        return render(req, template)


def _logout(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    logout(req)
    return redirect("/")


def register(req):
    if req.method == "POST":
        username = req.POST.get("username", False)
        password = req.POST.get("password", False)
        first_name = req.POST.get("first_name", False)
        last_name = req.POST.get("last_name", False)
        email = req.POST.get("email", False)

        users = User.objects.all()  # start user authentication system
        usrs = ''
        for user in users:
            usrs += str(user) + ' '
        # print(usrs)
        # print(username)
        if str(username) in usrs:
            return redirect(reverse("account:register"))  # end user authentication system

        elif False not in [username, password, email]:
            if first_name and last_name:
                user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
            else:
                user = User.objects.create_user(username, email, password)

            acc = Account()
            acc.user_id = user
            acc.save()

            login(req, user)
            return redirect(reverse("account:home"))  # 11

        # template="login.html"
        # template="register.html"
        return redirect(reverse("account:login"))
    else:
        template = "register.html"
        return render(req, template)


def getuser(req):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    user = User.objects.all()
    template = "get_user.html"
    return render(req, template, {"getUser": user})


def delete(req, id_user=None):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    if id_user:
        # print(id_user, type(id_user))
        try:
            user = User.objects.get(id=id_user)
            user.delete()
        except User.DoesNotExist:
            # print("Does not exist")
            return redirect(reverse("account:home"))
    # return redirect("/")
    return redirect(reverse("account:home"))  # 33


def profile_edit(req, id_user=None):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    if req.method == "POST":
        username = req.POST.get("username", False)
        first_name = req.POST.get("first_name", False)
        last_name = req.POST.get("last_name", False)
        father_name = req.POST.get("father_name", False)
        age = req.POST.get("age", False)
        gender = req.POST.get("gender", False)
        email = req.POST.get("email", False)
        try:
            user = User.objects.get(id=int(id_user))
            account = Account.objects.get(user_id=user)

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            account.father_name = father_name
            account.age = age
            account.gender = gender
            account.save()
            return redirect(reverse("account:profile"))
        except (User.DoesNotExist, Account.DoesNotExist):
            print("Does not exist 1")
            return redirect(reverse("account:get_user"))
    else:
        if id_user:
            try:
                user = User.objects.get(id=id_user)
                account = Account.objects.get(user_id=user)
                template = "profile_edit.html"
                return render(req, template, {"user_object": user, "account_object": account})
            except (User.DoesNotExist, Account.DoesNotExist):
                print("Does not exist 2")
        return redirect(reverse("account:get_user"))


def user_edit(req, id_user=None):
    if not req.user.is_authenticated:
        return redirect(reverse("account:login"))
    if req.method == "POST":
        username = req.POST.get("username", False)
        first_name = req.POST.get("first_name", False)
        last_name = req.POST.get("last_name", False)
        father_name = req.POST.get("father_name", False)
        age = req.POST.get("age", False)
        gender = req.POST.get("gender", False)
        email = req.POST.get("email", False)
        try:
            user = User.objects.get(id=int(id_user))
            account = Account.objects.get(user_id=user)

            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            account.father_name = father_name
            account.age = age
            account.gender = gender
            account.save()
            return redirect(reverse("account:get_user"))
        except (User.DoesNotExist, Account.DoesNotExist):
            print("Does not exist 1")
            return redirect(reverse("account:get_user"))
    else:
        if id_user:
            try:
                user = User.objects.get(id=id_user)
                account = Account.objects.get(user_id=user)
                template = "user_edit.html"
                return render(req, template, {"user_object": user, "account_object": account})
            except (User.DoesNotExist, Account.DoesNotExist):
                print("Does not exist 2")
        return redirect(reverse("account:get_user"))


def password_reset(req):
    subject = 'Subject here'
    message = 'Here is the message.'
    from_email = 'info@shayanataei.co'
    to_email = 'shayanataei1380@gmail.com'

    # send_mail(subject, message, from_email, to_email, fail_silently=False)
    # send_mail(subject, message, to_email, fail_silently=False)
    template = "password_reset.html"
    return render(req, template)
