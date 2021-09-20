#export DJANGO_SETTINGS_MODULE=mysite.settings no terminal
#py.test blog --ds=mysite.settings -s  -vvv

import datetime
import factory
import pytest

from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

from blog.models import Post
from blog.tests.factories import PostFactory, UserFactory
from blog import urls

#from django.contrib.auth.models import User


@pytest.mark.django_db
class TestPostViewSet:
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse_lazy('blog:post_list')

        posts = [('bru1', 'teste1','texto1',datetime.date.today(),datetime.date.today()), 
                ('bru2', 'teste2','texto2',datetime.date.today(),datetime.date.today()),
                ('bru3', 'teste3','texto3',datetime.date.today(),datetime.date.today())]

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
        #import ipdb; ipdb.set_trace();
        assert response.content.decode('utf-8').count('/post/') == Post.objects.count()
        assert response.status_code == status.HTTP_200_OK
