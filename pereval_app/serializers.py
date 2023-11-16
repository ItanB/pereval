from .models import *
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'email',
            'fam',
            'name',
            'otc',
            'phone',
        ]

        def save(self, **kwargs):
            self.is_valid()
            user = Users.objects.filter(mail=self.validated_data.get('email'))
            if user.exists():
                return user.first()
            else:
                new_user = Users.objects.create(
                    fam=self.validated_data.get('fam'),
                    name=self.validated_data.get('name'),
                    otc=self.validated_data.get('otc'),
                    phone=self.validated_data.get('phone'),
                    mail=self.validated_data.get('email'),
                )
                return new_user


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = [
            'winter',
            'spring',
            'summer',
            'autumn',
        ]


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = [
            'latitude',
            'longitude',
            'height',
        ]


class ImagesSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PerevalImage
        fields = [
            'pk',
            'image'
        ]


class PerevalAddedSerializer(WritableNestedModelSerializer):
    coords = CoordsSerializer()
    season = SeasonSerializer()
    users = UserSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        # depth = 1
        fields = [
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'users',
            'coords',
            'season',
            'images',
            'status', ]

        def create(self, validated_data, **kwargs):
            users = validated_data.pop('users')
            coords = validated_data.pop('coords')
            season = validated_data.pop('season')
            images = validated_data.pop('images')

            users_ = Users.objects.filter(mail=users['email'])
            if users_.exists():
                users_serializer = UserSerializer(data=users)
                users_serializer.is_valid(raise_exception=True)
                users = users_serializer.save()
            else:
                author = Users.objects.create(**users)

            coords = Coords.objects.create(**coords)
            season = Season.objects.create(**season)
            pereval = PerevalAdded.objects.create(**validated_data, images=images, author=author, coords=coords,
                                                  season=season)
            if images:
                for im in images:
                    name = im.pop(name)
                    photos = photos.pop(photos)
                    PerevalImage.objects.create(pereval=pereval, name=name, photos=photos)

            return pereval

        def validate(self, data):
            if self.instance is not None:
                instance_users = self.instance.users
                data_users = data.get('users')
                users_fields_for_validation = [
                    instance_users.fam != data_users['fam'],
                    instance_users.name != data_users['name'],
                    instance_users.otc != data_users['otc'],
                    instance_users.phone != data_users['phone'],
                    instance_users.email != data_users['email'],
                ]
                if data_users is not None and any(users_fields_for_validation):
                    raise serializers.ValidationError(
                        {
                            'Ошибка!': 'Данные пользователя не могут быть изменены',
                        }
                    )

            return data


class PerevalDetailSerializer(WritableNestedModelSerializer):
    users = UserSerializer()
    images = ImagesSerializer()
    coords = CoordsSerializer()

    class Meta:
        model = PerevalAdded
        fields = [
            'id',
            'beautyTitle',
            'title',
            'other_titles',
            'connect',
            'add_time',
            'status',
            'season',
            'coords',
            'users',
            'images',
        ]

    def validate(self, data):
        users_data = data.get('users')
        users = self.instance.users
        if users_data is not None:
            if users.first_name != users_data.get('first_name') \
                    or users.last_name != users_data.get('last_name') \
                    or users.otc != users_data.get('otc') \
                    or users.email != users_data.get('email') \
                    or users.phone != users_data.get('phone'):
                raise ValidationError({'message': 'Редактирование пользовательских данных запрещено'})

            return data

