from Users.models import user
from django.shortcuts import redirect
from django.http import HttpResponse
def password_check(request):
    if request.method == 'POST':
        pasword=request.POST.get('pass')
        try:
            credential=user.objects.get(id=request.POST.get('id'))
        except Exception as E:
            msg="Error Occured -> System ERROR -- {}".format(E)
            url='/error/?Error={}'.format(msg)
            return redirect(url)
        else:
            if credential.password == pasword:
                return HttpResponse(1,"private_profile.html")
            else:
                return HttpResponse(2,"private_profile.html")