Siya
=====

A live version of this repo can be found at khophi.co/siya. This application simply takes a Wikipedia URL, and returns an html page with an unescaped html of the Table of Contents of the Wikipedia URL provided. 

Currently using
===============

1. `Python <http://python.org>`_
2. `Django <http://djangoproject.com>`_ - Pyramid version will come soon
3. `Foundation Zurb CSS Framework <http://foundation.zurb.com>`_
4. `Beautiful Soup <www.crummy.com/software/BeautifulSoup/bs4/doc/>`_
5. `Coverage <http://nedbatchelder.com/code/coverage/>`_ for checking tested code coverage


Run code locally
================
To run this repo locally, please follow the steps below:

1. Clone this repository
2. You must have Python, Django, and BeautifulSoup installed. Or in the parent directory of this repo, type ``sudo pip install -r requirements.txt`` which will install latest Django and BeautifulSoup. If you wanna use the test coverage, please install the python package, called ``Coverage``
3. In parent directory of this repo, type, ``python manage.py runserver``
4. Visit localhost:8000 in your browser to see home page appear
5. Follow on screen steps to proceed.

Running Tests
=============
In the parent directory of this repo, run, ``python manage.py tests``. To see coverage report, locate htmlcov in the repo parent folder and look for ``index.html``. Open in browser to see coverage.

To run coverage code, type ``coverage run --source='.' manage.py test myapp`` when in project parent directory.

For the coverage to be reported, type ``coverage report``

Current Features
================
- The homepage shows a welcome message and present the user with an input box that asks for a Wikipedia URL and a submit button.
- When the submit button is clicked, the application, *behind the scene* downloads the HTML source code, *and stores in-memory* for the given page and scrape the table of contents for the given page. Pages without Table of Contents, an alert message displays accordingly to inform.
- The table of contents is then be posted back to the user in a new page in html format. I unescape any escaped html in this step. However, I displayed escaped TOC alongside
- The page showing the table of contents provides a ``refresh`` button that will allow the user to restart the process.

Bonus features
==============

- The application checks for user input that is not a valid Wikipedia URL and posts an error message stating this. Without even a url, form won't validate (based on basic HTML5 form validations. No server side validation done)
- In the event that a Wikipedia page has no table of contents, a suitable error message is given.
- Each view and method created for this application, has a unit test. An in-browser test via selenium is added as well. Code is tested to best of unit testing. Python module, Coverage indicates so.
- The source code is fully PEP8 compliant: https://www.python.org/dev/peps/pep-0008/. Anaconda plugin for Python used, via Sublime Text 3

Extras
======
- Styling NOT mandatory, but I added.
- Development of this app was done solely on Ubuntu 14.04 LTS
- Python version used is 2.7

What is left?
=============

1. Using Pyramid

Switch to Pyramid, when?
========================
Maximum by 27th of February.