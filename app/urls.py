from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.registerStudent,name='register'),
    path('students/',views.viewStudents,name='students'),
    path('login/',views.loginView,name='login'),
    path('logout/',views.logoutView,name='logout'),
    path('student_detail/<id>',views.student_detail,name='student_detail'),
    path('add_id/<id>',views.add_id,name='add_id'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)