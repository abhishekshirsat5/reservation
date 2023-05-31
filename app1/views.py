from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import razorpay
from django.contrib.auth import authenticate, login, logout
from .models import Bookingss, RoomsAvailable, RoomsList, Bookings
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

RAZOR_KEY_ID = "rzp_test_HPR933L2nTKRBP"
RAZOR_KEY_SECRET = "9Qf2Gau5DKgdmjZ6k7GJyAlj"
rezerpay_clint = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


# Create your views here.
def index(request):
    return render(request, "app1/index.html")


def loginPage(request):
    if request.user.is_authenticated:
        myorder = Bookingss.objects.all().filter(email=request.user.email)
        return render(request, "app1/profile.html", context={
            "order": myorder,
        })

    if request.method == "POST":
        if "LoginF" in request.POST:
            usernameR = request.POST['userName']
            password = request.POST['password']
            userA = authenticate(username=usernameR, password=password)
            if userA is not None:
                login(request, userA)
                return render(request, "app1/index.html")

        if "Signup" in request.POST:
            userNames = request.POST['userNames']
            email = request.POST['email']
            passwords = request.POST['passwords']
            Cpassword = request.POST['Cpassword']
            if passwords == Cpassword:
                user = User.objects.create_user(
                    username=userNames, email=email, password=passwords)
                user.save()
                userA = authenticate(username=userNames, password=passwords)
                if userA is not None:
                    print(True)
                    login(request, userA)
                    return render(request, "app1/index.html")

    return render(request, "app1/LoginR.html")


def outuser(request):
    logout(request)
    return render(request, "app1/index.html")


def bookNow(request):
    room = RoomsAvailable.objects.all()
    roomList = RoomsList.objects.all()

    return render(request, "app1/bookingPage.html", context={
        "rooms": room,
        "roomList": roomList,
    })


def confirmPage(request):
    if request.method == "POST":
        addressU = request.POST['addressU']
        number = request.POST['number']
        sex = request.POST['sex']
        dob = request.POST['dob']
        cin = request.POST['cin']
        cout = request.POST['cout']
        mode = request.POST['optmode']
        print(request.POST['amounts'])
        if mode == "onlinepayment":
            clint_s = rezerpay_clint.order.create({
                "amount": int(request.POST['amounts']) * 100, "currency": 'INR', "payment_capture": 1,
            })
            client_id = clint_s["id"]
            book = Bookingss.objects.create(number=number,
                                           address=addressU,
                                           user=request.user.username,
                                           email=request.user.email,
                                           sex=sex,
                                           dob=dob,
                                           cin=cin,
                                           cout=cout,
                                           amount=request.POST['amounts'],
                                           mode=mode,
                                           roomname=request.POST["roomname"])
            book.save()
            send_mail(f"Room confirmed...",
                    f"hii. {request.user.username} your room is confirmed..   Room Tittle :{request.POST['roomname']},   amount :{request.POST['amounts']} ,   thank you..     please contact us :9113221473",
                      settings.EMAIL_HOST_USER, [str(request.user.email)])
            return render(request, "app1/online.html", context={
                "order_id": client_id,
                "amount": 300,
            })
        else:
            book = Bookingss.objects.create(number=number,
                                           address=addressU,
                                           user=request.user.username,
                                           email=request.user.email,
                                           sex=sex,
                                           dob=dob,
                                           cin=cin,
                                           cout=cout,
                                           amount=request.POST['amounts'],
                                           mode=mode,
                                           roomname=request.POST["roomname"])
            book.save()
            send_mail(f"Room confirmed...",
                      f"hii. {request.user.username} your room is confirmed..   Room Tittle :{request.POST['roomname']},   amount :{request.POST['amounts']} ,   thank you..     please contact us :9113221473",
                      settings.EMAIL_HOST_USER, [str(request.user.email)])
            return redirect("auth")

    return render(request, "app1/conformation.html")


def chenageway(request):
    if request.user.is_authenticated == True:
        if request.method == "POST":
            val = request.POST["val"]
            clint_s = rezerpay_clint.order.create({
                "amount": 300 * 100, "currency": 'INR', "payment_capture": 1,
            })
            client_id = clint_s["id"]
            return render(request, "app1/conformation.html", context={
                "val": val,
                "order_id": client_id,
                "amount": 300,
            })

    else:
        return render(request, "app1/LoginR.html")


def cancelOrder(request):
    if request.method == "POST":
        ids = request.POST["ids"]
        Bookingss.objects.get(id=ids).delete()
        return redirect("auth")
    return redirect("auth")


@csrf_exempt
def payment_complete(request):
    if request.method == "POST":
        if request.POST.get("razorpay_payment_id") is not None:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = rezerpay_clint.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                return redirect("index")
            else:
                print("failed")
    return HttpResponse("It's a payment page")

def renderConfirm(request):
    if request.method == 'POST':
        name=request.POST['rmname']
        amount=request.POST['amt']
        print(amount)
        clint_s = rezerpay_clint.order.create({
                "amount": int(amount) * 100, "currency": 'INR', "payment_capture": 1,
            })
        client_id = clint_s["id"]
        return render(request,"app1/conformation.html",context={
            "val":name,
            "order_id": client_id,
            "amount": amount,
        })