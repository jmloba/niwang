from django.urls import include, re_path,path
from django.contrib import admin

from .views import RoomListView, BookingList, RoomDetailView, CancelBookingView
from app_booking import views



app_name='app_booking'

urlpatterns = [
  re_path(r'^room_list_view/$',views.RoomListView, name='RoomList'),
  

  path('room_detail_view/<category>', RoomDetailView.as_view(), name='room-detail-view' ),

  

  path('booking_list/', BookingList.as_view(), name ='BookingList'),

  # path('booking/', BookingView.as_view(), name ='bookingview'),


  path('booking/cancel/<pk>', CancelBookingView.as_view(), name ='CancelBookingView'),
  
  path('booked/', views.success_booking, name ='success-booking'),


    ]