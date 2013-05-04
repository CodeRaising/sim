===============================
SIM - seed inventory management
===============================

A project created at CodeRaising (May 2013).

To set up the SIM project on your computer, follow these steps:

#. Install system dependencies
#. Create your working environment
#. Install additional dependencies
#. Use the Django admin to create the project

Install system dependencies
===========================

SIM is built using Django, a Python-based web application framework. In order to use Django, you need to have Python installed on your computer. If you're on a Mac, you already have it installed, but you might need to install XCode to get GCC compiler and make utilities.

If you want to contribute to the project, you will also need to have a Git client installed, which is used to push code changes to Github.

Follow these instructions_ for getting Python and Git installed on your computer. 

.. _instructions: https://openhatch.org/wiki/Django_for_Designers/Laptop_setup

Working Environment
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to seperate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

To quickly get Virtualenv and virtualenvwrapper installed, check out the virtualenv-burrito_.

.. _virtualenv-burrito: https://github.com/brainsik/virtualenv-burrito

Virtualenv Only
---------------

Note: if you used virtualenv-wrapp
First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv --distribute sim-env

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.

Virtualenv with virtualenvwrapper
--------------------------

In Linux and Mac OSX, you can install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/),
which will take care of managing your virtual environments and adding the
project path to the `site-directory` for you::

    $ mkdir sim
    $ mkvirtualenv -a sim sim-dev
    $ cd sim && add2virtualenv `pwd`


Windows
----------

In Windows, or if you're not comfortable using the command line, you will need
to add a `.pth` file to the `site-packages` of your virtualenv. If you have
been following the book's example for the virtualenv directory (pg. 12), then
you will need to add a python pathfile named `_virtualenv_path_extensions.pth`
to the `site-packages`. If you have been following the book, then your
virtualenv folder will be something like::

`~/.virtualenvs/sim/lib/python2.7/site-directory/`

In the pathfile, you will want to include the following code (from
virtualenvwrapper):

    import sys; sys.__plen = len(sys.path)
    /home/<youruser>/sim/sim/
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)

Mac
---

Here are some recommendations if you're developing on a Mac.

- Github for Mac_. (nice GUI for managing your git repositories)
- Postgres.app_.  (the best database wrapped in an easily installable Mac package)
- Sublime Text 2_. (a nice text editor for Mac)

.. _Sublime Text 2: http://www.sublimetext.com/
.. _Postgres.app: http://postgresapp.com
.. _Github for Mac: http://mac.github.com/

Installation of Dependencies
=============================

First check out the code with Git::

    $ git clone git@github.com:CodeRaising/sim.git

Or if you don't have Git installed, you can download a zipfile here::

    https://github.com/CodeRaising/sim/archive/master.zip

Activate the virtualenv that you made earlier::

    $ source /path/to/sim-env

Note: your prompt should change to look like this::

    (sim-env)$

Use `local.txt` when developing locally on your computer::    

    (sim-env)$ cd sim
    (sim-env)$ pip install -r requirements/local.txt


Synchronize database
====================

The first thing we need to do is synchronize the database with the syncdb command::

    (sim-env)$ cd sim
    (sim-env)$ python manage.py syncdb
    Syncing...
    Creating tables ...
    Creating table auth_permission
    Creating table auth_group_permissions
    Creating table auth_group
    Creating table auth_user_groups
    Creating table auth_user_user_permissions
    Creating table auth_user
    Creating table django_content_type
    Creating table django_session
    Creating table django_site
    Creating table django_admin_log
    Creating table south_migrationhistory

    You just installed Django's auth system, which means you don't have any superusers defined.
    Would you like to create one now? (yes/no): 
    Username (leave blank to use 'nateaune'): admin
    Email address: user@domain.com
    Password: 
    Password (again): 
    Superuser created successfully.
    Installing custom SQL ...
    Installing indexes ...
    Installed 0 object(s) from 0 fixture(s)

    Synced:
     > django.contrib.auth
     > django.contrib.contenttypes
     > django.contrib.sessions
     > django.contrib.sites
     > django.contrib.messages
     > django.contrib.staticfiles
     > django.contrib.admin
     > south
     > debug_toolbar

    Not synced (use migrations):
     - 
    (use ./manage.py migrate to migrate these)

Migrate the database
====================

Above, the syncdb command is telling us that we need to run `manage.py migrate` since we're using South to manage our database schema migrations::

    (sim-env)$ python manage.py migrate

Start the Django server
=======================

Now we'll start up the Django server with `manage.py runserver`::

    (sim-env)$ python manage.py runserver

You can then view the site by going to http://localhost:8000 in your browser.

Contributing
============

We will use the ThinkUp contributor workflow for contributions.
http://www.thinkupapp.com/docs/contribute/developers/devfromsource.html

Acknowledgements
================

    - All of the contributors_ to this project.

.. _contributors: https://github.com/coderaising/sim/blob/master/CONTRIBUTORS.txt
