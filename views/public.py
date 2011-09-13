from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from rewrite import ContentNotFound
from rewrite.models import RewritePage, RewriteSection, RewriteBlogPost, RewriteWebsite
from rewrite.forms import RewritePageForm, RewriteBlogPostForm


# Full set of public views
class RewritePublicViews(object):
    def _get_website(self, request):
        return RewriteWebsite.objects.all()[0]


    def page(self, request, section=None, page_name=None):
        website = self._get_website(request)
        if page_name:
            page = get_object_or_404(RewritePage, slug=page_name, website=website, section__slug=section)
            template = page.template
            section = page.section
        else:
            if section:
                section = get_object_or_404(RewriteSection,slug=section)
            else:
                raise ContentNotFound
        if request.user.is_authenticated():
            page_form = RewritePageForm(instance=page)
        return render_to_response("rewrite/page.html", locals(), RequestContext(request))

    def blog_home(self, request):
        website = self._get_website(request)
        template = website.blog.template
        section = website.blog_section
        blog_posts = RewriteBlogPost.objects.filter(website=website, is_published=True).all()
        return render_to_response("rewrite/blog_home.html", locals(), RequestContext(request))

    def blog_entry(self, request, entry_slug):
        website = self._get_website(request)
        post = get_object_or_404(RewriteBlogPost,slug=entry_slug, website=website)
        template = post.blog.template
        section = website.blog_section
        page = post
        if request.user.is_authenticated():
            blog_post_form = RewriteBlogPostForm(instance=post)
        return render_to_response("rewrite/blog_post.html", locals(), RequestContext(request))