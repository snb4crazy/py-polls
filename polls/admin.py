from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
    Args:
        admin.StackedInline: input per row,
        admin.Tabular - all props of model in row
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)

