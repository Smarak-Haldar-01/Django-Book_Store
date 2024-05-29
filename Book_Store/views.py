from django.http import HttpResponse

from django.shortcuts import render,redirect

from Book_Store.login import login

from Book_Store.signin import signinf

from Users.models import user,product,ordered,reportProblem_1

from Book_Store.add_product import add_product

from Book_Store.order import order

from Book_Store.report_problem import report_problem

from django.contrib.auth import logout as log_out

import os



def index(request):
    try:
        items=product.objects.all()
    except Exception as E:
        msg="Run Time Error - System-Error -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'base_index.html',{'Title':'Home','items':items})

def log_in(request):
    form_login=login()
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            credential=user.objects.get(email=email,password=password,user_auth=1)
        except:
            return render(request,'login.html',{'Title':'Log-In','login':form_login,'Error':'You may be an Invalid User or You have inputed wrong credentils... Try Again... Or Register Freshly...'})
        else:
            # email=credential.email
            # url='/?email={}'.format(email)
            if credential.user_type == 'Manager' and credential.user_auth == 1:
                try:
                    items=product.objects.all()
                except Exception as E:
                    msg="Run Time Error - System-Error -- {}".format(E)
                    url='/error/?Error={}'.format(msg)
                    return redirect(url)
                else:
                    return render(request,'private_index.html',{'Title':'Home','details':credential,'items':items,'id':credential.id})
            else:
                try:
                    items=product.objects.all()
                except Exception as E:
                    msg="Run Time Error - System-Error -- {}".format(E)
                    url='/error/?Error={}'.format(msg)
                    return redirect(url)
                else:
                    return render(request,'user_index.html',{'Title':'Home','details':credential,'items':items,'id':credential.id})
    return render(request,'login.html',{'Title':'Log-In','login':form_login,'Error':False})

def signin(request):
    form_signin=signinf()
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        cr_pass=request.POST.get('cr_pass')
        c_pass=request.POST.get('c_pass')
        address=request.POST.get('address')
        address_2=''
        if request.POST.get('address_2'):
            address_2=request.POST.get('address_2')
        pic=request.FILES.get('profile_pic')
        try:
            if user.objects.get(email=email) :
                return render(request,'signin.html',{'Title':'Signin','Congrats':'Account Already Exists! Try Login.','signin':form_signin})
        except Exception as E:
            if len(cr_pass)>=8:
                if cr_pass==c_pass:
                    if not name.isalnum():
                        if address :
                            try:
                                save_data=user(uname=name,email=email,password=c_pass,address=address+'-'+address_2,pic=pic)
                                save_data.save()
                            except Exception as E:
                                msg="Run Time Error - System-Error -- {}".format(E)
                                url='/error/?Error={}'.format(msg)
                                return redirect(url)
                            else:
                                return render(request,'signin.html',{'Title':'Signin','Congrats':'Account Created Successfully!','signin':form_signin})
                        else:
                            return render(request,'signin.html',{'Title':'Signin','Error':'Enter a valid Address','signin':form_signin})
                    else:
                        return render(request,'signin.html',{'Title':'Signin','Error':'Invalid Name Type','signin':form_signin})
                else:
                    return render(request,'signin.html',{'Title':'Signin','Error':'Confirm Password doesn\'t matches with Created Password','signin':form_signin})
            else:
                return render(request,'signin.html',{'Title':'Signin','Error':'Password is too short','signin':form_signin})
    else:
        return render(request,'signin.html',{'Title':'Signin','Error':False,'signin':form_signin})
                    

def error(request):
    Error=request.GET.get("Error")
    return render(request,'error.html',{'Title':'Error.caused.Trouble','Error':Error})

