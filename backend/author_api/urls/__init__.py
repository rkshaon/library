from django.urls import path, include
from author_api.urls.v1 import urlpatterns as v1


urlpatterns = [
    path('v1/', include(v1)),
]
