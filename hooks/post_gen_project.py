import pathlib


wants_cli = '{{ cookiecutter.command_line_interface }}' == "yes"

if not wants_cli:
    p = pathlib.Path( '{{ cookiecutter.project_slug }}' ) / 'cli.py'
    p.unlink()
