from rest_framework import serializers

from resumes.models import Resume
from resumes.serializers.specialtis import SpecialtySerializer


class BaseResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = (
            'status',
            'grade',
            'specialty',
            'salary',
            'education',
            'experience',
            'portfolio',
            'title',
            'phone',
            'email',
        )


class ResumeDetailSerializer(BaseResumeSerializer):
    specialty = SpecialtySerializer()
