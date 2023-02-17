#the two lines below are not recommanded
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, contact

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('contact/', contact, name='contact'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Jijiri Johnson Abusu Enterprise Director Dashboard"
admin.site.site_title= "Jijiri Johnson Abusu Enterprise"
admin.site.index_title='Welcome to Director Dashboard'