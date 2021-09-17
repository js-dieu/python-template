# Contribution, getting started
Contributions are highly welcomed and appreciated.  Every little help counts,
so do not hesitate!

  * [Create your own development environment](#create-your-own-development-environment)
  * [Feature request and feebacks](#feature-request-and-feebacks)
  * [Report bugs](#report-bugs)
  * [Fix bugs](#fix-bugs)
  * [Implement features](#implement-features)
  * [Preparing Pull Requests](#preparing-pull-requests)
     + [Short version](#short-version)
     + [Long version](#long-version)


## Create your own development environment
We use conda as our main packaging system, though pip work as well. Nevertheless, 
the following instructions describe how to make your development environment using conda.

### Create a new environment:

    conda create -n {{cookiecutter.project_name.replace(' ', '-')}}-dev python={{cookiecutter.python_version_major}} -c https://conda.anaconda.org/conda-forge -c defaults
    
### Install the dependencies

    conda install --file requirements.txt -n {{cookiecutter.project_name.replace(' ', '-')}}-dev -c https://conda.anaconda.org/conda-forge -c defaults
    
### Activate your environment

    conda activate {{cookiecutter.project_name.replace(' ', '-')}}-dev

### Install {{cookiecutter.project_name.replace(' ', '-')}} in development mode

    python setup.py develop

### You're done!



## Feature request and feebacks

We'd like to hear about your propositions and suggestions. Feel free to
`submit them as issues <https://github.com/js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}/issues>`_ and:

* Explain in detail how they should work.
* Keep the scope as narrow as possible.  This will make it easier to implement.


## Report bugs
Report bugs for {{cookiecutter.project_name.replace(' ', '-')}} in the issue tracker. Every filed bugs should include:
 * Your operating system name and version.
 * Any details about your local setup that might be helpful in troubleshooting, specifically:
    * the Python interpreter version
    * installed libraries
    * and pytest version.
 * Detailed steps to reproduce the bug.

## Fix bugs

Look through the `GitHub issues for bugs <https://github.com/js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}>`_.


## Implement features
Look through the `GitHub issues for enhancements <https://github.com/js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}/labels/type:%20enhancement>`_.

## Preparing Pull Requests
### Short version
##### Fork the repository.
##### Enable and install `pre-commit <https://pre-commit.com>`_ to ensure style-guides and code checks are followed.
##### Target ``master`` for bugfixes and doc changes.
##### Target ``features`` for new features or functionality changes.
##### Follow **PEP-8** for naming.
##### Tests are run using ``pytest``:

    pytest

   The test environments above are usually enough to cover most cases locally.

##### Write a ``changelog`` entry: ``changelog/2574.bugfix.rst``, use issue id number
   and one of ``bugfix``, ``removal``, ``feature``, ``vendor``, ``doc`` or
   ``trivial`` for the issue type.
##### Unless your change is a trivial or a documentation fix (e.g., a typo or reword of a small section)
   Please add yourself to the ``AUTHORS`` file, in alphabetical order.


### Long version
What is a "pull request"?  It informs the project's core developers about the
changes you want to review and merge.  Pull requests are stored on
`GitHub servers <https://github.com/js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}/pulls>`_.
Once you send a pull request, we can discuss its potential modifications and
even add more commits to it later on. There's an excellent tutorial on how Pull
Requests work in the
`GitHub Help Center <https://help.github.com/articles/using-pull-requests/>`_.

Here is a simple overview, with{{cookiecutter.project_name.replace(' ', '-')}}-specific bits:

##### Fork the
   `{{cookiecutter.project_name}}  GitHub repository <https://github.com/js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}>`__.  It's
   fine to use ``{{cookiecutter.project_name.replace(' ', '-')}}`` as your fork repository name because it will live under your user.

##### Clone your fork locally using `git <https://git-scm.com/>`_ and create a branch:

    $ git clone git@github.com:YOUR_GITHUB_USERNAME/{{cookiecutter.project_name.replace(' ', '-')}}.git
    $ cd {{cookiecutter.project_name.replace(' ', '-')}}
    # now, to fix a bug create your own branch off "master":

        $ git checkout -b fix/your-bugfix-branch-name master

    # or to instead add a feature create your own branch off "master":

        $ git checkout -b feature/your-feature-branch-name master

   Given we have "major.minor.micro" version numbers, bugfixes will usually
   be released in micro releases whereas features will be released in
   minor releases and incompatible changes in major releases.

   If you need some help with Git, follow this quick start
   guide: https://git.wiki.kernel.org/index.php/QuickStart

##### Install pytest

   pytest is used to run all the tests
   
    $ pip install pytest

##### Run all the tests

   You need to have at Python {{cookiecutter.python_version_min}} available in your system.  Now running tests is as simple as issuing these commands:

    $ conda activate {{cookiecutter.project_name.replace(' ', '-')}}-dev
    $ pytest

##### You can now edit your local working copy and run the tests again as necessary. Please follow PEP-8 for naming.

   You can pass different options to ``pytest``. For example, to run tests and pass options (e.g. enter pdb on failure) to pytest you can do:

    $ pytest -- --pdb

   Or to only run tests in a particular test module:

    $ pytest -- tests/test_config.py


##### Commit and push once your tests pass and you are happy with your change(s):

    $ git commit -a -m "<commit message>"
    $ git push -u

##### Create a new changelog entry in ``changelog``. The file should be named ``<issueid>.<type>.rst``,
   where *issueid* is the number of the issue related to the change and *type* is one of
   ``bugfix``, ``removal``, ``feature``, ``vendor``, ``doc`` or ``trivial``. You may not create a
   changelog entry if the change doesn't affect the documented behaviour of {{cookiecutter.project_name}}.

##### Add yourself to ``AUTHORS`` file if not there yet, in alphabetical order.

##### Finally, submit a pull request through the GitHub website using this data:

    head-fork: YOUR_GITHUB_USERNAME/{{cookiecutter.project_name.replace(' ', '-')}}
    compare: your-branch-name

    base-fork: js-dieu/{{cookiecutter.project_name.replace(' ', '-')}}
    base: master          # if it's a bugfix
    base: features        # if it's a feature

