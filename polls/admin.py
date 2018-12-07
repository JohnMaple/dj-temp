from django.contrib import admin

from .models import Question, Choice


# 修改后台的管理表单
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 后台表格显示列
    list_filter = ['pub_date']  # 显示筛选
    search_fields = ['question_text']   # 显示搜索框
    list_per_page = 1


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
