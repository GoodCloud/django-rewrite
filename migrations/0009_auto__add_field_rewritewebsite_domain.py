# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'RewriteWebsite.domain'
        db.add_column('rewrite_rewritewebsite', 'domain', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'RewriteWebsite.domain'
        db.delete_column('rewrite_rewritewebsite', 'domain')


    models = {
        'rewrite.rewriteblog': {
            'Meta': {'object_name': 'RewriteBlog'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteTemplate']"}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteWebsite']"})
        },
        'rewrite.rewriteblogpost': {
            'Meta': {'object_name': 'RewriteBlogPost'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteBlog']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': 'u\'<p>This is some sample content so that you can see\\nwhat it looks like.  Please replace it!  Often, when designers are filling out \\nsample content, they use a passage from an obscure latin book, known as "lorem \\nipsum" text. It goes a little something like this:</p>\\n\\n<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>\\n\\n<p>If you also found that riveting, design may be for you. If not, it may still\\nbe for you. Many people find the next paragraphs better. Check it out:</p>\\n\\n<p>\\nSed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. \\nPhasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse \\ndictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent \\nid metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et \\njusto dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum \\nlaoreet.</p>\\n\\n<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget \\nin metus. In pellentesque faucibus vestibulum. Nulla at nulla justo, eget luctus \\ntortor. Nulla facilisi. Duis aliquet egestas purus in blandit. Curabitur \\nvulputate, ligula lacinia scelerisque tempor, lacus lacus ornare ante, ac egestas \\nest urna sit amet arcu. Class aptent taciti sociosqu ad litora torquent per \\nconubia nostra, per inceptos himenaeos. Sed molestie augue sit amet leo \\nconsequat posuere. Vestibulum ante ipsum primis.</p> \'', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '156', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '69', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteWebsite']"})
        },
        'rewrite.rewritepage': {
            'Meta': {'ordering': "('order', 'title')", 'object_name': 'RewritePage'},
            'content': ('django.db.models.fields.TextField', [], {'default': 'u\'<p>This is some sample content so that you can see\\nwhat it looks like.  Please replace it!  Often, when designers are filling out \\nsample content, they use a passage from an obscure latin book, known as "lorem \\nipsum" text. It goes a little something like this:</p>\\n\\n<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\\ntempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\\nquis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\\nconsequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\\ncillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\\nproident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>\\n\\n<p>If you also found that riveting, design may be for you. If not, it may still\\nbe for you. Many people find the next paragraphs better. Check it out:</p>\\n\\n<p>\\nSed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. \\nPhasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse \\ndictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent \\nid metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et \\njusto dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum \\nlaoreet.</p>\\n\\n<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget \\nin metus. In pellentesque faucibus vestibulum. Nulla at nulla justo, eget luctus \\ntortor. Nulla facilisi. Duis aliquet egestas purus in blandit. Curabitur \\nvulputate, ligula lacinia scelerisque tempor, lacus lacus ornare ante, ac egestas \\nest urna sit amet arcu. Class aptent taciti sociosqu ad litora torquent per \\nconubia nostra, per inceptos himenaeos. Sed molestie augue sit amet leo \\nconsequat posuere. Vestibulum ante ipsum primis.</p> \'', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '156', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'nav_link_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteSection']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteTemplate']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '69', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteWebsite']"})
        },
        'rewrite.rewritesection': {
            'Meta': {'ordering': "('order', 'name')", 'object_name': 'RewriteSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteWebsite']"})
        },
        'rewrite.rewritetemplate': {
            'Meta': {'ordering': "('name',)", 'object_name': 'RewriteTemplate'},
            'extra_head_html': ('django.db.models.fields.TextField', [], {'default': "'<!-- Enter any JavaScript or CSS that should be in the page <HEAD> here. -->'", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'page_header_html': ('django.db.models.fields.TextField', [], {'default': "'<!-- Enter any HTML that should show above the navigation (like a page header) here. -->'", 'null': 'True', 'blank': 'True'}),
            'post_content_html': ('django.db.models.fields.TextField', [], {'default': "'<!-- Type any HTML that goes after the content here -->'", 'null': 'True', 'blank': 'True'}),
            'pre_content_html': ('django.db.models.fields.TextField', [], {'default': "'<!-- Enter any HTML that goes before the content here -->'", 'null': 'True', 'blank': 'True'}),
            'show_main_nav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_section_nav': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rewrite.RewriteWebsite']"})
        },
        'rewrite.rewritewebsite': {
            'Meta': {'object_name': 'RewriteWebsite'},
            'blog_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rewrite']
