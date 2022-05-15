from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,RegistrationView,purchaseform,form_valid,verify_trans,purchaseissues,purchaseissues_valid,processcomplete



urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/<str:ref>/',apply,name="apply"),
   path('apply-validate/',RegistrationView.as_view(),name="apply-validate"),
   path('purchaseform/',purchaseform,name="buyform"),
   path('purchasevalid/',form_valid,name="purchase-valid"),
   path('verify_trans/<str:ref_num>/',verify_trans,name="verify_trans"),
   path('purchaseissues/',purchaseissues,name='purchase-issues'),
   path("purchaseissues-valid/",purchaseissues_valid,name="purchaseissues-valid"),
   path("processcomplete/",processcomplete,name='processcomplete')
]