def manager_add_product(request,id):
    try:
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Run Time Error - System-Error -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        form=add_product()
        if request.method == 'POST':
            name=request.POST.get('name')
            if name == '':
                return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Product name is missing','id':credential.id,'name':credential.uname,'pic':credential.pic})
            detail=request.POST.get('details')
            if detail =='':
                return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Product Details is missing','name':credential.uname,'pic':credential.pic,'id':credential.id})
            try:
                price=float(request.POST.get('price'))
            except:
                return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Invalid Type of Price','name':credential.uname,'pic':credential.pic,'id':credential.id})
            else:
                offers=''
                if request.POST.get('offers'):
                    offers=request.POST.get('offers')
                pic=request.FILES.get('pic')
                if pic=='':
                    return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Product image is missing','name':credential.uname,'pic':credential.pic,'id':credential.id})
                pic2=''
                pic3=''
                pic4=''
                pic5=''
                if request.FILES.get('pic2'):
                    pic2=request.FILES.get('pic2')
                if request.FILES.get('pic3'):
                    pic3=request.FILES.get('pic3')
                if request.FILES.get('pic4'):
                    pic4=request.FILES.get('pic4')
                if request.FILES.get('pic5'):
                    pic5=request.FILES.get('pic5')
                ptype=request.POST.get('select')
                edoc=request.FILES.get('edoc')
                if edoc == '':
                    return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Product\'s Downloadable file is missing'})
                if ptype=='':
                    return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Error': 'Product Type is missing'})
                try:
                    object_save=product(name=name,product_type=ptype,details=detail,product_price=price,product_offers=offers,pic=pic,pic2=pic2,pic3=pic3,pic4=pic4,pic5=pic5,edoc=edoc)
                    object_save.save()
                except Exception as E:
                    msg="Run Time Error - System-Error -- {}".format(E)
                    url='/error/?Error={}'.format(msg)
                    return redirect(url)
                else:
                    return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'Congrats':'Product(s) Added Successfully.','name':credential.uname,'pic':credential.pic,'id':credential.id})
        return render(request,'manager_add_prodcut.html',{'Title':'Add Product','frm':form,'name':credential.uname,'pic':credential.pic,'id':credential.id})

def logout(request):
    try:
        request.session.clear()
        items=product.objects.all()
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        log_out(request)
        return render(request,'base_index.html',{'Title':'Home','items':items})
    
def private_index(request,id):
    # print(request.path)
    try:
        items=product.objects.all()
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'private_index.html',{'Title':'Home','items':items,'name':credential.uname,'pic':credential.pic,'id':id})
    
# def deletes(request,mid,pid):
#     try:
#         credential=user.objects.get(id=mid)
#         dels=product.objects.get(id=pid)
#         dels.delete()
#     except Exception as E:
#         msg="Error Occured -> System ERROR -- {}".format(E)
#         url='/error/?Error={}'.format(msg)
#         return redirect(url)
#     else:
#         try:
#             items=product.objects.all()
#         except Exception as E:
#             msg="Error Occured -> System ERROR -- {}".format(E)
#             url='/error/?Error={}'.format(msg)
#             return redirect(url)
#         else:
#             return render(request,'view_products.html',{'Title':'View Products','items':items,'Congrats':'Product(s) Deleted Successfully.','name':credential.uname,'pic':credential.pic,'id':mid})

def delete_product(request):
    if request.method == 'GET':
        pid=request.GET.get('pid')
        mid=request.GET.get('mid')
        try:
            product.objects.get(id=pid).delete()
            items=product.objects.all()
            credential=user.objects.get(id=mid)
        except Exception as E:
            msg="Error Occured -> System ERROR -- {}".format(E)
            url='/error/?Error={}'.format(msg)
            return redirect(url)
        else:
            return render(request,'view_products.html',{'Title':'View Products','items':items,'name':credential.uname,'pic':credential.pic,'id':mid,'info':credential})

def productView(request,id):
    try:
        items=product.objects.all()
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'view_products.html',{'Title':'View Products','items':items,'name':credential.uname,'pic':credential.pic,'id':id,'info':credential})

def user_index(request,id):
    try:
        items=product.objects.all()
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'user_index.html',{'Title':'Home','items':items,'id':id,'name':credential.uname,'pic':credential.pic,})
    
def orders(request,id):
    ordere=order()
    try:
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        if request.method == 'POST':
            umail=request.POST.get('email')
            if umail=='':
                return render(request,'user_order.html',{'Title':'Order Item(s)','Error':'Cannot find Sender\'s Mail...','name':credential.uname,'pic':credential.pic,'order':ordered,'id':id})
            or_n=request.POST.get('order_name')
            if or_n=='':
                return render(request,'user_order.html',{'Title':'Order Item(s)','Error':'Product name cannot be empty!','name':credential.uname,'pic':credential.pic,'order':ordered,'id':id})
            or_d='~~~ No Details ~~~'
            if request.POST.get('order_details'):
                or_d=request.POST.get('order_details')
            ex_d='~~~ No Date ~~~'
            if request.POST.get('ex_order_delvery'):
                ex_d=request.POST.get('ex_order_delvery')
            ex_t='~~~ No Time ~~~'
            if request.POST.get('ex_order_time'):
                ex_t=request.POST.get('ex_order_time')
            try:
                order_save=ordered(uid=user.objects.get(id=id),umail=umail,order_name=or_n,order_details=or_d,ex_order_delevery=ex_d,ex_order_delevery_time=ex_t)
                order_save.save()
            except Exception as E:
                msg="Error Occured -> System ERROR -- {}".format(E)
                url='/error/?Error={}'.format(msg)
                return redirect(url)
            else:
                return render(request,'user_order.html',{'Title':'Order Item(s)','Congrats':'Product(s) Order Sent Successfully.','name':credential.uname,'pic':credential.pic,'order':ordere,'id':id})
    return render(request,'user_order.html',{'Title':'Order Item(s)','name':credential.uname,'pic':credential.pic,'order':ordere,'id':id})

