==================
Contribution guide
==================

If you want to contribute to this project, you are welcome to do so!

Create your own development environment
---------------------------------------
We use conda as our main packaging system, though pip works as well.

The following instructions describe how to create your development environment using conda:

#. Create a new environment:

    .. code-block:: bash

       conda create -n {{cookiecutter.project_slug}}-dev python=3 -c https://conda.anaconda.org/conda-forge -c defaults

#. Install the dependencies:

    .. code-block:: bash

       conda install --file requirements.txt -n {{cookiecutter.project_name.replace(' ', '-')}}-dev -c https://conda.anaconda.org/conda-forge -c defaults

#. Activate your environment:

    .. code-block:: bash

        conda activate {{cookiecutter.project_name.replace(' ', '-')}}-dev

#. Install `{{cookiecutter.project_name }}` in development mode:

    .. code-block:: bash

       python setup.py develop

#. You're done!

Feature requests and feedback
-----------------------------

We would be happy to hear about your propositions and suggestions. Feel free to
`submit them as issues <https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/issues>`_ and:

* Explain in details the expected behavior.
* Keep the scope as narrow as possible.  This will make them easier to implement.


.. _reportbugs:

Bug reporting
-------------

Report bugs for `{{cookiecutter.project_name}}` in the `issue tracker <https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/issues>`_. Every filed bugs should include:

 * Your operating system name and version.
 * Any details about your local setup that might be helpful in troubleshooting, specifically:
     * the Python interpreter version,
     * installed libraries,
 * Detailed steps to reproduce the bug.

.. _fixbugs:

Bug fixing
----------

Look through the `GitHub issues for bugs <https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/issues>`_.
Talk to developers to find out how you can fix specific bugs.

Feature implementation
----------------------

Look through the `GitHub issues for enhancements <https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/type:%20enhancement>`_.

Talk to developers to find out how you can implement specific features.

Thank you!
