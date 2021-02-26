from django.urls import path
from .views import reg, entry, logout


urlpatterns = [
    path('reg', reg),
    path('entry', entry),
    path('logout', logout),
]
