from rest_framework.serializers import ModelSerializer

from resumes.models import Specialty


class SpecialtySerializer(ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
