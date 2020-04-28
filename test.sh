#!/bin/sh

set -e

# Generate role
cookiecutter . --no-input app_name="github_cli" exec_name="gh" author="John Doe" min_ansible_version="2.2" ansible_version="2.8.6" molecule_version="3.0.1" python_docker_version="4.1.0" ansible_lint_version="4.2.0" has_service="False" has_files="False" has_handlers="False" has_templates="False"
(
    # Adjust the role to test
    cd github_cli_role
    sed -i 's/someuser/cli/g' defaults/main.yml
    sed -i 's/somerepo/cli/g' defaults/main.yml
    sed -i 's/1.0.0/0.6.4/g' defaults/main.yml
    sed -i 's/exampleapplication/gh/g' defaults/main.yml
    # Launch molecule tests
    pipenv sync
    pipenv run molecule test
)
# Cleanup
rm -rf github_cli_role
