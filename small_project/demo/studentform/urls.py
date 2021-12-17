from django.conf.urls import urls
from .views import AddstudentformAPIView,ReadstudentformAPIView,UpdatestudentformAPIView,DeletestudentformAPIView


urlpatterns = [
    url("addstudentform", AddstudentformAPIView(), name="add-student"),
    url("readstudentform",ReadstudentformAPIView.as_view()),
    url("updatestudentform/(?P<pk>.+)",UpdatestudentformAPIView.as_view()),
    url("deletestudentform/(?P<pk>.+)",DeletestudentformAPIView.as_view()),

]