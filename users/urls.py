from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static



app_name = 'users'

urlpatterns = [
    path('profile/signup/', views.signup_user, name='signup'),
    path('profile/login/', views.login_user, name='login'),
    path('profile/logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/create-review/', views.create_review, name='create_review'),
    path('exam/', views.exam_view, name='exam'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

