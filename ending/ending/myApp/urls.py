from django.conf.urls import url
from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns=[
    path('index', views.show_index ),
    path('tools',  views.show_tools),
    path('ending',  views.show_ending),
    path('web',views.show_web),
    path('leak',views.show_leak),
    path('1',views.show_test),
    path('deal_web',views.web),
    path('deal_leak',views.leak),
]
