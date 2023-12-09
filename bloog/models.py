from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# models.cascade +> abshary
# models.set_null => null = true => vaghti on model hazf she bejaye on user/object null tarif mishe
# blank = true => mitonim to panel modiriat ye field ro optional konim.
# models.set_default, default=1  => vaghti useri ro pak mikonim kole article haye oon user be user1 montaghel mishe
# models.protect => hefazat mikone az user az tarighe article haei ke dare va nemizare user delete she ta vaghti ke article ha pak nashode
# cascade
# set_null

# protect
# set default

# do_nothing

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.body[:30]} - Updated at: {self.updated.strftime('%Y-%m-%d %H:%M:%S')}"
