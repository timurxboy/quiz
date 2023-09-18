from django.contrib import admin

from .models import answer
from .models.answer import Answer
from .models.category import Category
from .models.question import Question
from .models.quiz import Quizzes
from .models.user_response import UserResponse


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_filter = ['category']
    list_display_links = ['id', 'title']
    list_display = [
        'id',
        'title',
        'category',
    ]


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
    ]
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'difficulty',
    ]
    list_filter = ['quiz__category__name']
    list_display = [
        'title',
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInlineModel,
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = ['is_right', 'question__quiz__category__name']
    search_fields = ['question__title']
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'answer', 'is_correct']
    list_filter = ['user']
    search_fields = ['question__title']



