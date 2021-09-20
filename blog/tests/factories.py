import factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
import datetime

from blog.models import Post

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = 'Testando o factoryboy'
    text = 'parece que funcionou'
    created_date = datetime.date.today()
    published_date = datetime.date.today()


