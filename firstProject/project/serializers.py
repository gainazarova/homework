from rest_framework import serializers
from project.models import Group, GroupStudents, Students, Teacher


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title')

class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudents
        fields = ('student',)


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['students'] = GroupStudentSerializer(
            instance.groups.all(), many=True
        ).data
        return representation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        field = '__all__'
