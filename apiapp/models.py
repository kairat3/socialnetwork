from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField('auth.User', default='')

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return f'{self.owner}-->{self.title}-->{self.like}'

#
# class LikeDislike(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likedislike')
#     like = models.BooleanField(default=False)
#     dislike = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.user}-->{self.like}, {self.dislike}'
