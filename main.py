# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main():
    print(os.environ.get("CIRCLECI_API_V1"))


if __name__ == '__main__':
    main()
