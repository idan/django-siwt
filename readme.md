Django-SIWT (Sign In With Twitter)
==================================

A reusable app which makes it easy to use Twitter's "[Sign In With Twitter][siwt]" authentication mechanism.

  [siwt]: http://apiwiki.twitter.com/Sign-in-with-Twitter


Usage
-----

  1. Put the `django_siwt` folder somewhere on your pythonpath.
  1. Add `django_siwt` to your `INSTALLED_APPS`. There are no models, ergo there's no need for syncdb.
  1. Make sure to set `CONSUMER_KEY` and `CONSUMER_SECRET` in your `settings.py`.  
  1. Include `django_siwt`'s urls somewhere convenient (say, your project's urls.py).
  1. Add some links to `django_siwt`'s `signin`/`signout` views from within your templates. Easily accomplished using the `url` tag: `{% url siwt_signin %}` and `{% url siwt_signout %}`.

Take a look in `utils.py` for a few more tweakable knobs.


History
-------

This project is a cleaned-up, reusable-app-ified version of henriklied's [django-twitter-oauth](http://github.com/henriklied/django-twitter-oauth). That application used the standard authentication flow and not "Sign In With Twitter", though the distinction appears largely academic as both seem to operate fine. I wanted to use the sanctioned way though, hence the modifications.

License
-------

This code is yours to use and modify according to the terms of the BSD License, the full text of which is available in LICENSE.txt or at http://opensource.org/licenses/bsd-license.php



  