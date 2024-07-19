from django.urls import include, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings
from . import views
from articles import views as article_views

urlpatterns = [
  re_path(r'^admin/', admin.site.urls),
  re_path(r'^articles/', include('articles.urls')),
  re_path(r'^bootstrap_test/', include('bootstrap_test.urls')),
  re_path(r'^mail/', include('app_mail.urls')),

  #accounts
  re_path(r'^accounts/', include('accounts.urls')),
  
  re_path(r'^about/$', views.about, name='about'),
  re_path(r'^$',article_views.main_page, name='main_page'),
  #appsample
  re_path(r'^appsample/', include('appsample.urls')),
  
  # app_forms
  re_path(r'^app_forms/', include('app_forms.urls')),

  re_path(r'^app_photos/', include('app_photos.urls')),
  re_path(r'^booking/', include('app_booking.urls')),


    
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)