from django import forms
from rewrite.models import RewriteWebsite, RewriteTemplate, RewriteSection,  RewriteBlog, RewritePage, RewriteBlogPost

class RewriteWebsiteForm(forms.ModelForm):
    class Meta:
        model = RewriteWebsite
        fields = ( "domain", "blog_enabled",)

class RewriteSectionForm(forms.ModelForm):
    class Meta:
        model = RewriteSection
        fields = ("name", )

class RewriteTemplateForm(forms.ModelForm):
    class Meta:
        model = RewriteTemplate
        fields = ("name", "show_main_nav", "show_section_nav",
                  "extra_head_html", "page_header_html", 
                  "pre_content_html", "post_content_html",
                  )

class RewriteNewTemplateForm(forms.ModelForm):
    class Meta:
        model = RewriteTemplate
        fields = ("name",)

class RewriteBlogForm(forms.ModelForm):
    class Meta:
        model = RewriteBlog
        fields = ("template", )


class RewriteNewPageForm(forms.ModelForm):
    class Meta:
        model = RewritePage
        fields = ("title", "section", "template",)
    
    def __init__(self, *args, **kwargs):
        super(RewriteNewPageForm,self).__init__(*args,**kwargs)
        self.fields["template"].choices = [f for f in self.fields["template"].choices][1:]

class RewritePageForm(RewriteNewPageForm):
    class Meta:
        model = RewritePage
        fields = ("title", "section", "nav_link_name", "description", "keywords", "template", "is_published")


class RewriteBlogPostForm(forms.ModelForm):
    class Meta:
        model = RewriteBlogPost
        fields = ("title", "description", "keywords", "is_published")

class RewriteNewBlogPostForm(forms.ModelForm):
    class Meta:
        model = RewriteBlogPost
        fields = ("title", )
