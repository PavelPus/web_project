from django.urls import path, re_path
from . import views

app_name = 'ls'

urlpatterns = [
    path('', views.index, name='index' ),
    ######### Овощи ####################################
    path('vegetables/', views.VegList, name='VegList' ),
    path('vegetables/<str:veg_type>/', views.InVegList, name='InVegList' ),
    path('vegetables/<str:veg_type>/<str:veg_vids>/', views.InVegList, name='InVegList' ),
    path('vegetables/<str:veg_type>/<str:veg_vids>/sorts/<str:name>/', views.SortDetails, name='SortDetails' ),
    path('vegetables/<str:veg_type>/sorts/<str:name>/', views.SortDetails, name='SortDetails' ),
    
    ######### Цветы ####################################
    path('flowers/', views.FlowersVid, name='FlowersVid' ),
    path('flowers/<str:vid>/', views.FlowersVidDetails, name='FlowersVidDetails' ),
    path('flowers/<str:vid>/<str:name>/', views.FlowersSortDetails, name='FlowersSortDetails' ),
    
    path('compare/', views.CompareList, name='CompareList' ),
    re_path(r'search/', views.SearchList, name='SearchList' ),
    re_path(r'vote/', views.SortVote, name='SortVote' ),
    re_path(r'addcompare/', views.SortCompare, name='SortCompare' ),
    path(r'delcompare/', views.SortCompareDel, name='SortCompareDel' ),
    path('contact/', views.Contact, name='Contact'),
    path('success/', views.Success, name='Success'),
    path('send-response/', views.SendResponse, name='SendResponse'),
    re_path(r'send-comment/', views.SendResponse, name='SendResponse' ),

    ############ Статические html ########################################
    
]
