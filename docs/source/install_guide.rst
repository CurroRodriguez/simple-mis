smis Installation Guide
========================================================================================================================

The smis library is provides as |python|_ package at the |pypi|_ and as source code, which can be obtained from its
|repo|_. The following sections describe the requirements and installation process of the library.


Software Requirements
------------------------------------------------------------------------------------------------------------------------

The library is currently implemented using |python|_ 2.7.x, and it is being tested using that version. It may work under
|python|_ 3.x, but I haven't tested the functionality. If you decided to use the source version of the library,
downloaded from its |repo|_, you will have to use |python|_ 2.7.x to insure all the requirements can be satisfied in
your environment for development.

Due to some security restriction accessing the |mis|, the minimum version of |python|_ required is 2.7.9. This is due
to the fact that the |mis| requires secure requests using the TLS 1.2 protocol, which is supported out of the box by
|python|_ 2.7.9 or higher.

|python|_ 2.7.9 or higher also comes pre-packaged with ``pip``, which allows to install the library from |pypi|_,
which is the recommended procedure.


..  _access-requirements:

Access Requirements
------------------------------------------------------------------------------------------------------------------------

In order to access the |mis|, you need to request a consumer key and secret that will enable your application to access
the service. You can request the consumer key and secret by contacting Autodesk A.D.N.


Installing the Library using PIP
------------------------------------------------------------------------------------------------------------------------

The installation using ``pip`` through |pypi|_ is identical to other python packages. The library will be installed into
your ``site-packages`` folder and will become available to your |python|_ environment::

    > pip install smis

..  note::

    I prefer and recommend to create a virtual environment for each application I work in |python|_, that way, I don't
    clutter the global |python|_ environment. You can create a virtual environment for your ``smis`` applications by
    following the instructions in the `virtualenv`_ documentation site.


Downloading the Source Code
------------------------------------------------------------------------------------------------------------------------

If you plan to contribute or if you would like to checkout the code, you can get the library source from its |repo|_.
Once you download the source to your machine, you will need to install all the required packages to insure everything
is setup correctly::

    > git clone https://github.com/CurroRodriguez/smis-python
    > pip install -r requirements.txt

To insure you have the project setup correctly, you can execute all the tests, and if no errors are found, then your
environment has been setup correctly (see notes about :ref:`setting-credentials`)::

    # Executing the unit tests.
    > nosetests ./tests/unit

    # Executing acceptance tests.
    > behave ./tests/acceptance


..  _setting-credentials:

Setting Up Credentials
------------------------------------------------------------------------------------------------------------------------

To contribute to the source, you need to insure that all the test automation is working; therefore, you need to run
the tests. There are two test harness: a unit test harness which verifies the low-level implementation of the library
and that can be executed without credentials; and an acceptance test harness that performs calls into the live service
to insure the library functionality works as expected. For the later, you need to setup your credentials.

There are two sets of credentials required for any application to be able to access the service. First, you need to
request a consumer key and secret unique to each application you intend to develop. This includes the ability to run
the acceptance tests (see :ref:`access-requirements`). You also need an active user in |A360|_ because all requests to
|mis| are performed on behalf of a user.

Once you have both sets of credentials you can create a ``smis.txt`` file in the user directory in your system. The
file uses a standard ``.ini`` format for the parameters::

    [smis]
    consumer_key=<replace with your consumer key>
    consumer_secret=<replace with your consumer secret>
    user_name=<replace with your user name usually your email>
    password=<replace with your password>

The acceptance test harness will load your credentials from this file, and will allow you run the automation.

..

    Links


.. _virtualenv: https://virtualenv.pypa.io/en/latest/