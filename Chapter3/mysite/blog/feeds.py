from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
# from django.template.defaultfilters import truncatewords_html

from .models import Post


# import markdown


class LastPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        # return truncatewords_html(markdown.markdown(item.body), 30)
        return truncatewords(item.body, 30)
