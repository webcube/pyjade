[![Build Status](https://secure.travis-ci.org/SyrusAkbary/pyjade.png)](https://secure.travis-ci.org/SyrusAkbary/pyjade)

PyJade
======

PyJade is a high performance port of Jade-lang for python, that converts any .jade source to the each Template-language (Django, Jinja2, Mako or Tornado).


UTILITIES
=========
To simply output the conversion to your console:

```console
pyjade [-c django|jinja|mako|tornado] input.jade [output.html]
```


INSTALLATION
============

First, you must do:

```console
pip install pyjade
```

Or:

```console
python setup.py install
```

Now simply **name your templates with a `.jade` extension** and this jade compiler
will do the rest.  Any templates with other extensions will not be compiled
with the pyjade compiler.


Django
------

In `settings.py`, modify `TEMPLATE_LOADERS` like:

```python
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
```

Jinja2
------

Just add `pyjade.ext.jinja.PyJadeExtension` as extension:

```python
jinja_env = Environment(extensions=['pyjade.ext.jinja.PyJadeExtension'])
```

Mako
----

Just add  `pyjade.ext.mako.preprocessor` as preprocessor:

```python
from pyjade.ext.mako import preprocessor as mako_preprocessor
mako.template.Template(jade_source,
    preprocessor=mako_preprocessor
)
```

Flask
-----

Just add  `pyjade.ext.jinja.PyJadeExtension` as extension to the environment of the app::

```python
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
```

Pyramid
-------

Adjust your "your_project/__init__.py" and add the following line somewhere to in the main() function:

```python
config.include('pyjade.ext.pyramid')
```

Tornado Templates
-----------------

Append this after importing tornado.template

```python
from tornado import template
from pyjade.ext.tornado import patch_tornado
patch_tornado()

(...)
```

Syntax
======

Exactly the same as the Jade Node.js module (except of cases, which are not implemented)
https://github.com/visionmedia/jade/blob/master/Readme.md


Example
-------

This code:

```jade
!!! 5
html(lang="en")
  head
    title= pageTitle
    script(type='text/javascript')
      if (foo) {
         bar()
      }
  body
    h1.title Jade - node template engine
    #container
      if youAreUsingJade
        p You are amazing
      else
        p Get on it!
```


Converts to:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{{pageTitle}}</title>
    <script type='text/javascript'>
      if (foo) {
         bar()
      }
    </script>
  </head>
  <body>
    <h1 class="title">Jade - node template engine</h1>
    <div id="container">
      {%if youAreUsingJade%}
        <p>You are amazing</p>
      {%else%}
        <p>Get on it!</p>
      {%endif%}
    </div>
  </body>
</html>
```

Register filters
================

If you want to register a function as a filter, you only have to
decorate the function with `pyjade.register_filter("filter_name")`

```python
import pyjade

@pyjade.register_filter('capitalize')
def capitalize(text,ast):
  return text.capitalize()
```

### Using templatetags (and any feature of the compiled-to language)

*Using Django and crispy-forms as an illustrative example but the information
can be generalized.*

If you need to use templatetags, you can use Jade's syntax for rendering code:

```jade
- load crispy_forms_tags
- crispy form
```

This will compile into

```html
{% load crispy_forms_tags %}
{% crispy form %}
```

If you have any trouble with this feature, or there's some feature of your
template language that is being misinterpreted when using this syntax, you
can also do something like this:

```jade
| {% load crispy_forms_tags %}
| {% crispy form %}
```

This will compile into the same Django template snippet.


**If you need to pass a bare template tag to an element to dynamically generate an HTML attribute, use `^`:**
```jinja
<h2 class="no_entries" {% add_link "blog" "blogentry" %} >{% trans 'No Blog Entries Found.' %}</h2>
```
is written like this in jade:
```jade
h2(class="no_entries", ^='{% add_link "blog" "blogentry" %}')
  - trans 'No Blog Entries Found.'
```
Multiple attributes for an HTML tag can be separated by commas or newlines. Using `^` as the attribute name will cause the value to be passed through to the intermediate template unaltered.

TESTING
=======

You must have `nose` package installed.
You can do the tests with

```console
./test.sh
```


TODOs and BUGS
==============
See: http://github.com/syrusakbary/pyjade/issues
