from django.urls import path
from .views import *

urlpatterns = [
  path('', welcome),
  

  # ---------- LIST ----------
  path('get_list/', get_list),
  path('get_lists/', get_lists),
  path('create_list/', create_list),
  path('delete_list/', delete_list),
  path('update_list/', update_list),

  # ---------- ITEM ----------
  path('get_item/', get_item),
  path('get_items/', get_items),
  path('create_item/', create_item),
  path('delete_item/', delete_item),
  path('update_item/', update_item),

  # ---------- GROUP ----------
  path('get_group/', get_group),
  path('get_groups/', get_groups),
  path('create_group', create_group),
  path('join_group/', join_group),
  path('leave_group/', leave_group),
  path('update_group/', update_group),

  # ---------- EVENT ----------
  path('create_event/', create_event),
  path('add_to_event/', add_to_event),
  path('remove_from_event/', remove_from_event),
  path('update_event/', update_event),
    
  # ---------- ADMIN ----------
  path('login_submit/', login_submit),
  path('signup_submit/', signup_submit),
  path('signout_submit/', signout_submit)
]