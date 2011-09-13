# encoding: utf-8
import time
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.defaultfilters import slugify


class RewriteTestAbstractions(object):

    def _private_urlify(self, url):
        return "http://test.localhost:%s%s" % (settings.LIVE_SERVER_PORT, url)
    
    def _open_private_url(self, url):
        sel = self.selenium
        sel.open(self._private_urlify(url))
        sel.wait_for_page_to_load("30000")

    def _public_urlify(self, url):
        return "http://localhost:%s%s" % (settings.LIVE_SERVER_PORT, url)
    
    def _open_public_url(self, url):
        sel = self.selenium
        sel.open(self._public_urlify(url))
        sel.wait_for_page_to_load("30000")

    def type_into_codemirror(self, css_selector, string):
        sel = self.selenium
        sel.get_eval("this.browserbot.getCurrentWindow().rewrite.editor.state.codeMirrorInstances['%s'].setValue('%s')" % (css_selector, string))

    def get_to_management_console(self, username="admin", password="admin"):
        sel = self.selenium
        self._open_private_url(reverse("rewrite:manage_home"))
        if sel.is_element_present("css=input[value=Log In]") or sel.is_element_present("css=input[value=Log in]"):
            sel.type("css=input[name=username]",username)
            sel.type("css=input[name=password]",password)
            sel.click("css=input[type=submit]")
            sel.wait_for_page_to_load("30000")

    def open_page_publicly(self, name=None, section=None):
        if not name or not section:
            raise Exception, "Missing page name or section"
        else:
            return self._open_public_url("/%s/%s" %(slugify(section),slugify(name)))

    
    def assert_in_the_management_console(self):
        sel = self.selenium
        assert sel.is_text_present("Website Manager")

    def get_to_manage_pages(self):
        self.get_to_management_console()

    def get_to_manage_templates(self):
        sel = self.selenium
        self.get_to_management_console()
        sel.click("link=Templates")
        sel.wait_for_page_to_load("30000")
        self.assert_on_the_templates_list()

    def assert_on_the_templates_list(self):
        sel = self.selenium
        assert sel.is_text_present("Click on a template name to edit.")

    def edit_template_number(self, number):
        sel = self.selenium
        sel.click("css=template:nth(%s) a" % number)
        sel.wait_for_page_to_load("30000")

    def save_template_changes(self):
        sel = self.selenium
        sel.click("css=#id_save_template_changes")
        sel.wait_for_page_to_load("30000")
        assert sel.is_text_present("Changes Saved.")

    def create_a_section(self, name="Section One"):
        sel = self.selenium
        self.get_to_manage_pages()
        sel.click("css=.new_section_link")
        sel.type("css=.new_section_form #id_name", name)
        sel.click("css=.new_section_form input[type=submit]")
        sel.wait_for_page_to_load("30000")
        assert sel.is_element_present("css=section")
        assert sel.is_text_present(name)


    def create_a_page(self, name="Test Page", section_number=0):
        sel = self.selenium
        self.get_to_manage_pages()
        sel.click("css=.new_page_link:nth(%s)" % section_number)
        sel.type("css=.new_page_form:nth(%s) #id_title" % section_number, name)
        sel.click("css=.new_page_form:nth(%s) input[type=submit]" % section_number)
        sel.wait_for_page_to_load("30000")
        assert sel.is_element_present("css=section .page")
        assert sel.is_text_present(name)


    def create_a_template(self, name="Test Template"):
        sel = self.selenium
        self.get_to_manage_pages()
        self.get_to_manage_templates()
        assert not sel.is_element_present("css=templates template:nth(1)")
        sel.click("css=.new_template_link" )
        sel.type("css=.new_template_form #id_name", name)
        sel.click("css=.new_template_form input[type=submit]" )
        sel.wait_for_page_to_load("30000")
        assert sel.is_element_present("css=templates template:nth(1)")
        assert sel.is_text_present(name)

    def start_page_or_post_editing(self):
        sel = self.selenium
        sel.click("css=.edit_link")
        time.sleep(0.25)
        assert sel.is_element_present("css=.save_link")

    def set_page_content(self, content="Test content"):
        self.type_into_codemirror("rewrite_editable_body", content)

    def save_page_or_post(self):
        sel = self.selenium
        sel.click("css=.save_link")
        time.sleep(2)
        assert sel.is_element_present("css=.edit_link")

        
        
