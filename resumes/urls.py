from django.urls import path

from resumes.views.views import ResumesView

urlpatterns = [
    path('resumes/<int:pk>/', ResumesView.as_view(), name='resumes')
]
