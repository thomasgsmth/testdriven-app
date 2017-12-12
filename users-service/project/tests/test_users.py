# users-service/project/tests/test_users.py


import json
import unittest

from project.tests.base import BaseTestCase


class TestUserServices(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()
