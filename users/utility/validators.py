from django.core.validators import RegexValidator


USER_NAME_VALIDATOR = RegexValidator(
    regex=r'[`~!@#$%^&*()_|+=?;:"\',.<>{}\\[\/\]]',
    message='Name cannot contain special characters.',
    inverse_match=True
)
