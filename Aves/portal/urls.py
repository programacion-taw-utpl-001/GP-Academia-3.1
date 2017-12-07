from django.conf.urls import include, url, patterns
from . import views

urlpatterns = patterns('portal.views',
	url(r'^$', 'index_view', name='index'),
)