from rest_framework import serializers
from crud_django_form.models import Item
from .models import Singer, Song


# serializer

# Validators
# def start_with_r(value):
#     # if value[0].lower() != 'r':
#     #     raise serializers.ValidationError('Name Should be start with R')

# class ItemSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30, validators=[start_with_r])
#     description = serializers.CharField(max_length=100)
#     price = serializers.FloatField()

#     def create(self, validated_data):
#         return Item.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         # print(instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.save()
#         return instance

#     def validate_price(self, value):
#         if value >= 1000.0:
#             raise serializers.ValidationError('Too Expensive')
#         return value

#     def vallidate(self, data):
#         description = data.get('description')
#         if description == '':
#             raise serializers.ValidationError('You have not entered anything in the description')
#         return data


# Model Serializer

# Validators
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name Should be start with R')
class ItemSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only= True)
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only' : True}}

    # Field level validation
    # def validate_price(self, value):
    #     if value >= 1000.0:
    #         raise serializers.ValidationError('Too Expensive')
    #     return value

    # Object level Validation
    # def vallidate(self, data):
    #     description = data.get('description')
    #     if description == '':
    #         raise serializers.ValidationError('You have not entered anything in the description')
    #     return data


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']


class ItemHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'url', 'name', 'description', 'price']


class SingerSerializerNested(serializers.ModelSerializer):
    # sung_by = SongSerializer

    class Meta:
        model = Singer
        # fields = ['id', 'name', 'gender', 'sung_by']
        fields = ['id', 'name', 'gender']
