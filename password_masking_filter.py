"""
This creates filters for logging
"""

import copy
import logging
import typing


class PasswordMaskingFilter(logging.Filter):
    """Creates Password masking filters for logging"""

    def filter(self, record: typing.Any) -> None:
        """
        Method to check the specified record is to be logged
        :param record: Record of logging
        """
        if hasattr(record, 'msg') and isinstance(record.msg, dict):
            record.msg = self.replace_passwords_with_asterisks(record.msg)


    @staticmethod
    def replace_passwords_with_asterisks(record_dict: dict) -> dict:
        """
        Method to replace passwords values with asterisks
        :param record_dict: Dictionary to be analyzed
        :return: Updated dictionary with asterisks instead of passwords
        """
        if not isinstance(record_dict, dict):
            return record_dict
        password_expressions = ['password', 'pass', 'pwd']
        record_dict = copy.deepcopy(record_dict)
        for key in record_dict.keys():
            is_password_key = any(expression in key.lower() for expression in password_expressions)
            if isinstance(record_dict[key], dict):
                record_dict[key] = PasswordMaskingFilter.replace_passwords_with_asterisks(record_dict[key])
            elif is_password_key:
                record_dict[key] = '*' * len(record_dict[key])
        return record_dict
