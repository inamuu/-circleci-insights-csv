# coding: utf-8

import os
from os.path import join, dirname
from tkinter import W
from dotenv import load_dotenv
import requests

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def get_projects(api_url: str) -> dict:
    payload = {
        "Authorization": "Basic " + os.environ.get("API_TOKEN")
    }
    response = requests.get(
        api_url + "/me",
        headers=payload
    ).json()
    return response


def get_workflows(api_url: str, project_list: list) -> dict:
    payload = {
        "Authorization": "Basic " + os.environ.get("API_TOKEN"),
    }
    params = {
        "reporting-window": "last-30-days"
    }

    pjt_summary = {}
    for project in project_list:
        response = requests.get(
            api_url + "/insights/pages/gh/"
            + str(os.environ.get("ORGS_NAME"))
            + "/" + project
            + "/summary",
            headers=payload,
            params=params
        ).json()
        pjt_summary[project] = response['project_workflow_data']
    return pjt_summary


def main():
    response = get_projects(os.environ.get("CIRCLECI_API_V1"))
    if type(response) != dict:
        raise TypeError('Not dict')
    project_url_list = response['projects']

    project_list = []
    for key in project_url_list:
        repo_url = key.split('/')
        if repo_url[3] != os.environ.get("ORGS_NAME"):
            break
        project_list.append(repo_url[4])
    workflows = get_workflows(os.environ.get("CIRCLECI_API_V2"), project_list)
    print(workflows)


if __name__ == '__main__':
    main()
