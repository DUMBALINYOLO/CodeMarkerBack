"""Tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app import views


urlpatterns = [
    url(r'^codemarker/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    url(r'^api/obtain-auth-token/$', views.CustomObtainAuthToken.as_view()),

    url(r'^api/get-user/$', views.GetCurrentUserData.as_view()),

    url(r'^api/users/$', views.UsersList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$',
        views.UsersDetail.as_view(), name='users-detail'),

    url(r'^api/courses/$', views.CoursesList.as_view(), name='courses-list'),
    url(r'^api/courses/(?P<pk>[0-9]+)/$',
        views.CoursesDetail.as_view(), name='courses-detail'),

    url(r'^api/courses/users/delete/$', views.CoursesUsersDestroy.as_view(),
        name='courses-users-delete'),

    url(r'^api/courses/users/delete/$', views.CoursesUsersDestroy.as_view(),
        name='courses-users-delete'),
    url(r'^api/courses/users/add/$', views.CoursesUsersAdd.as_view(),
        name='courses-users-add'),

    url(r'^api/submissions/$', views.SubmissionsList.as_view(),
        name='submissions-list'),
    url(r'^api/submissions/(?P<pk>[0-9]+)/$',
        views.SubmissionsDetail.as_view(), name='submissions-detail'),

    url(r'^api/assessments/$', views.AssessmentsList.as_view(),
        name='assessments-list'),
    url(r'^api/assessments/(?P<pk>[0-9]+)/$',
        views.AssessmentsDetail.as_view(), name='assessments-detail'),

    url(r'^api/submissions/(?P<submission_id>\d+)/process/$',
        views.process_submission, name='submission-process'),

    url(r'^api/create_backup/$',
        views.create_backup, name='create-backup'),

    url(r'^api/restore_backup/$',
        views.restore_backup, name='create-backup'),
]
