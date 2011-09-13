from django.utils.translation import ugettext as _

DEFAULT_CONTENT_FILLER = _("""<p>This is some sample content so that you can see
what it looks like.  Please replace it!  Often, when designers are filling out 
sample content, they use a passage from an obscure latin book, known as "lorem 
ipsum" text. It goes a little something like this:</p>

<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

<p>If you also found that riveting, design may be for you. If not, it may still
be for you. Many people find the next paragraphs better. Check it out:</p>

<p>
Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. 
Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse 
dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent 
id metus massa, ut blandit odio. Proin quis tortor orci. Etiam at risus et 
justo dignissim congue. Donec congue lacinia dui, a porttitor lectus condimentum 
laoreet.</p>

<p>Nunc eu ullamcorper orci. Quisque eget odio ac lectus vestibulum faucibus eget 
in metus. In pellentesque faucibus vestibulum. Nulla at nulla justo, eget luctus 
tortor. Nulla facilisi. Duis aliquet egestas purus in blandit. Curabitur 
vulputate, ligula lacinia scelerisque tempor, lacus lacus ornare ante, ac egestas 
est urna sit amet arcu. Class aptent taciti sociosqu ad litora torquent per 
conubia nostra, per inceptos himenaeos. Sed molestie augue sit amet leo 
consequat posuere. Vestibulum ante ipsum primis.</p> """)


class ContentNotFound(Exception):
    pass