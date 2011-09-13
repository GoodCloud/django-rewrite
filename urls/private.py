from django.conf.urls.defaults import *
from rewrite.views.private import RewritePrivateViews
from django.contrib.auth.decorators import login_required

# I like pretty non-regex URL patterns.
from rewrite.libs import dselector
parser = dselector.Parser()
url = parser.url

# Instantiate the views class
private_views = RewritePrivateViews()

# Define the URLs as a method, so the views class can be subclassed, and added as desired
def private_url_patterns(view_class):
    return ('',
        url(r'$',                                    login_required(view_class.pages),                       name="manage_home"                  ),
        url(r'pages$',                               login_required(view_class.pages),                       name="manage_pages"                 ),
        url(r'templates$',                           login_required(view_class.templates),                   name="manage_templates"             ),
        url(r'blog$',                                login_required(view_class.blog),                        name="manage_blog"                  ),
        url(r'settings$',                            login_required(view_class.settings),                    name="manage_settings"              ),
        url(r'save-page/{page_id:digits}$',          login_required(view_class.save_page),                   name="save_page"                    ),
        url(r'save-post/{post_id:digits}$',          login_required(view_class.save_post),                   name="save_blog_post"               ),
        url(r'new-page$',                            login_required(view_class.new_page),                    name="new_page"                     ),
        url(r'new-section$',                         login_required(view_class.new_section),                 name="new_section"                  ),
        url(r'new-template$',                        login_required(view_class.new_template),                name="new_template"                 ),
        url(r'edit-template/{template_id:digits}$',  login_required(view_class.edit_template),               name="edit_template"                ),
        url(r'new-blog-post$',                       login_required(view_class.new_blog_post),               name="new_blog_post"                ),
        url(r'delete-page/{page_id:digits}$',        login_required(view_class.delete_page),                 name="delete_page"                  ),
        url(r'delete-post/{post_id:digits}$',        login_required(view_class.delete_post),                 name="delete_post"                  ),
        url(r'delete-template/{template_id:digits}$',login_required(view_class.delete_template),             name="delete_template"              ),
        url(r'save-order$',                          login_required(view_class.save_page_and_section_order), name="save_page_and_section_order"  ),
    )

# Acually set the URL patterns. 
urlpatterns = parser.patterns(*private_url_patterns(private_views))

