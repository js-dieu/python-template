============
Installation
============

.. Explain:: `{{cookiecutter.project_name}}` 
 

Supported environments
----------------------
{% if cookiecutter.operating_system.split(' :: ')[-1] == "OS Independent" %}
`{{cookiecutter.project_name}}` currently works on any platforms.
{% else %} 
`{{cookiecutter.project_name}}` currently works on {{cookiecutter.operating_system.split(' :: ')[-1]}}.
{% endif %}
The following versions of Python are supported:
{% for item in ['3.5', '3.6', '3.7', '3.8', '3.9'] %}
{%+ if cookiecutter.python_version_min  <=  item <=  cookiecutter.python_version_max %}- Python {{ item }} {% endif %}
{%- endfor %}

From conda
----------

Simply run the following command to get it installed in your current environment

.. code-block:: bash

    conda install {{cookiecutter.project_name.replace(' ', '-')}} -c https://conda.anaconda.org/conda-forge


From pip
--------

Simply run the following command to get it installed

.. code-block:: bash

    pip install {{cookiecutter.project_name.replace(' ', '-')}}
