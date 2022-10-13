
from django.shortcuts import render
from django.shortcuts import redirect

from app1 import models
from app1 import modelforms
# from app1.utils.Pagination import Pagination

# Create your views here.
'''欢迎界面'''
def dyyxh(request):
    return render(request,'dyyxh.html')

'''模板界面'''
def layout(request):
    return render(request,'layout.html')

'''首页'''
def homepage(request):
    return render(request,'homepage.html')

'''研究方向界面'''
def research(request):
    return render(request,'research.html')

'''成员界面'''
def members(request):
    # ############# 分页栏 ####################################
    queryset = models.members.objects.filter(grade__lte=8).order_by('create_time')
    queryset_bys = models.members.objects.filter(grade=9).order_by('create_time')  # 毕业生
    queryset_bsh = models.members.objects.filter(grade=10).order_by('create_time')  # 博士后
    # page_object = Pagination(request=request,queryset=queryset,page_size=40)
    context = {
        'queryset': queryset,
        'queryset_bys': queryset_bys,
        'queryset_bsh': queryset_bsh,
        # 'page_string': page_object.html()
    }
    return render(request, 'members.html', context)

'''人员列表'''
def members_list(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    # 去数据库中获取所有部门信息
    # queryset类型[对象(一行信息),对象,对象]
    queryset = models.members.objects.all()
    return render(request, 'members_list.html', {'queryset': queryset})  # 将queryset参数传入html中

'''添加成员'''
def members_add(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    if request.method == "GET":
        form = modelforms.membersModelForm()
        return render(request, 'members_add.html', {'form': form})
    form = modelforms.membersModelForm(data=request.POST)
    form.save()  # 数据保存至数据库
    return redirect('/members/list')

'''删除成员'''
def members_delete(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    nid = request.GET.get('nid')
    models.members.objects.filter(id=nid).delete()
    return redirect('/members/list')

'''编辑成员'''
def members_edit(request,nid):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    row_obj = models.members.objects.filter(id=nid).first()
        # 根据ID获取相应数据
    if request.method == 'GET':
        form = modelforms.membersModelForm(instance=row_obj)
        return render(request, 'members_edit.html', {'form': form})

    form = modelforms.membersModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/members/list')
    return render(request, 'members/list', {'form': form})

'''文献列表'''
def achievement_list(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    queryset = models.articles.objects.all()
    return render(request,'articles_list.html',{'queryset':queryset})

'''添加文献'''
def articles_add(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    if request.method == "GET":
        form = modelforms.articlesModelForm()
        return render(request, 'articles_add.html', {'form': form})
    form = modelforms.articlesModelForm(data=request.POST)
    form.save()  # 数据保存至数据库
    return redirect('/achievement/list')

'''删除文献'''
def achievement_delete(request):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    nid = request.GET.get('nid')
    models.articles.objects.filter(id=nid).delete()
    return redirect('/achievement/list')

'''研究成果界面'''
def achievement(request):
    queryset = models.articles.objects.filter(cat_class=2).order_by('-ifr')
    queryset_all = models.articles.objects.filter(cat_class__lte=2).order_by('-birthday')
    context = {
        'queryset': queryset,
        'queryset_all': queryset_all,
    }
    return render(request,'achievement.html',context)

'''编辑研究成果'''
def achievement_edit(request,nid):
    info = request.session.get("info")
    if not info:
        return redirect('/login')
    row_obj = models.articles.objects.filter(id=nid).first()
        # 根据ID获取相应数据
    if request.method == 'GET':
        form = modelforms.articlesModelForm(instance=row_obj)
        return render(request, 'achievement_edit.html', {'form': form})

    form = modelforms.articlesModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/achievement/list')
    return render(request, 'achievement/list', {'form': form})

'''数据库界面(可删)'''
def databases(request):
    return render(request,'databases.html')

'''联系我们'''
def contact(request):
    return render(request,'contact.html')

'''(可删)'''
def test(request):
    return render(request,'test.html') 
