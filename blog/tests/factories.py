'''Factories for test'''
import factory
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog.models import Post

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    '''UserFactory for test'''

    class Meta:
        '''Setting model'''

        model = User


class PostFactory(factory.django.DjangoModelFactory):
    '''PostFactory for test'''

    class Meta:
        '''Setting model'''

        model = Post

    author = factory.SubFactory(UserFactory)
    title = 'Testando o factoryboy'
    text = 'parece que funcionou'
    created_date = timezone.now()
    published_date = timezone.now()
