import unittest

from password_masking_filter import PasswordMaskingFilter


class TestPasswordFiltering(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            'login': 'test_login',
            'some_field': {'password': "new"},
            'pass': 'Tes1qt!'
        }
        self.filtered_data = PasswordMaskingFilter.replace_passwords_with_asterisks(self.test_data)

    def test_mask_password(self):
        expected_password = '*' * 7
        self.assertEqual(self.filtered_data['pass'], expected_password,
                         'Password value should be changed with asterisks')

    def test_mask_inner_password(self):
        self.assertEqual(self.filtered_data['some_field']['password'], '***',
                         'Inner password value should be changed with asterisks')

    def test_unchangeable_fields(self):
        self.assertEqual(self.filtered_data['login'], 'test_login', 'Login value should not be changed')

    def test_original_data_dict_unchanged(self):
        self.assertNotEqual(self.filtered_data, self.test_data, 'Base test data should not be changed')

    def test_string_name(self):
        expected_data = 'password'
        actual_data = PasswordMaskingFilter.replace_passwords_with_asterisks(expected_data)
        self.assertEqual(actual_data, expected_data, 'Base test data should not be changed')


if __name__ == '__main__':
    unittest.main()
