
from django.urls import path
from . import views
urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name="blog_list"),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('blog/update/',views.BlogUpdateView.as_view(), name="blog_update"),
    path('blog/create/',views.BlogCreateView.as_view(), name="blog_create"),
    path('blog/delete/<int:pk>/', views.BlogDeleteView.as_view(), name="blog_delete")
]