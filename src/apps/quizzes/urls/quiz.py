from django.urls import path
from ..views.quiz import Quiz
from ..views.quiz_question import QuizQuestion
from ..views.random_question import RandomQuestion
from ..views.user_responded import UsersRespondedView
from ..views.user_response import UserResponseView
from ..views.response_all_results import ResponseAllResultsView

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions'),
    path('response_results/', ResponseAllResultsView.as_view(), name='response-results'),
    path('submit_response/', UserResponseView.as_view(), name='submit-response'),
    path('responded_users/<str:answer>', UsersRespondedView.as_view(), name='responded-users')
]
