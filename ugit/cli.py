import argparse
import os

from ugit import data
from ugit.data import GIT_DIR

def main():
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser(description="A DIY git in python")

    commands = parser.add_subparsers(dest='command', required=True)

    init_parser = commands.add_parser("init", description="initializes ugit")
    init_parser.set_defaults(func=init)

    return parser.parse_args()
    

def init(args):
    print(data.init())

