==============
pytest-splitio
==============

.. image:: https://img.shields.io/pypi/v/pytest-splitio.svg
    :target: https://pypi.org/project/pytest-splitio
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-splitio.svg
    :target: https://pypi.org/project/pytest-splitio
    :alt: Python versions

Split.io SDK integration for e2e tests

----

Requirements
------------

* Pytest >= 5.0
* splitio_client >= 8.0

Installation
------------

You can install "pytest-splitio" via `pip`_ from `PyPI`_::

    $ pip install pytest-splitio


Usage
----------

There are two types of markers - **skipif_split_not_equal** and **skipif_split_equals**.

* This test will be skipped if 'cool-split-name' split's value is not equal to "on" value in environment

.. code-block:: python

    import pytest

    @pytest.mark.skipif_split_not_equal('cool-split-name', 'on')
    def test_m1():
        pass

* This test will be skipped if 'cool-split-name' split's value is equal to "off" value

.. code-block:: python

    import pytest

    @pytest.mark.skipif_split_equals('cool-split-name', 'off')
    def test_m2():
        pass

You can also add some logic inside your test, by checking split's treatment value

* Make sure to pass 'split' argument to your test function

.. code-block:: python

    def test_m3(split):
        split_treatment = split.get_treatment('cool-split-name')
        if split_treatment == 'on':
            print('YES!!!')

Now to Run your tests you need to specify --SPLIT-KEY argument or create an environment variable *SPLIT_KEY*,
which should be environment SDK key::

    $ python -m pytest --SPLIT-KEY="your-split-sdk-key"

Contributing
------------
Contributions are very welcome.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-splitio" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`MIT`: http://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/mikoblog/pytest-splitio/issues
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project/pytest-splitio
