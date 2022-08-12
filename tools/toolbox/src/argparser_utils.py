import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message: str):
        sys.stderr.write(f'Failed to parse args:\n\t{message}\n')
        self.print_help()
        sys.exit(2)
