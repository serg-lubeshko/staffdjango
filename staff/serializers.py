from rest_framework import serializers

from .models import Staff, GradePosition



class GradePositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradePosition
        fields = ["grade"]


class StaffSerializer(serializers.HyperlinkedModelSerializer):
    wages = serializers.StringRelatedField(many=True)
    class Meta:
        model = Staff
        fields = ["surname", "name", "patronymic", "employment_date", "wage", "staffs", "level", "wages"]

    level = GradePositionSerializer()
