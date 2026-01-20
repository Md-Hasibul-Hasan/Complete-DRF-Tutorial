from rest_framework import serializers
from .models import *

def start_with_x(value):
    if value[0].lower() == 'x' :
        raise serializers.ValidationError('Name cannot start with X')
    return value


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        validators=[start_with_x],
        label='Student Name'
        )

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        read_only_fields = ['id']
        extra_kwargs = {'name': {'required': True}}


    def validate_roll(self, data):
        if data>=100:
            raise serializers.ValidationError('seat full')
        
        return data
    
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == city.lower():
            raise serializers.ValidationError('Name and City should be different')
        return data



class SingerSerializer(serializers.ModelSerializer):
    rt_song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # rt_song = serializers.StringRelatedField(many=True, read_only=True)
    # rt_song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'rt_song']


class SongSerializer(serializers.ModelSerializer):

    singer = serializers.PrimaryKeyRelatedField(
        queryset=Singer.objects.all(),
        write_only=True
    )
    sung_by = SingerSerializer(read_only=True, source='singer')
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'sung_by'  ]