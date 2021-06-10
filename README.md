Hello-World
======

Pre-Rquisite : 

 * Python3
 * pip
 
Install
-------

    # clone the repository
    $ git clone https://github.com/shariqmahmood21/hello-world.git
    $ cd hello-world
    
Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install Flask & Pytest::

    $ pip install -r requirements.txt 


Run
---

::

    $ export FLASK_APP=app
    $ export FLASK_ENV=development
    $ export FLASK_DEBUG=1 #Run this to enable DEBUG
    $ flask run



Or on Windows cmd::

    > set FLASK_APP=flaskr
    > set FLASK_ENV=development
    > set FLASK_DEBUG=1 #Run this to enable DEBUG
    > flask run

Validation
---------- 
* To test GET: 
    > Open http://127.0.0.1:5000 in a browser.
* To test GET + Accept Header:
    > Open Terminal and paste
   
      curl -v  http://127.0.0.1:5000/ -H "X-accept-header: application/json" 
* To test POST:
    > Open Terminal and paste
   
      curl -X POST  http://127.0.0.1:5000/ 
            

Test
----
To execute the unit test cases.
::

    $ pytest -v