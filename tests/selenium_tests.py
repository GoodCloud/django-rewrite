# encoding: utf-8
from qi_toolkit.selenium_test_case import QiConservativeSeleniumTestCase
import time
from rewrite.tests.selenium_abstractions import RewriteTestAbstractions
    
# class TestRewriteManagement(QiConservativeSeleniumTestCase, RewriteTestAbstractions):

#     def setUp(self, *args, **kwargs):
#         self.verificationErrors = []

from accounts.tests.selenium_abstractions import AccountTestAbstractions
class TestRewriteManagement(QiConservativeSeleniumTestCase, RewriteTestAbstractions, AccountTestAbstractions):
    
    def setUp(self, *args, **kwargs):
        self.account = self.setup_for_logged_in()

    def test_management_console_loads(self):
        self.get_to_management_console()
        self.assert_in_the_management_console()

    def test_creating_a_section(self):
        self.create_a_section(name="My Test Section")

    def test_creating_a_page(self):
        self.create_a_section()
        self.create_a_page(name="My Test Page")
        
    def test_that_a_created_page_is_viewable_to_an_editor(self):
        sel = self.selenium
        self.create_a_section(name="Section To Test")
        self.create_a_page(name="My Test Page")
        self.open_page_publicly(name="My Test Page", section="Section To Test")
        self.assertEqual(sel.get_title(),"My Test Page")

    def test_reordering_a_page_works_and_updates_the_nav(self):
        sel = self.selenium
        self.create_a_section()
        self.create_a_page(name="My Test Page 1")
        self.create_a_page(name="My Test Page 2")
        
        # Baseline
        self.open_page_publicly(name="My Test Page 1", section="Section To Test")        
        self.assertEqual(sel.get_text("css=section_nav a:nth(0)"), "My Test Page 1")
        self.assertEqual(sel.get_text("css=section_nav a:nth(1)"), "My Test Page 2")

        # D-N-D
        self.get_to_management_console()
        self.assert_in_the_management_console()
        
        assert not sel.is_text_present("Saved")
        sel.drag_and_drop_to_object("css=.connectedPages .list_block:nth(0)", "css=.new_page_link:nth(0)")
        time.sleep(2)
        assert sel.is_text_present("Saved")

        # Make sure it changed.
        self.open_page_publicly(name="My Test Page 1", section="Section To Test")        
        self.assertEqual(sel.get_text("css=section_nav a:nth(0)"), "My Test Page 2")
        self.assertEqual(sel.get_text("css=section_nav a:nth(1)"), "My Test Page 1")

    def test_reordering_a_section_works_and_updates_the_nav(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_section(name="Section 2")
        self.create_a_page(name="My Test Page 1")
        self.create_a_page(name="My Test Page 1", section_number=1)
        
        # Baseline
        self.open_page_publicly(name="My Test Page 1", section="Section 1")        
        self.assertEqual(sel.get_text("css=main_nav a:nth(0)"), "Section 1")
        self.assertEqual(sel.get_text("css=main_nav a:nth(1)"), "Section 2")

        # D-N-D
        self.get_to_management_console()
        self.assert_in_the_management_console()
        
        assert not sel.is_text_present("Saved")
        sel.drag_and_drop_to_object("css=section:nth(0)", "css=.new_section_link")
        time.sleep(2)
        assert sel.is_text_present("Saved")

        # Make sure it changed.
        self.open_page_publicly(name="My Test Page 1", section="Section 1")        
        self.assertEqual(sel.get_text("css=main_nav a:nth(0)"), "Section 2")
        self.assertEqual(sel.get_text("css=main_nav a:nth(1)"), "Section 1")

    def test_blank_sections_dont_display_in_the_nav(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_section(name="Section 2")
        self.create_a_page(name="My Test Page 1")
        
        # Baseline
        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert sel.is_text_present("Section 1")
        assert not sel.is_text_present("Section 2")



    def test_moving_a_page_from_one_section_to_another_works(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_section(name="Section 2")
        self.create_a_page(name="My Test Page 1")
        self.create_a_page(name="My Test Page 2", section_number=1)
        
        # Baseline
        self.open_page_publicly(name="My Test Page 1", section="Section 1")        
        self.assertEqual(sel.get_text("css=section_nav a:nth(0)"), "My Test Page 1")
        assert not sel.is_element_present("css=section_nav a:nth(1)")

        # D-N-D
        self.get_to_management_console()
        self.assert_in_the_management_console()
        
        assert not sel.is_text_present("Saved")
        sel.drag_and_drop_to_object("css=section:nth(1) .connectedPages .list_block", "css=section:nth(0) .connectedPages .list_block")
        time.sleep(2)
        assert sel.is_text_present("Saved")

        # Make sure it changed.
        self.open_page_publicly(name="My Test Page 1", section="Section 1")        
        self.assertEqual(sel.get_text("css=section_nav a:nth(0)"), "My Test Page 1")
        self.assertEqual(sel.get_text("css=section_nav a:nth(1)"), "My Test Page 2")
    

    def test_disabling_the_main_nav_hides_it_from_the_page(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_section(name="Section 2")
        self.create_a_page(name="My Test Page 1")
        self.create_a_page(name="My Test Page 1", section_number=1)

        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert sel.is_text_present("Section 1")
        assert sel.is_text_present("Section 2")

        self.get_to_manage_templates()
        self.edit_template_number(0)
        sel.uncheck("css=#id_show_main_nav")
        self.save_template_changes()

        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert not sel.is_text_present("Section 1")
        assert not sel.is_text_present("Section 2")


    def test_disabling_the_section_nav_hides_it_from_the_page(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_page(name="My Test Page 1")
        self.create_a_page(name="My Test Page 2")

        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert sel.is_text_present("My Test Page 1")
        assert sel.is_text_present("My Test Page 2")

        self.get_to_manage_templates()
        self.edit_template_number(0)
        sel.uncheck("css=#id_show_section_nav")
        self.save_template_changes()

        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert not sel.is_text_present("My Test Page 2")

    def test_each_template_section_is_reflected_on_the_page(self):
        sel = self.selenium
        self.create_a_section(name="Section 1")
        self.create_a_page(name="My Test Page 1")

        # Baseline
        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        assert not sel.is_alert_present()
        assert not sel.is_text_present("Page Header")
        assert not sel.is_text_present("This is pre.")
        assert not sel.is_text_present("This is post.")

        self.get_to_manage_templates()
        self.edit_template_number(0)
        self.type_into_codemirror("id_extra_head_html", "<script>$(function(){setTimeout(function(){window.alert(\"test\");},300);});</script>")
        self.type_into_codemirror("id_page_header_html", "Page Header")
        self.type_into_codemirror("id_pre_content_html",  "This is pre.")
        self.type_into_codemirror("id_post_content_html", "This is post.")
        self.save_template_changes()

        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        time.sleep(0.3)
        assert sel.is_alert_present()
        assert sel.is_text_present("Page Header")
        assert sel.is_text_present("This is pre.")
        assert sel.is_text_present("This is post.")

    def test_creating_a_template(self):
        self.create_a_template()

    def test_editing_a_page(self):
        sel = self.selenium

        test_content = "Here's some test content"

        self.create_a_section(name="Section 1")
        self.create_a_page(name="My Test Page 1")
        self.open_page_publicly(name="My Test Page 1", section="Section 1")
        self.start_page_or_post_editing()
        self.set_page_content(test_content)
        self.save_page_or_post()
        assert sel.is_text_present(test_content)
        sel.refresh()
        assert sel.is_text_present(test_content)
        

        

class TestRewriteBlog(QiConservativeSeleniumTestCase, RewriteTestAbstractions):
    # selenium_fixtures = ["generic_tags.selenium_fixtures.json",]

    def setUp(self, *args, **kwargs):
        self.a1 = self.create_demo_site()   
        self.verificationErrors = []
    
    
class TestRewritePage(QiConservativeSeleniumTestCase, RewriteTestAbstractions):
    # selenium_fixtures = ["generic_tags.selenium_fixtures.json",]

    def setUp(self, *args, **kwargs):
        self.a1 = self.create_demo_site()   
        self.verificationErrors = []
    
    
        