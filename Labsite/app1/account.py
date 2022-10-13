
from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect

from app1 import models
from app1 import modelforms
# from app1.utils.Pagination import Pagination



def login(request):
    if request.method == "GET":
        form = modelforms.LoginForm()
        return render(request,'dyyxh_login.html',{"form":form})
    form = modelforms.LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功
        # admin_object = models.admin.objects.filter(admin=form.cleaned_data["admin"],password=form.cleaned_data["password"]).first()
        admin_object = models.admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","账号或密码错误")
            return render(request,'dyyxh_login.html',{"form":form})
        request.session["info"] = {'id':admin_object.id,'name':admin_object.admin}
        return redirect("/dyyxh/members/list")
    return render(request,'dyyxh_login.html',{"form":form})