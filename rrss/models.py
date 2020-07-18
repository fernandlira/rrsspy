from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=False)
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"Comentario de {self.user.username} en el post de {self.post.user}"

class Follow(models.Model):
    id = models.AutoField(primary_key=True)
    following_id = models.ManyToManyField("auth.User", related_name="follower")
    followed_id = models.ManyToManyField("auth.User", related_name="followed")


