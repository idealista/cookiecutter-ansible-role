#!/usr/bin/python3

import sys
import os
import shutil


def checkInput():
    appName = "{{ cookiecutter.app_name }}"
    moleculeVersion = "{{ cookiecutter.molecule_version }}"
    if appName.endswith("role"):
        print("Error: app_name should not have _role or -role at the end, try again without it")
        print("       The name of the role will the value you introduce in app_name plus _role appended")
        sys.exit(1)
    if not moleculeVersion.startswith("3"):
        print("Error: Only supported molecule version 3.x.x, please change it and try again")
        sys.exit(1)

def configureRole():
    # Remove or not the service
    if not {{ cookiecutter.has_service }}:
        # Delete the service and things that reference the service
        os.remove("tasks/service.yml")
        os.remove("templates/{{ cookiecutter.app_name }}.service.j2")
        # Remove or not the handlers folder
        if not {{ cookiecutter.has_handlers }}:
            shutil.rmtree("handlers")
        # Remove or not the templates folder
        if not {{ cookiecutter.has_templates }}:
            shutil.rmtree("templates")
    # Remove or not the files folder
    if not {{ cookiecutter.has_files }}:
        shutil.rmtree("files")
    else:
        os.remove("files/.empty")

def generatePipfile():
    os.system("pipenv install -r test-requirements.txt --three")

def main():
    checkInput()
    configureRole()
    generatePipfile()

if __name__ == '__main__':
    main()