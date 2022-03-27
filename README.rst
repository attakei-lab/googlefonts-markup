==================
googlefonts-markup
==================

.. warning:: This is alpha library

Overview
========

This is small utility to handle specs of Google Fonts in my products.

Usage
=====

.. note:: WIP

Simple case
-----------

.. code-block:: python

   >>> from googlefonts_markup import Font
   >>> noto_sans_jp = Font(family_name="Noto Sans JP")
   >>> noto_sans_jp.css_url()
   'https://fonts.googleapis.com/css2?family=Noto+Sans+JP'
   >>> noto_sans_jp.css_tag()
   '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP" rel="stylesheet">'

If you want only URL of CSS, use ``googlefonts_markup.shortcuts``.

.. code-block:: python

   >>> from googlefonts_markup.shortcuts import font_css_url
   >>> font_css_url("Noto Sans JP")
   'https://fonts.googleapis.com/css2?family=Noto+Sans+JP'

With italic
-----------

.. code-block:: python

   >>> from googlefonts_markup import Axis, Font
   >>> red_hat_mono = Font(family_name="Red Hat Mono", axis_list=[Axis(italic=True)])
   >>> red_hat_mono.css_url()
   'https://fonts.googleapis.com/css2?family=Red+Hat+Mono:ital,wght@1,400'

Extra attributes
----------------

.. code-block:: python

   >>> from googlefonts_markup import Font, FontSet
   >>> noto_sans_jp = Font(family_name="Noto Sans JP")
   >>> fontset = FontSet(fonts=[noto_sans_jp], display="swap")
   >>> fontset.css_url()
   'https://fonts.googleapis.com/css2?family=Noto+Sans+JP&display=swap'

Multiple fonts
--------------

.. code-block:: python

   >>> from googlefonts_markup import Font, FontSet
   >>> noto_sans_jp = Font(family_name="Noto Sans JP")
   >>> roboto_mono = Font(family_name="Roboto Mono")
   >>> fontset = FontSet(fonts=[noto_sans_jp, roboto_mono], display="swap")
   >>> fontset.css_url()
   'https://fonts.googleapis.com/css2?family=Noto+Sans+JP&family=Roboto+Mono&display=swap'

Installation
============

.. code-block:: console

   pip install git+https://github.com/attakei-lab/googlefonts-markup
