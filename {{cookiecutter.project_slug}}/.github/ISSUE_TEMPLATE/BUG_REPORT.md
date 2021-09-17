# :warning: Attention please ! :warning:

This template is here to help you submit an issue.

It is meant to guide you towards creating a meaningful report, so that the maintainers of `{{cookiecutter.project_name}}` have all the information they need to address your problem in a swift and efficient manner.
Please read carefully each of the sections below, and adapt the text depending on the type of issue you are reporting.

Github uses [Markdown](https://help.github.com/en/github/writing-on-github) to render issues: you can edit this very text here, and then see a preview of how it renders by switching to the *Preview* tab just above this panel.
Do not hesitate to use the full extent of [Markdown formatting][markdown_formatting] to make your issue submission more clear and explicit.

[markdown_formatting]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

If all is clear, you may delete this section and start with your submission.

# Prerequisites

Please answer the following questions **for yourself** before submitting an issue. **YOU MAY DELETE THE PREREQUISITES SECTION.**

- [ ] I am running the latest version of `{{cookiecutter.project_name}}`
- [ ] I checked the documentation and found no answer
- [ ] I [checked](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/issues?utf8=%E2%9C%93&q=is%3Aissue) to make sure that this issue has not already been filed

# Context

Please provide any relevant information about your setup. This is important in case the issue is not reproducible except for under certain conditions.

* `{{cookiecutter.project_name}}` version (`master`, `develop` or a [numbered version](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/releases)):
```python
import pytest
print(pytest.__version__)
```
* `python` version (from a cmd console):
```bash
λ python
Python 3.6.8 |Anaconda, Inc.| (default, Feb 21 2019, 18:30:04) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
* If the bug seems related to a third party package, provide us with the output of a `pip freeze`
 or `conda list` command


# Failure Information (for bugs)

A clear and concise description of what the bug is.
Make sure you [craft minimal bug reports][bug_reports], using [Minimal Complete Verifiable
 Examples][mcve].

[bug_reports]: http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports
[mcve]: https://stackoverflow.com/help/mcve

## Steps to Reproduce

Please provide detailed steps for reproducing the issue.

1. step 1
2. step 2
3. you get it...


## Failure Logs

Please include any relevant log snippets or files here.

# Labels

Correctly labelling your issue helps maintainers with triaging. Use such labels as [`Type: Bug`](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Type%3A%20Bug), [`Type: Question`](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Type%3A%20Question) or [`Type: Enhancement`](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Type%3A%20Enhancement) for example.
Depending on the criticality of your issue, you can also use the `Priority` labels [Critical](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Priority%3A%20Critical), [High](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Priority%3A%20High), [Medium](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Priority%3A%20Medium) or [Low](https://github.com/CFMTech/{{cookiecutter.project_name.replace(' ', '-')}}/labels/Priority%3A%20Low).

Reporting issues is one way to contribute to `{{cookiecutter.project_name}}`, so thanks for your help !
