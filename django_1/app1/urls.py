from  django.urls import  path
from  .views import home_sahifa
from .views import Hodim,model_sahifa,Muzqaymoq_s,izoh_sahifa,hodim_button,muzqaymoq_t,Hodim_add
urlpatterns=[
    path('', home_sahifa.as_view(), name="home"),
    path('hodimlar/',Hodim.as_view(),name='hodim'),
    path('Izohlar/',model_sahifa.as_view(),name='sahifa3'),
    path('muzqaymoqlar/',Muzqaymoq_s.as_view(),name='muzqaymoq_sahifasi'),
    path('mavzu/<int:pk>/',izoh_sahifa.as_view(),name="sahifalar"),
    path('xodim/<int:pk>/', hodim_button.as_view(), name="hodimuz"),
    path('muzqaymoq_malumot/<int:pk>/', muzqaymoq_t.as_view(), name="muz_malum"),
    path('hodim/add/', Hodim_add.as_view(), name="hodim_add"),

]