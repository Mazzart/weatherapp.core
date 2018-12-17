"""Main module of the application"""

import html
import sys
from argparse import ArgumentParser


class App:
    """Weather aggregator application"""

    def __init__(self):
        self.arg_parser = self._arg_parse()

    def _arg_parse(self):
        """Initialize argument parser."""
        arg_parser = ArgumentParser(add_help=False)
        arg_parser.add_argument('command', help='Command', nargs='?')
        arg_parser.add_argument('--refresh', help='Bypass caches',
                                action='store_true')

        return arg_parser

    def program_output(self, city: str, info: dict):
        """Print the application output in readable form"""

        length_column_1 = max(len(key) for key in info.keys())
        length_column_2 = max(len(value) for value in info.values())

        print(f'{city.upper()}')

        def border_line(column_1: int, column_2: int) -> str:
            """Print a line for dividing information"""

            line = ''.join(['+'] + ['-' * (column_1 + column_2 + 5)] + ['+'])
            return line

        def status_msg(msg: str, state: str) -> str:
            """Print weather information"""

            result = f"| {msg} {' ' * (length_column_1 - len(msg))}" \
                     f"| {state} {' ' * (length_column_2 - len(state))}|\n"
            return result

        print(border_line(length_column_1, length_column_2))

        for key, value in info.items():
            print(status_msg(key, html.unescape(value)), end='')

        print(border_line(length_column_1, length_column_2))

    def run(self, argv):
        """Run application

        :param argv: list of passed arguments
        """

        self.options, remaining_args = self.arg_parser.parse_known_args(argv)
        command_name = self.options.command

        if not command_name:
            # run all weather providers by default
            pass
        elif command_name in {}:
            # run specific provider
            pass


def main(argv=sys.argv[1:]):
    return App().run(argv)
