from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('letters/', views.letters,name='letters'),
    path('post/<int:pk>/', views.detail_page, name='detail_page'),
    # path('category/<category>/', views.CatListView.as_view(template_name='core/category.html'), name='category'),
    # path("post/<slug>/", views.PostDetailView.as_view(), name="post_detail"),

]
