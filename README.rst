googlefonts-markup
==================

.. warning:: This is alpha library

Overview
--------

This is small utility to handle specs of Google Fonts in my products.

Usage
-----

.. note:: WIP

.. code-block:: python

   >>> from googlefonts_markup import Font
   >>> noto_sans_jp = Font(family_name="Noto Sans JP")
   >>> noto_sans_jp.css_url()
   https://fonts.googleapis.com/css2?family=Noto+Sans+JP
   >>> noto_sans_jp.css_tag()
   <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP" rel="stylesheet">

Installation
------------

.. code-block:: console

   pip install git+https://github.com/attakei-lab/googlefonts-markup
