from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend, UserModel

# authenticates the user and checks with the entered email id and password
class EmailBackend(ModelBackend):
    def authenticate(self, username = None, password = None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email = username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None