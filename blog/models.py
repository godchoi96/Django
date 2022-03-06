from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# 장고 shell에서 __의 의미
# 필드의 이름과 연산자를 구분하는 데 씀 ex) Post.objects.filter(title__contains='title') = title 필드에 title이 들어간 것만 뽑아내고 싶을 때 사용
