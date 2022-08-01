from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    User model manager used in the creation of User instances.
    """
    def create_user(self, first, last, email, password, **kwargs):
        user = self.model(
            first_name  = first,
            last_name = last,
            email_address = self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first, last, email, password):
        user = self.create_user(
            email_address = email,
            first_name = first,
            last_name = last,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
