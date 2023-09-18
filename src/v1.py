from django.urls import path, include

quizzes = [
    path('quizzes/',
         include(
             (
                 'src.apps.quizzes.urls.quiz',
                 'src.apps.quizzes',
             ),
             namespace='quizzes'
         ),
         ),
]

user = [
    path('user/',
         include(
             (
                 'src.apps.user.urls.user',
                 'src.apps.user',
             ),
             namespace='user'
         ),
         ),
]

urlpatterns = quizzes + user
