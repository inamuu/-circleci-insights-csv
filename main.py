# coding: utf-8

import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_projects(api_url: dict):
    payload = {
        "Authorization": "Basic " + os.environ.get("API_TOKEN")
    }
    response = requests.get(
        api_url + "/me",
        headers=payload
    ).json()
    return response


def main():
    response = get_projects(os.environ.get("CIRCLECI_API_V1"))
    if type(response) != dict:
        raise TypeError('Not dict')
    project_list = response['projects']


if __name__ == '__main__':
    main()
