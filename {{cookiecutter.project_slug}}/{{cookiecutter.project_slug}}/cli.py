import argparse

from {{ cookiecutter.project_name.lower().replace(" ", "-")}} import __version__


def make_parser_and_read_options(args=None):
    parser = argparse.ArgumentParser('{{ cookiecutter.project_name.lower().replace(" ", "-")}}',
                                     description='')
    parser.add_argument('--version', action='version', version=f'%(prog)s, version {__version__}')
    return parser.parse_args(args)


def main():
    try:
        options = make_parser_and_read_options()
    except Exception as e:
        print(e)
