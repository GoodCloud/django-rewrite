from django.conf.urls.defaults import *
from rewrite.views.public import RewritePublicViews

# I like pretty non-regex URL patterns.
from rewrite.libs import dselector
parser = dselector.Parser()
url = parser.url

# Instantiate the views class
public_views = RewritePublicViews()

# Define the URLs as a method, so the views class can be subclassed, and added as desired
def public_url_patterns(view_class):
    return ('',
        url(r'^blog/$',                                  view_class.blog_home,    name="blog_home"),
        url(r'^blog/{entry_slug:slug}$',                 view_class.blog_entry,   name="blog_entry"),
        url(r'^{section:slug}$',                         view_class.page,         name="section"),
        url(r'^{section:slug}/{page_name:slug}$',        view_class.page,         name="page"),
    )

# Acually set the URL patterns. 
urlpatterns = parser.patterns(*public_url_patterns(public_views))
