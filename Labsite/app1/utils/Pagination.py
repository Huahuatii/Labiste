from django.utils.safestring import mark_safe
import copy

'''
自定义的分页组件，你需要用的话，需要做以下几件事：
----------------------------------------------------------------------------------------------------
在视图函数中：
def XX(request):
    # 1 根据情况筛选数据
    queryset = models.table.objects.all().order_by('')
    # 2 实例化对象
    page_object = Pagination(request,queryset)

    context = {
                "queryset":page_object.page_queryset,   # 分完页的数据
                "page_string":page_object.html()        # 生成页码
                }
    return render(request,'XX.html',context)
----------------------------------------------------------------------------------------------------
在HTML页面中: 

数据内容：
{% for obj in queryset %}
{{ obj.xx }}
{% endfor %}

分页栏：
<nav aria-label="...">
    <ul class="pagination">
      {{ page_string }}
    </ul>
  </nav>
'''

class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=2):
        '''
        request：请求对象
        queryset：符合条件的数据
        page_size：每页数据条数
        page_param：URL中传递的参数
        plus：显示的页码前后页数
        '''

        # 解决传递多个GET参数问题
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        total_count = queryset.count()
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        start_page = self.page - self.plus
        end_page = self.page + 3

        # 数据条数较少
        if self.total_page_count <= 5:
            start_page = 1
            end_page = self.total_page_count + 1

        # 当前页码小于3时，表示1-5
        elif self.page <= 2:
            start_page = 1
            end_page = 6

        # 当前页码接近最大页码时，表示最后5个页码
        elif self.page >= self.total_page_count - 2:
            start_page = self.total_page_count - 4
            end_page = self.total_page_count + 1

        # 添加首页功能
        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])
        first = '<li><a href="?{}">«</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(first)

        # 添加上一页功能
        if self.page > 1:
            # 解决传递多个GET参数问题
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}"><</a></li>'.format(self.query_dict.urlencode())
        else:
            prev = '<li class="disabled"><a><</a></li>'
        page_str_list.append(prev)

        # 添加主体分页栏
        for i in range(start_page, end_page):
            if i == self.page:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                self.query_dict.setlist(self.page_param, [i])
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 添加下一页功能
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">></a></li>'.format(self.query_dict.urlencode())
        else:
            prev = '<li class="disabled"><a>></a></li>'
        page_str_list.append(prev)

        # 添加尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        last = '<li><a href="?{}">»</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(last)

        # 全部转换为HTML代码（需要导包）
        page_string = mark_safe("".join(page_str_list))
        return page_string


