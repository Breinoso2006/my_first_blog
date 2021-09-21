import factory

from django.utils import timezone
from django.contrib.auth import get_user_model

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
    created_date = timezone.now()
    published_date = timezone.now()


