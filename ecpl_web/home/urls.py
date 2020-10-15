
from django.urls import path
from .views import index,contact,add_message,aboutus,claim_processing,pi_request,order_taking,certification
from .views import infra,careers,career_view,add_candidate,all_services,addcontact
urlpatterns = [
    path('',index),
    path('contact',contact),
    path('about',aboutus),
    path('submitmessage',add_message),
    path('claim_processing',claim_processing),
    path('pi_request',pi_request),
    path('order_taking',order_taking),
    path('certification',certification),
    path('infra',infra),
    path('careers',careers),
    path('all_services',all_services),
    path('add_candidate',add_candidate),
    path('career_view/<int:pid>',career_view),
    path('addcontact',addcontact),
]
