#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pathlib
import re
from setuptools import setup, find_packages


def read_version():
    p = pathlib.Path(__file__)
    p = p.parent / "{{ cookiecutter.project_slug}}" / '__init__.py'
    with p.open('r') as f:
        for line in f:
            if line.startswith('__version__'):
                line = line.split('=')[1].strip()
                match = re.match(r"^['\"](\d+\.\d+\.\d+\w*)['\"]", line)
                if match:
                    return match.group(1)
    raise ValueError('Unable to compute version')


def read(fname):
    file_path = pathlib.Path(__file__).parent / fname
    with file_path.open('r', encoding='utf-8') as f:
        return f.read()


def get_requirements():
    requirements = pathlib.Path(__file__).parent / 'requirements.txt'
    with requirements.open('r', encoding='utf-8') as f:
        packages = f.readlines()
        packages.append('wheel')
    return list(set([i for i in packages])) 


setup(
    name='{{cookiecutter.project_name}}',
    version=read_version(),
    author='{{cookiecutter.author_full_name}}',
    author_email='{{cookiecutter.author_email}}',
    maintainer='{{cookiecutter.author_full_name}}',
    maintainer_email='{{cookiecutter.author_email}}',
    license='MIT',
    project_urls=dict(Source='https://github.com/CFMTech/{{cookiecutter.project_name.replace(" ", "-")}}',
                      Tracker='https://github.com/CFMTech/{{cookiecutter.project_name.replace(" ", "-")}}/issues'),
    url='https://{{cookiecutter.project_name.replace(" ", "-")}}.readthedocs.io/',
    description='{{cookiecutter.project_short_description}}',
    long_description=read('README.md'),
    packages=find_packages('.', exclude=('tests', 'example', 'docs')),
    python_requires=f'>=3.{ {{cookiecutter.python_version_min}} }',
    install_requires=get_requirements(),
    options={"bdist_wheel": {"universal": False}},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: {{cookiecutter.intended_audience}}',
        'Programming Language :: Python',
        f'Programming Language :: Python :: { {{cookiecutter.python_version_major}} }',
        {%- for item in range(cookiecutter.python_version_min, cookiecutter.python_version_max + 1): %}
        'Programming Language :: Python :: {{ item }}',
        {%- endfor %}
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: {{cookiecutter.operating_system}}',
        'License :: OSI Approved :: MIT License',
    ],
    {%- if 'no' != cookiecutter.command_line_interface|lower %}
    entry_points={ 'console_scripts': [ '{{ cookiecutter.project_name.lower().replace(" ", "-")}}={{ cookiecutter.project_slug }}.cli:main', ], },
    {%- endif %}
)
