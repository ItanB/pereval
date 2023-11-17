from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PerevalAdded, Coords, Users
from .serializers import PerevalAddedSerializer


class PerevalAddedApiTestCase(APITestCase):

    def setUp(self):
        user_1 = Users.objects.create(email='Testest@test.com', phone=+111111, fam='Test1', name='Test2', otc='Test3')
        user_2 = Users.objects.create(email='Testt@test.com', phone=+1234567, fam='Test4', name='Test5', otc='Test6')
        coords_1 = Coords.objects.create(latitude=45.39, longitude=31.6, height=125)
        coords_2 = Coords.objects.create(latitude=31.96, longitude=67, height=250)
        self.pereval_1 = PerevalAdded.objects.create(user=user_1, beautyTitle='beautyTest', title="test",
                                                     other_titles='other_test', coords=coords_1)
        self.pereval_2 = PerevalAdded.objects.create(user=user_2, beautyTitle='beautyTest2', title="test2",
                                                     other_titles='other_test2', coords=coords_2)

    def test_get_list(self):
        url = reverse('submitData')
        response = self.client.get(url)
        serializer_data = PerevalAddedSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('submitDetailData', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalAddedSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PerevalAddedSerializerTestCase(TestCase):
    def setUp(self):
        user_1 = Users.objects.create(email="T", phone=1111, fam="Test1", name="Test2", otc="Test3")
        user_2 = Users.objects.create(email="Testtest@test.ru", phone=2222, fam="Test5", name="Test6", otc="Test7")
        coords_1 = Coords.objects.create(latitude=56.1234, longitude=57.1234, height=125)
        coords_2 = Coords.objects.create(latitude=39.6969, longitude=40.6060, height=250)
        self.pereval_1 = PerevalAdded.objects.create(user=user_1, beautyTitle="beautyTitleTest", title="titletestt",
                                                     other_titles="other_test",
                                                     coords=coords_1)
        self.pereval_2 = PerevalAdded.objects.create(user=user_2, beautyTitle='beautyTestt', title="testt",
                                                     other_titles='other_testt', coords=coords_2)

    def test_check(self):
        serializer_data = PerevalAddedSerializer([self.pereval_1, self.pereval_2], many=True).data

        expected_data = [
            {
                "id": 1,
                "user": {
                    "fam": "Test11",
                    "name": "Test22",
                    "otc": "Test33",
                    "email": "ttt@test.com",
                    "phone": 1234
                },
                "coords": {
                    "id": 1,
                    "latitude": 68.6766,
                    "longitude": 31.1848,
                    "height": 305
                },
                "season": None,
                "images": None,
                "beautyTitle": "beautyTitleTestt",
                "title": "titlet",
                "other_titles": "other_titletestt",
                "connect": None,
                "add_time": None,
                "status": None,
            },
            {
                "id": 2,
                "user": {
                    "fam": "Test1",
                    "name": "Test1",
                    "otc": "Test1",
                    "email": "Ttt@test.com",
                    "phone": 475987656984,
                },
                "coords": {
                    "id": 2,
                    "latitude": 39.6969,
                    "longitude": 40.6060,
                    "height": 2500
                },
                "season": None,
                "images": None,
                "beautyTitle": "beautyTitletest",
                "title": "titletest",
                "other_titles": "other_titletest",
                "connect": None,
                "add_time": None,
                "status": None,
            },
        ]

        self.assertEqual(serializer_data, expected_data)
