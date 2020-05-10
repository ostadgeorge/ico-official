from django.conf.urls.static import static
from django.urls import path
from . import views
from ico import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('contact-us/', views.contact_us, name="contact-us"),
    path('blog/', views.blog, name="blog"),
    path('blog/<int:cat_id>/', views.blog_list, name="blog-list"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
