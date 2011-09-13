from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from rewrite.models import RewriteSection, RewriteBlogPost, RewriteTemplate, RewriteWebsite, RewriteBlog
from rewrite.forms import *   # I hate import * as well, but there are a *TON* of them.


# Full set of private views.  Subclass as you see fit.
class RewritePrivateViews(object):
    def _get_website(self,request):
        return RewriteWebsite.objects.all()[0]

    def _get_blog(self,request):
        return self._get_website(request).blog

    def pages(self, request):
        tab = "pages"
        website = self._get_website(request)

        sections = RewriteSection.objects.all()
        new_page_form = RewriteNewPageForm()
        new_section_form = RewriteSectionForm()
        
        return render_to_response("rewrite/manage/pages.html", locals(), RequestContext(request))

    def blog(self, request):
        tab = "blog"
        website = self._get_website(request)

        blog_posts = RewriteBlogPost.objects.all()
        blog = RewriteBlog.objects.all()[0]
        new_blog_post_form = RewriteNewBlogPostForm()
        return render_to_response("rewrite/manage/blog.html", locals(), RequestContext(request))

    def templates(self, request):
        tab = "templates"
        website = self._get_website(request)

        templates = RewriteTemplate.objects.all()
        new_template_form = RewriteNewTemplateForm()
        return render_to_response("rewrite/manage/templates.html", locals(), RequestContext(request))

    def settings(self, request):
        tab = "settings"
        website = self._get_website(request)
        blog = RewriteBlog.objects.all()[0]
        if request.method == "POST":
            blog_settings_form = RewriteBlogForm(request.POST, instance=blog)
            website_settings_form = RewriteWebsiteForm(request.POST, instance=website)    
            if blog_settings_form.is_valid() and website_settings_form.is_valid():
                blog_settings_form.save()
                website_settings_form.save()
        else:
            blog_settings_form = RewriteBlogForm(instance=blog)
            website_settings_form = RewriteWebsiteForm(instance=website)

        return render_to_response("rewrite/manage/settings.html", locals(), RequestContext(request))


    def new_page(self, request):
        website = self._get_website(request)
        if request.is_ajax():
            print "ajax"
        else:
            print "normal"
            new_page_form = RewriteNewPageForm(request.POST)
            if new_page_form.is_valid():
                p = new_page_form.save(commit=False)
                p.website = website
                p.save()
            return HttpResponseRedirect(reverse("rewrite:manage_pages"))
        

    def new_section(self, request):
        website = self._get_website(request)
        if request.is_ajax():
            print "ajax"
        else:
            print "normal"
            new_section_form = RewriteSectionForm(request.POST)
            if new_section_form.is_valid():
                s = new_section_form.save(commit=False)
                s.website = website
                s.save()
            return HttpResponseRedirect(reverse("rewrite:manage_pages"))


    def new_template(self, request):
        website = self._get_website(request)
        if request.is_ajax():
            print "ajax"
        else:
            print "normal"
            new_template_form = RewriteNewTemplateForm(request.POST)
            if new_template_form.is_valid():
                t = new_template_form.save(commit=False)
                t.website = website
                t.save()
            return HttpResponseRedirect(reverse("rewrite:manage_templates"))


    def new_blog_post(self, request):
        website = self._get_website(request)
        blog = self._get_blog(request)
        if request.is_ajax():
            print "ajax"
        else:
            print "normal"
            new_blog_post_form = RewriteNewBlogPostForm(request.POST)
            if new_blog_post_form.is_valid():
                p = new_blog_post_form.save(commit=False)
                p.website = website
                p.blog = blog
                p.save()
            return HttpResponseRedirect(reverse("rewrite:manage_blog"))

    def save_page(self, request, page_id):
        success = False
        try:
            assert request.is_ajax() and request.method == "POST" and "content" in request.POST
            website = self._get_website(request)
            page = get_object_or_404(RewritePage, pk=page_id, website=website)
            page_form = RewritePageForm(request.POST, instance=page)
            page_to_save = page_form.save(commit=False)
            page_to_save.content = request.POST["content"]
            page_to_save.save()
            success = True
        except:
            pass
            
        return HttpResponse(simplejson.dumps({"success":success}))

    def save_post(self, request, post_id):
        success = False
        try:
            assert request.is_ajax() and request.method == "POST" and "content" in request.POST
            website = self._get_website(request)
            post = get_object_or_404(RewriteBlogPost, pk=post_id, website=website)

            blog_post_form = RewriteBlogPostForm(request.POST, instance=post)
            post_to_save = blog_post_form.save(commit=False)
            post_to_save.content = request.POST["content"]
            post_to_save.save()

            success = True
        except:
            pass
            
        return HttpResponse(simplejson.dumps({"success":success}))


    def edit_template(self, request, template_id):
        tab = "templates"
        website = self._get_website(request)
        changes_saved = False
        template = get_object_or_404(RewriteTemplate, pk=template_id, website=website)
        if request.method == "POST":
            template_form = RewriteTemplateForm(request.POST, instance=template)
            if template_form.is_valid():
                template = template_form.save()
                changes_saved = True
        else:
            template_form = RewriteTemplateForm(instance=template)
        
        return render_to_response("rewrite/manage/edit_template.html", locals(), RequestContext(request))
        



    def delete_page(self, request, page_id):
        website = self._get_website(request)
        page = get_object_or_404(RewritePage, pk=page_id, website=website)
        page.delete()
        return HttpResponseRedirect(reverse("rewrite:manage_pages"))

       
    def delete_post(self, request, post_id):
        website = self._get_website(request)
        post = get_object_or_404(RewriteBlogPost, pk=post_id, website=website)
        post.delete()
        return HttpResponseRedirect(reverse("rewrite:manage_blog"))

    def delete_template(self, request, template_id):
        website = self._get_website(request)
        template = get_object_or_404(RewriteTemplate, pk=template_id, website=website)
        template.delete()
        return HttpResponseRedirect(reverse("rewrite:manage_templates"))

    def save_page_and_section_order(self, request):
        success = False
        try:
            assert request.method == "POST"
            website = self._get_website(request)
            for s in website.sections:
                s.order = request.POST.get("section_%s_order" % s.pk)
                s.save()
            
            for p in website.pages:
                p.order = request.POST.get("page_%s_order" % p.pk)
                section_pk = request.POST.get("page_%s_section" % p.pk)
                if not section_pk == p.section.pk:
                    p.section = get_object_or_404(RewriteSection,pk=section_pk, website=website)
                p.save()

        except:
            pass
        
        return HttpResponse(simplejson.dumps({"success":success}))

