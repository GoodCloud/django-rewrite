#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django-Selector is a custom url pattern parser for Django whose API is based on
`Luke Arno's Selector <http://lukearno.com/projects/selector/>`_ for WSGI.  It
is designed to simplify the writing and reading of url patterns by providing
recipes for frequently used patterns.  Django-Selector's parser ignores classic
regex based url patterns, so if you require the flexibility of regexes you
needn't jump through registration hoops for a one-off url pattern. Using these
named patterns in your urls.py clarifies *what* they are matching as well as
*how* they are matching it::

    patterns('foo.views',
        (r'^/(?P<name>[a-zA-Z0-9\-]+)/(?P<foos>\d*.?\d+)/$', 'index', {}, 'foo-index'))

becomes::

    parser.patterns('foo.views',
        (r'/{name:slug}/{foos:number}/', 'index', {}, 'foo-index'))
"""

import re
from django.conf.urls.defaults import url as django_url
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver

import calendar

__all__ = ['pattern_types', 'Parser']

pattern_types = {
    'word'      : r'\w+',
    'alpha'     : r'[a-zA-Z]+',
    'digits'    : r'\d+',
    'number'    : r'\d*\.?\d+',
    'chunk'     : r'[^/^.]+',
    'segment'   : r'[^/]+',
    'any'       : r'.*',
    # common url pieces
    'year'      : r'\d{4}',
    'month'     : r'(%s)' % '|'.join(calendar.month_abbr[1:]),
    'day'       : r'\d{1,2}',
    'slug'      : r'[a-zA-Z0-9\-]+',
}

pattern_re = re.compile(r'{(?P<name>\w+):?(?P<pattern>\w+)?}')
re_template = r'(?P<%s>%s)'
re_findstr  = r'{%(name)s:%(pattern)s}'

class Parser:
    """A parser that can process url patterns with named patterns in them."""
    def __init__(self, **extra_patterns):
        self.pattern_types = pattern_types.copy()
        for key, val in extra_patterns.iteritems():
            self.pattern_types[key] = val

    def register(self, name, regex):
        """Registers a new pattern or overrides an old one."""
        # sanity check
        re.compile(regex)
        self.pattern_types[name] = regex
        return True

    def parse_pattern(self, pat):
        """Parses a pattern to a full regex. Surrounds pattern w/ ^ & $, and
        replaces the embedded patterns with regexes."""
        matches = [m.groupdict() for m in pattern_re.finditer(pat)]
        for match in matches:
            # {'pattern': p, 'name': n}
            p, n = match['pattern'], match['name']
            if p is None:
                p = 'segment'
                findstr = '{%s}' % n
            else:
                findstr = re_findstr % match
            replacement = re_template % (n, self.pattern_types[p])
            pat = pat.replace(findstr, replacement)
        pat = ('^%s$' % pat) if not pat.endswith('!') else ('^%s' % pat[:-1])
        return pat

    def patterns(self, prefix, *args):
        """A replacement 'patterns' that understands named patterns."""
        pattern_list = []
        for t in args:
            if isinstance(t, (list, tuple)):
                t = self.url(prefix=prefix, *t)
            elif isinstance(t, RegexURLPattern):
                t.add_prefix(prefix)
            pattern_list.append(t)
        return pattern_list

    def url(self, regex, view, kwargs=None, name=None, prefix=''):
        """A replacement for 'url' that understands named patterns."""
        regex = self.parse_pattern(regex)
        return django_url(regex, view, kwargs, name, prefix)

