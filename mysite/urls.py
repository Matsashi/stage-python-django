import debug_toolbar
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__', include(debug_toolbar.urls)),
    path('', include('projects.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('project/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('quiz/', include('quiz.urls')),
]
