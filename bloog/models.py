from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


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

#
# timezone.timedelta

class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class ArticleManager(models.Manager):
    def count(self):
        return len(self.all())

    def published(self):
        return self.filter(is_published=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=False)
    title = models.CharField(max_length=70)
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=timezone.now)
    is_published = models.BooleanField(default=False)
    # myfile = models.BinaryField(null=True)
    myfile = models.FileField(upload_to='blogfiles', null=True)
    objects = ArticleManager()
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ('-updated', '-created')
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def __str__(self):
        return f"{self.title} - {self.body[:30]} - Updated at: {self.updated.strftime('%Y-%m-%d %H:%M:%S')}"
