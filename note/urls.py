from django.conf.urls import url
from note import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [ 
    url(r'^note$', views.NoteList.as_view(),name='NoteList'),
    url(r'^note/(?P<pk>[0-9]+)$', views.NoteDetail.as_view(),name='NoteDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)