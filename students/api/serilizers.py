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




# class StudentSerilalizer(serializers.ModelSerializer):
#     track_name = serializers.StringRelatedField(source="track")
#     class Meta:
#         model = Student
#         fields = '__all__'

####################### GeT track infromation

class TrackSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ["id", "name"]


class StudentSerilalizer(serializers.ModelSerializer):
    # track_name = serializers.StringRelatedField(source="track")
    track = TrackSerilalizer(read_only=True)
    track_id = serializers.IntegerField(write_only=True)
    t_name = serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = '__all__'
        fields.__add__("track_id")
        fields.__add__("t_name")

        
    def create(self, validated_data):
        print(validated_data)
        t_name = validated_data.pop("t_name")
        print(t_name)
        student=super(StudentSerilalizer, self).create(validated_data)

        try:
            track_obj  = Track.objects.filter(name=t_name)[0]
        except:
            track_obj = Track.objects.create(name=t_name)

        student.track = track_obj
        student.save()
        return student


    def update(self, instance, validated_data):
        student = super(StudentSerilalizer, self).update(instance, validated_data)
        return student

        











