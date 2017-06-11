from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.success),
    url(r'^logout$', views.logout),
    url(r'^users/new$', views.new_user),
    url(r'^register/$', views.register),
    url(r'^users/edit$', views.profile_edit),
    url(r'^users/show/(?P<user_id>\d+)$', views.user_wall),
    url(r'^process/(?P<process>\w+)$', views.process_user),
    url(r'^add/message/(?P<to_who>\d+)$', views.add_message),
	url(r'^manage/(?P<user_level>\w+)$', views.manage_users),
	url(r'^users/delete/(?P<user_id>\d+)$', views.delete_user),
	url(r'^users/edit/(?P<user_id>\d+)$', views.edit_user_by_admin),
	url(r'^add/post/(?P<message_id>\d+)/(?P<user_id>\d+)$', views.add_post)

]
