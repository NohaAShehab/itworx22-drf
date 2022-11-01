from rest_framework import serializers
from students.models import Student, Track

# class StudentSerilalizer(serializers.Serializer):
#     id = serializers.IntegerField(label='ID', read_only=True)
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(allow_blank=True, allow_null=True,
#                                    max_length=254, required=False)
#     salary = serializers.IntegerField(max_value=2147483647, min_value=-2147483648, required=False)
#     age = serializers.IntegerField(max_value=2147483647, min_value=-2147483648, required=False)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#     track = serializers.PrimaryKeyRelatedField(allow_null=True,
#                 queryset=Track.objects.all(), required=False)

class StudentSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
