from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    User model manager used in the creation of User instances.
    """
    def create_user(self, first_name, last_name, email_address, password, **kwargs):
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email_address = self.normalize_email(email_address),
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, *args):
        user = self.create_user(*args)

        user.is_admin = True
        user.save(using=self._db)
        return user
