=============================
Cookiecutter Template
=============================

A `Cookiecutter`_ template for DS projects.

.. contents:: Table of Contents
   :depth: 2

Requirements
============
* Python >= 3.7
* PyTorch >= 1.1
* Tensorboard >= 1.4

Features
========
* Clear folder structure which is suitable for many machine learning projects.
* Runs are configured via ``.yml`` files allowing for easy experimentation.
* Checkpoint saving and resuming.
* Dagster Integration

Usage
=====

.. code::

    $ pip install cookiecutter
    $ cookiecutter .
    $ cd path/to/repo

A template project has now been created! 

.. code::

    $ make env
    $ conda activate <your-project-name>
    $ make train

Custom Defaults
===============
If you fork this repo, you can modify ``cookiecutter.json`` to provide personalised defaults eg.
name, email, username, etc.

Acknowledgements
================
This template was based on `DS Template https://github.com/drivendata/cookiecutter-data-science/>`_.
