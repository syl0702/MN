from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    # movie_set =
    # movies


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor, related_name='movies')
    # related_name : 기본적으로 관계 설정하는 위치(Movie)의 
    #                반대편 모델(Actor)에 생기는 기본 칼럼 이름 (move_set)
    #                을 movies로 변경