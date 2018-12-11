from django.contrib import admin
from .models import Article, Category, Tags


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'user', 'views', 'top', 'created_time')

    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title', 'user')

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['title', 'user', 'top']

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)

    # fk_fields 设置显示外键字段
    fk_fields = ['category']

    # 列表顶部，设置为False不在顶部显示，默认为True。
    # actions_on_top = False

    # 列表底部，设置为False不在底部显示，默认为False。
    # actions_on_bottom = False
    # 搜索框
    search_fields = ['title']

    # 右侧栏过滤属性
    list_filter = ['user__username', 'created_time']

    # 详细时间分层筛选
    date_hierarchy = 'created_time'

    # 定制Action行为具体方法
    def func(self, request, queryset):
        queryset.update(created_time='2018-09-28')
        # 批量更新我们的created_time字段的值为2018-09-28

    func.short_description = "中文显示自定义Actions"
    actions = [func, ]


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tags)


