from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from resumes.models import Resume
from resumes.serializers.resumes import BaseResumeSerializer, ResumeDetailSerializer
from resumes.utils.permissions import IsAuthorPermission


class ResumesView(GenericAPIView):
    def get_queryset(self):
        return Resume.objects.prefetch_related('specialty')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ResumeDetailSerializer
        return BaseResumeSerializer

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAuthenticated(), IsAuthorPermission()]
        else:
            return [IsAuthenticated()]

    def patch(self, request, *args, **kwargs):
        resume = self.get_object()
        serializer = self.get_serializer(resume, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        resume = self.get_object()
        serializer = self.get_serializer(resume)
        return Response(serializer.data, status=status.HTTP_200_OK)
