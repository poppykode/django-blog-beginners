from accounts.models import User

def generate_password():
    new_password = User.objects.make_random_password()
    return new_password
