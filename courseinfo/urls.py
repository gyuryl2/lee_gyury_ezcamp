from django.urls import path
from courseinfo.views import (
    CounselorList,
    CabinList,
    CourseList,
    RegistrationList,
    SessionList,
    CamperList,
    CounselorDetail,
    CabinDetail,
    SessionDetail,
    CourseDetail,
    CamperDetail,
    RegistrationDetail,
    CounselorCreate,
    CabinCreate,
    CourseCreate,
    SessionCreate,
    CamperCreate,
    RegistrationCreate,
    CounselorUpdate,
    CabinUpdate,
    CourseUpdate,
    CamperUpdate,
    SessionUpdate,
    RegistrationUpdate,
    RegistrationDelete,
    CounselorDelete,
    CabinDelete,
    CourseDelete,
    SessionDelete,
    CamperDelete,
)

urlpatterns = [

    path('counselor/',
         CounselorList.as_view(),
         name='courseinfo_counselor_list_urlpattern'),

    path('counselor/<int:pk>/',
         CounselorDetail.as_view(),
         name='courseinfo_counselor_detail_urlpattern'),

    path('counselor/create/',
         CounselorCreate.as_view(),
         name='courseinfo_counselor_create_urlpattern'),

    path('counselor/<int:pk>/update/',
         CounselorUpdate.as_view(),
         name='courseinfo_counselor_update_urlpattern'),

    path('counselor/<int:pk>/delete/',
         CounselorDelete.as_view(),
         name='courseinfo_counselor_delete_urlpattern'),


    path('cabin/',
         CabinList.as_view(),
         name='courseinfo_cabin_list_urlpattern'),

    path('cabin/<int:pk>/',
         CabinDetail.as_view(),
         name='courseinfo_cabin_detail_urlpattern'),

    path('cabin/create/',
         CabinCreate.as_view(),
         name='courseinfo_cabin_create_urlpattern'),

    path('cabin/<int:pk>/update/',
         CabinUpdate.as_view(),
         name='courseinfo_cabin_update_urlpattern'),

    path('cabin/<int:pk>/delete/',
         CabinDelete.as_view(),
         name='courseinfo_cabin_delete_urlpattern'),



    path('course/',
         CourseList.as_view(),
         name='courseinfo_course_list_urlpattern'),

    path('course/<int:pk>/',
         CourseDetail.as_view(),
         name='courseinfo_course_detail_urlpattern'),

    path('course/create/',
         CourseCreate.as_view(),
         name='courseinfo_course_create_urlpattern'),

    path('course/<int:pk>/update/',
         CourseUpdate.as_view(),
         name='courseinfo_course_update_urlpattern'),

    path('course/<int:pk>/delete/',
         CourseDelete.as_view(),
         name='courseinfo_course_delete_urlpattern'),



    path('session/',
         SessionList.as_view(),
         name='courseinfo_session_list_urlpattern'),

    path('session/<int:pk>/',
         SessionDetail.as_view(),
         name='courseinfo_session_detail_urlpattern'),

    path('session/create/',
         SessionCreate.as_view(),
         name='courseinfo_session_create_urlpattern'),

    path('session/<int:pk>/update/',
         SessionUpdate.as_view(),
         name='courseinfo_session_update_urlpattern'),

    path('session/<int:pk>/delete/',
         SessionDelete.as_view(),
         name='courseinfo_session_delete_urlpattern'),


    path('camper/',
         CamperList.as_view(),
         name='courseinfo_camper_list_urlpattern'),

    path('camper/<int:pk>/',
         CamperDetail.as_view(),
         name='courseinfo_camper_detail_urlpattern'),

    path('camper/create',
         CamperCreate.as_view(),
         name='courseinfo_camper_create_urlpattern'),

    path('camper/<int:pk>/update/',
         CamperUpdate.as_view(),
         name='courseinfo_camper_update_urlpattern'),

    path('camper/<int:pk>/delete/',
         CamperDelete.as_view(),
         name='courseinfo_camper_delete_urlpattern'),



    path('registration/',
         RegistrationList.as_view(),
         name='courseinfo_registration_list_urlpattern'),

    path('registration/<int:pk>/',
         RegistrationDetail.as_view(),
         name='courseinfo_registration_detail_urlpattern'),

    path('registration/create/',
         RegistrationCreate.as_view(),
         name='courseinfo_registration_create_urlpattern'),

    path('registration/<int:pk>/update/',
         RegistrationUpdate.as_view(),
         name='courseinfo_registration_update_urlpattern'),

    path('registration/<int:pk>/delete/',
         RegistrationDelete.as_view(),
         name='courseinfo_registration_delete_urlpattern'),

]
