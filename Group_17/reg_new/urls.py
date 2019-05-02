from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('registration.urls')),
    path('admin/',admin.site.urls),
    path('credits/', include('credits.urls')),
    path('book/',include('Book.urls')),
    path('package/',include('project.urls')),
    path('reviews/',include('user_reviews.urls'))
]
