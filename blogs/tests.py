from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from CustomUsers.models import User
from blogs.models import Post, Comments
# Create your tests here.

# Я все еще помню о тестах, постараюсь прописать минималку, если успею.


class BasicTestingCase(TestCase):

    def setUp(self) -> None:
        self.register_url = reverse('signup')
        self.user = {"email": "test1@gmail.com", "username": "test1",
                "password": "password", "password2": "password"}

        self.user_short_pass = {"email": "test2@gmail.com", "username": "test2",
                "password": "pass", "password2": "passw"}

        self.user_unmatching_passwords = {"email": "test3@gmail.com", "username": "test3",
                "password": "password", "password2": "password123"}

        self.created_user = User.objects.create(email='test@mail.ru', username='username_test',
                                                password='password')
        self.post = Post.objects.create(
            title='Test', owner=self.created_user,
            created_at=timezone.now(), text='test text',
            tag='test')
        self.comment = Comments.objects.create(
            author=self.created_user, sent_at=timezone.now(),
            message='test text', post=self.post)


# Вторую регистрацию не успеваю

# class RegisterTestCase(BaseTestCase):
#
#     def test_can_register_user(self):
#         response = self.client.post(self.register_url, data=self.user)
#         self.assertEqual(response.status_code, 302)
