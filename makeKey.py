from django.core.management.utils import get_random_secret_key

print(f"New SECRET KEY: {get_random_secret_key()}")
print("put it in your environment or settings.py")
print("do not check it into git repo")
