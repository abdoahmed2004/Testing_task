import re

class UserValidation:
    @staticmethod
    def validate_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_username(username):
        pattern = r'^\w{3,}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_egyptian_phone(phone):
        pattern = r'^(010|011|012|015)\d{8}$'
        return bool(re.match(pattern, phone))

    @staticmethod
    def validate_national_id(national_id):
        pattern = r'^[23]\d{13}$'
        return bool(re.match(pattern, national_id))
