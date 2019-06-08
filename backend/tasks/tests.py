from django.test import TestCase
from django.contrib.auth.models import User
from .models import TaskList, Task, Sharing


class TaskListModelTestCase(TestCase):

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
        self.assertQuerysetEqual(allowed_lists, [repr(self.user_1_list)])