def viewOrder(request,id):
    try:
        ob_order=ordered.objects.all()
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'view_order.html',{'Title':'View Ordered Item(s)','name':credential.uname,'pic':credential.pic,'id':id,'order_info':ob_order})

def deleteUser(request):
    try:
        id=request.GET.get('id')
        del_ob=user.objects.get(id=id)
        if os.path.isfile("./Media/"+str(del_ob.pic)):
            os.remove('./Media/'+str(del_ob.pic))
        del_ob.delete()
        details=product.objects.all()
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'base_index.html',{'Title':'Home','details':details})
    
def report_problem_u(request,id):
    try:
        report=report_problem()
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        if request.method == 'POST':
            email=request.POST.get('email')
            title=request.POST.get('report_title')
            details=request.POST.get('report_details')
            pdate=request.POST.get('problem_date')
            ptime=request.POST.get('problem_time')
            rpic=request.FILES.get('report_pic')
            utype=credential.user_type
            try:
                report_save=reportProblem_1(uid=credential,umail=email,utype=utype,report_title=title,explain=details,problem_pic=rpic,problem_date=pdate,problem_time=ptime)
                report_save.save()
            except Exception as E:
                msg="Error Occured -> System ERROR -- {}".format(E)
                url='/error/?Error={}'.format(msg)
                return redirect(url)
            else:
                return render(request,'report_user.html',{'Title':'Report Problem','name':credential.uname,'pic':credential.pic,'id':id,'report_problem':report,'Congrats':'Reported Successfully! You may Follow the Report Status from Status. '})
        return render(request,'report_user.html',{'Title':'Report Problem','name':credential.uname,'pic':credential.pic,'id':id,'report_problem':report})

def reported_problems(request,id):
    try:
        # report=reportProblem_1.objects.get(utype='Client')
        report=reportProblem_1.objects.all().filter(utype='Client')
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'private_user_reported_problems.html',{'Title':'Reported Problems','name':credential.uname,'pic':credential.pic,'id':id,'report_info':report,'info':credential})

def helpLine(request):
    return render(request,'helpline.html',{'Title':'Help Desk'})

def delete_report(request):
    if request.method == 'GET':
        id=request.GET.get('id')
        mid=request.GET.get('mid')
        try:
            ob_del=reportProblem_1.objects.get(id=id)
            if os.path.isfile("./Media/"+str(ob_del.problem_pic)):
                os.remove('./Media/'+str(ob_del.problem_pic))
            ob_del.delete()
            report=reportProblem_1.objects.all().filter(utype='Client')
            credential=user.objects.get(id=mid)
        except Exception as E:
            msg="Error Occured -> System ERROR -- {}".format(E)
            url='/error/?Error={}'.format(msg)
            return redirect(url)
        else:
            return render(request,'private_user_reported_problems.html',{'Title':'Reported Problems','name':credential.uname,'pic':credential.pic,'id':id,'report_info':report})

def private_profile(request,id):
    try:
        credential=user.objects.get(id=id)
    except Exception as E:
        msg="Error Occured -> System ERROR -- {}".format(E)
        url='/error/?Error={}'.format(msg)
        return redirect(url)
    else:
        return render(request,'private_profile.html',{'Title':f'Profile | {credential.uname}','name':credential.uname,'pic':credential.pic,'id':id,'details':credential})
    
def update_profile_pic(request,id):
    if request.method == 'POST':
        if request.FILES.get('pic'):
            print('OK')
            try:
                credential=user.objects.get(id=id)
            except Exception as E:
                msg="Error Occured -> System ERROR -- {}".format(E)
                url='/error/?Error={}'.format(msg)
                return redirect(url)
            else:
                heading = "Profile Picture Uploaded Successfully!"
                return render(request,'private_profile.html',{'Title':f'Profile | {credential.uname}','name':credential.uname,'pic':credential.pic,'id':id,'details':credential,'E_1':'pass','heading':heading})
        else:
            heading="Picture Not Found!!"
            try:
                credential=user.objects.get(id=id)
            except Exception as E:
                msg="Error Occured -> System ERROR -- {}".format(E)
                url='/error/?Error={}'.format(msg)
                return redirect(url)
            else:
                return render(request,'private_profile.html',{'Title':f'Profile | {credential.uname}','name':credential.uname,'pic':credential.pic,'id':id,'details':credential,'E_1':'N_pass','heading':heading})