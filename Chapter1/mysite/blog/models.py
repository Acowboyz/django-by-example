from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    # title of blog, transfer to VARCHAR in SQL
    title = models.CharField(max_length=250)
    # a short tag, use in the URLs
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    # a ForeignKey many-to-one, a blog can only be edited by one author, but one author can edit many blog.
    author = models.ForeignKey(User,
                               related_name='blog_posts')
    # body of blog, transfer to TEXT in SQL
    body = models.TextField()
    # This is just a timezone-aware datetime.now
    publish = models.DateTimeField(default=timezone.now)
    # save the time when the blog is created
    created = models.DateTimeField(auto_now_add=True)
    # save the time when the blog is updated
    updated = models.DateTimeField(auto_now=True)
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#choices
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    # The default manager.
    objects = models.Manager()
    # Our custom manager.
    published = PublishedManager()

    # return the data by descent ordering
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # strftime : use to make sure 01, 02, 03 in month and day
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])


