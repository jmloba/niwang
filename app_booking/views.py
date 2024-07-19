from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages

from .models import Room, Booking
from app_booking.forms import AvailabilityForm

from app_booking.booking_functions.availability import check_availability

from app_booking.booking_functions.get_room_cat_url_list import get_room_cat_url_list

from app_booking.booking_functions.get_room_category_human_format import get_room_category_human_format
from app_booking.booking_functions.get_available_rooms import get_available_rooms

from app_booking.booking_functions.book_room import book_room 

from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.
def RoomListView(request):
  room_category_url_list = get_room_cat_url_list()
  context = { 'room_list':room_category_url_list} 
  return render(request,'app_booking/room_list.html', context)




class RoomDetailView(View) : 
  '''
  Room detail view  is a generic view based
  '''
  def get(self, request, *rgs, **kwargs):
    # get Room Category from keywords arguments
    category =self.kwargs.get('category',None)
    # call function  get the  value of the category not the key
    human_format_room_category = get_room_category_human_format(category)
    form = AvailabilityForm()
    # check for invalid category names
    if human_format_room_category is not None:
      context={ 
        'room_category':human_format_room_category, 
        'form': form 
        }
      return render(request,'room_detail_view.html',context)
    else:
      return HttpResponse('Category does not exist')
   
  def post(self, request, *rgs, **kwargs):    
    category =self.kwargs.get('category',None)
    form = AvailabilityForm(request.POST)

    # checking form validity
    if form.is_valid():
      data = form.cleaned_data


    available_rooms = get_available_rooms(category,data['check_in'],data['check_out'])
    if(data['check_in']>=data['check_out']):
      return HttpResponse('Checkin date is greater than checkout date')
    # ********
      # return redirect('app_booking:RoomList')




    if available_rooms is not None:
      
      booking = book_room(request,available_rooms[0],data['check_in'],data['check_out'])

      context={'booking':booking}
      return render(request,'app_booking/success-booking.html',context)
    else :
      context={}
      return render(request,'app_booking/response-room-booked.html',context)      
      

        

class BookingList (ListView):
  model = Booking
  template_name = 'booking_list.html'
  def get_queryset(self,*args, **kwargs):
    if self.request.user.is_staff:
      booking_list = Booking.objects.all()
      return booking_list
    else:
      booking_list = Booking.objects.filter(user = self.request.user) 
      return booking_list
    

 
    
class    CancelBookingView(DeleteView):
  model=Booking
  template_name='booking_cancel_view.html'
  success_url = reverse_lazy('app_booking:BookingList')

def success_booking(request):
  pass




    
  

