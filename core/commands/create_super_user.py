import argparse
import django
import sys, os

sys.path.append('.')
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
django.setup()

from django.contrib.auth.models import User  # noqa


def create_super_user(username, email, password):
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_superuser(username, email, password)
        user.save()
        print(f'Пользователь {username} успешно создан.')
    else:
        print(f'Пользователь с именем {username} уже существует.')


def main():
    parser = argparse.ArgumentParser(description='Создание super_user в Django')
    parser.add_argument('--user', required=True, help='User')
    parser.add_argument('--password', required=True, help='Password')
    parser.add_argument('--email', required=True, help='Email')
    args = parser.parse_args()

    create_super_user(args.user, args.email, args.password)


if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     create_super_user('user', 'newuser@example.com', 'user12345')
