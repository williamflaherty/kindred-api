from django.conf.urls import patterns, url
from kindred_api import views

urlpatterns = patterns('',
               
                   # GET
                   #url(r'^get_photos_by_location_with_sort/$', views.get_photos_by_location_with_sort, name='get_photos_by_location_with_sort'),
                   #url(r'^get_photos_by_user/$', views.get_photos_by_user, name='get_photos_by_user'),
                   url(r'^get_todays_challenge/$', views.get_todays_challenge, name='get_todays_challenge'),
               
                   # INSERT/UPDATE
                   #url(r'^delete_photo_by_id/$', views.delete_photo_by_id, name='delete_photo_by_id'),
                   #url(r'^update_photo_by_id/$', views.update_photo_by_id, name='update_photo_by_id'),
                   url(r'^store_photo/$', views.store_photo, name='store_photo'),
                   url(r'^store_user/$', views.store_user, name='store_user'),

               
               )
