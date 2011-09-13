django-rewrite is a simple-to-use website and blog application for django.

Overview
========
Rewrite is a user-centric website and blogging application for Django.  It's designed to be simple to use. Its target audience is people and organizations who need a website, and who aren't particularly likely to know what a "CMS" is.  Editing websites and posting blog entries should be simple.  We built rewrite to make it that way.


Why another CMS/Blog?!?!?!
==========================

Don't get me wrong, there are some great CMS and Blog projects for Django out there, Django-CMS and Mezzanine chief among them.  But they're also industrial-weight solutions, requiring lots of tuning for simple setups.  They're also built around the Django admin site - which is really more of a data-editing scaffold than a true content-administration UI.  

We created django-rewrite to provide a simple website editor and blog that was a joy to use, and where users would always know what their content looked like, and how to change it.

If you have multiple, nested sections of content, please use one of the industrial solutions.  If you *need* tracebacks in your blog, please use one of the heavier blogging apps.  But for the 90% of projects that don't need those sorts of advanced features, here's something simpler.

The basic philosophy for both content editing and template editing is this: You should see, clearly, exactly what your content is going to look like.  In the editor, this means with live, proper stylesheets and formatting.  In the template editor, that means the designer sees the actual HTML - no magic substitutions or placeholder abstractions here.


Project Status
==============

Rewrite is 0.1 version complete, and working. It's currently only halfway tested, as we realized that it isn't our top business priority about two weeks out from release.  It will be picked up with renewed vigor in early 2012, most likely.  


Documentation Status
====================

Currently incomplete, but with slow but steady improvement. We're a startup, and as you might imagine, our priorities are often elsewhere.  But it is valued, we're working on it, and your suggestions and improvements are always welcome.


Dependencies
============
- Django >= 1.3
- south, if you'd like to use the migrations (we'll maintain any schema changes in it.)

For the tests:
- django_sane_testing
- qi_toolkit : Some of the tests and possibly other things depend on the helper functions in the toolkit. Long term, we'll either remove the dependency, or integrate it in a more stable/reliable way.
- maybe some other dependencies? We're using it within a pretty heavy functional testing structure, so it's possible something has been missed. Please file an issue if so. 

Installation
============
Standard stuff: 

* pip install, from here for now.  We're looking into pypi, but haven't gotten to it yet.
* Add rewrite to `INSTALLED_APPS`
* Include the public and private URLs where you want them. Default reversing assumes the app names are "website" for public and "rewrite" for private.
* `./manage.py syncdb`
* `./manage.py migrate`
* `./manage.py collectstatic` (before deploying)

Usage
=====

Add sections and pages via the management console.  Drag/drop to reorder.

To edit a page, visit it logged in, and click "Edit Page".  It's now editable. Make your changes, and click "Save".  That's it. You'll notice throughout the process that it looks like you're browsing the site. That's the exactly the point.

More detailed instructions coming, but that should be enough to get you started!


Templates and Styling
=====================

CSS is good. JS is good.  You have full control of both in styling up pages.  By default, the base templates include:

* HTML5 Boilerplate
* jQuery
* jQuery UI
* 1140px templating system.

We've taken the simplest and most flexibile approach to page customization by providing a few wide-open integration points.  When editing a template, you'll see the full structure of the final page. Rewrite uses a simple, additive approach that means you can add side content, headers, footers, and pretty much whatever you'd like.  You can also disable the navigation, either via the interface, or with CSS.

Typically, the use case is that developers build out a first template or two for their clients, using their HTML skills.  There's no pretty UI editing to the template HTML, and that's by design. Knowledge of HTML isn't necessary to use the editor or the blog, but it is to write templates. We want that to be abundantly clear to users.


Advanced Integration
====================

Subclassing really is better than sliced bread, and rewrite is built around it.  You can use rewrite as a set of base classes and functionality, and extend to integrate with your particular needs.

### Changing the templates 

* Standard django template stuff applies. Make a `/rewrite` folder in your project `templates` folder, and replace any templates you'd like.

### Changing the views

* The views are class-based, so you can import the default views class, subclass, and change specific methods to meet your needs.
* The urls are also abstracted - so once you've written your own views, if you have the same url patterns, you can just pass your updated RewritePublicViews or RewritePrivateViews to the constructor, and move on.

### Changing the models

* Subclass the models
* Update the models and views to point to your new models
* Include the rewrite urls, and pass your updated class to the url builder.

