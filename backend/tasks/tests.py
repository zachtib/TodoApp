from django.test import TestCase
from django.contrib.auth.models import User
from .models import TaskList, Task, Sharing


class TaskModelTestCase(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user('user_1')
        self.user_2 = User.objects.create_user('user_2')

        self.user_1_list = TaskList.objects.create(
            owner=self.user_1,
            name='User 1 List',
        )
        self.user_2_list = TaskList.objects.create(
            owner=self.user_2,
            name='User 2 List',
        )

    def test_user_has_access_to_own_lists(self):
        allowed_lists = TaskList.get_allowed_for_user(self.user_1).all()
        self.assertIn(self.user_1_list, allowed_lists)
        self.assertQuerysetEqual(allowed_lists, [repr(self.user_1_list)])

    def test_user_cannot_access_other_lists(self):
        allowed_lists = TaskList.get_allowed_for_user(self.user_1).all()
        self.assertNotIn(self.user_2_list, allowed_lists)

    def test_user_can_access_list_once_shared(self):
        Sharing.objects.create(tasklist=self.user_1_list, user=self.user_2)
        allowed_lists = TaskList.get_allowed_for_user(self.user_2).all()
        self.assertIn(self.user_1_list, allowed_lists)
