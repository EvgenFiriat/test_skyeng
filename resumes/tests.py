from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    fixtures = ['test']

    def login(self, user, **headers):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {user.auth_token}", **headers
        )

    def setUp(self):
        self.user1 = User.objects.get(username='yauheni')
        self.user2 = User.objects.get(username='testuser')
        self.user1_resume = self.user1.resumes.first()
        self.user2_resume = self.user2.resumes.first()

        self.resume_detail_url = lambda resume: reverse(
            'resumes', args=(resume.id,)
        )

    def test_retrieve_resume_provides_proper_data(self):
        self.login(self.user1)
        response = self.client.get(path=self.resume_detail_url(self.user1_resume))
        self.assertIn('title', response.data)
        self.assertIn('status', response.data)
        self.assertIn('specialty', response.data)
        self.assertIn('salary', response.data)
        self.assertIn('education', response.data)
        self.assertIn('experience', response.data)
        self.assertIn('portfolio', response.data)
        self.assertIn('phone', response.data)
        self.assertIn('email', response.data)

    def test_partial_resume_update_returns_success(self):
        self.login(self.user1)
        data = {
            "status": "applying",
            "grade": 9,
            "specialty": 1,
            "salary": 10000,
            "education": "BSUIR",
            "experience": 2,
            "portfolio": "https://docs.google.com/document/d/1gK3OSRp-8C-Y5AZwDRmI2XojkPosdwZLQDrrcqi0F1s/edit",
            "title": "title1123",
            "phone": "+375291896089",
            "email": "17m2000y@gmail.com"
        }
        response = self.client.patch(path=self.resume_detail_url(self.user1_resume), data=data)
        self.assertEqual(response.status_code, 201)

    def test_partial_resume_phone_number_update_returns_failure_for_incorrect_format(self):
        self.login(self.user1)
        data = {
            "phone": "sdfsdf1896089",
        }
        response = self.client.patch(path=self.resume_detail_url(self.user1_resume), data=data)
        self.assertEqual(response.status_code, 400)

    def test_partial_resume_phone_number_update_returns_failure_for_incorrect_salary(self):
        self.login(self.user1)
        data = {
            "salary": -1000
        }
        response = self.client.patch(path=self.resume_detail_url(self.user1_resume), data=data)
        self.assertEqual(response.status_code, 400)

    def test_partial_update_for_non_author_returns_forbidden(self):
        self.login(self.user2)
        data = {
            "status": "applying",
            "grade": 9,
            "specialty": 1,
            "salary": 10000,
            "education": "BSUIR",
            "experience": 2,
            "portfolio": "https://docs.google.com/document/d/1gK3OSRp-8C-Y5AZwDRmI2XojkPosdwZLQDrrcqi0F1s/edit",
            "title": "title1123",
            "phone": "+375291896089",
            "email": "17m2000y@gmail.com"
        }
        response = self.client.patch(path=self.resume_detail_url(self.user1_resume), data=data)
        self.assertEqual(response.status_code, 403)


