from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_basic(self):
        """Простой тест для проверки работы"""
        self.assertTrue(True)
