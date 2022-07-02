====
Home
====

.. pyscript-env::

   - googlefonts-markup

``googlefonts-markup`` is small utility to handle specs of `Google Fonts <https://fonts.google.com/>`_ in your products.

You can manage fonts URL by only "spec dict" not Full-URL.

Playground
==========

.. pyscript-repl::

   from googlefonts_markup import Font
   noto_sans_jp = Font(family_name="Noto Sans JP")
   noto_sans_jp.css_url()
