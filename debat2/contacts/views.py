from django.shortcuts import render
from contacts.models import contact_req
# Create your views here.

def contact_form(request):
    if request.method == 'POST':
        user_name = request.POST.get('User_Name')
        user_email = request.POST.get('User_Email')
        user_message = request.POST.get('User_Message')
        contact_req.objects.create(name=user_name,Email=user_email ,Message=user_message)
    return render(request,'debat/contuct.html')
