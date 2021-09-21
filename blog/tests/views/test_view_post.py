#export DJANGO_SETTINGS_MODULE=mysite.settings --> no terminal caso necessário
#py.test blog --ds=mysite.settings -s  -vvv --> no terminal para rodar pytest
#import ipdb; ipdb.set_trace(); --> no código para testar partes

import factory
import pytest

from django.urls import reverse_lazy
from django.utils import timezone

from rest_framework import status
from rest_framework.test import APIClient

from blog.tests.factories import PostFactory, UserFactory
from blog.models import Post

@pytest.mark.django_db
class TestPostViewSet:
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse_lazy('blog:post_list')

        posts = [('bru1', 'title1','text1',timezone.now(),timezone.now()), 
                ('bru2', 'title2','text2',timezone.now(),timezone.now()),
                ('bru3', 'title3','text3',timezone.now(),timezone.now())]

        sequence = factory.Sequence(lambda n : n + 1)

        for post in posts:

            user = UserFactory(
                id=sequence, 
                username=post[0]
                )

            PostFactory(
                author=user,
                title=post[1],
                text=post[2],
                created_date=post[3],
                published_date=post[4]
            )

    def test_get_posts(self):
        response = self.client.get(self.list_url)

        assert response.content.decode('utf-8').count('/post/') == Post.objects.count()
        assert response.status_code == status.HTTP_200_OK

    def test_unique_titles(self):
        response = self.client.get(self.list_url)

        assert response.content.decode('utf-8').count('title1') == 1
        assert response.content.decode('utf-8').count('title2') == 1 
        assert response.content.decode('utf-8').count('title3') == 1 

    def test_unique_texts(self):
        response = self.client.get(self.list_url)

        assert response.content.decode('utf-8').count('text1') == 1 
        assert response.content.decode('utf-8').count('text2') == 1 
        assert response.content.decode('utf-8').count('text3') == 1 

