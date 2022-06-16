# Cookiecutter Ansible Role
![Logo](https://raw.githubusercontent.com/idealista/cookiecutter-ansible-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/cookiecutter-ansible-role.png)](https://travis-ci.com/idealista/cookiecutter-ansible-role)

This cookiecutter generates an [ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html).

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started
These instructions will get you an Ansible Role generated using [Cookiecutter](https://github.com/cookiecutter/cookiecutter). 

This cookiecutter:
* Follows the best practices 
* Asks you if some features are wanted or not in the role
* Generates a Pipfile and Pipfile.lock for using the role based on some parameters

### Prerequisities

You just need to have [pipenv](https://github.com/pypa/pipenv) installed.

## Usage

To generate your ansible role type ```printf "cookiecutter==1.7.2\nJinja2==2.11.2" > requirements.txt && pipenv install -r requirements.txt && pipenv run cookiecutter https://github.com/idealista/cookiecutter-ansible-role && rm -rf Pipfile*
requirements.txt && pipenv --rm && rm -rf requirements.txt```.

Then, introduce some parameters needed for generating it. 

It displays some comments that help you to use the cookiecutter sucessfully, if you assign value to them nothing happens.

```
comment_0 [The role name will be the value you assign to app_name with _role appended]:
comment_1 [Introduce in exec_name the executable file name, you can change it later in the defaults/main.yml if you don't know it]:
app_name []: github_cli
exec_name []: gh
github_user [idealista]:
company [Idealista S.A.U.]:
author []: pablogcaldito
min_ansible_version []: 2.2
ansible_version []: 5.2.0
molecule_version []: 3.0.1
python_docker_version []: 4.1.0
ansible_lint_version []: 5.3.2
license [Apache 2.0]:
galaxy_tag_1 [example_tag1]: github_cli
galaxy_tag_2 [example_tag2]: github
galaxy_tag_3 [example_tag3]: cli
Select debian_bullseye_support:
1 - True
2 - False
Choose from 1, 2 [1]:
Select debian_buster_support:
1 - True
2 - False
Choose from 1, 2 [1]:
Select has_service:
1 - True
2 - False
Choose from 1, 2 [1]:
Select has_files:
1 - True
2 - False
Choose from 1, 2 [1]:
comment_2 [If there is service the following options will not have any effect]:
Select has_handlers:
1 - True
2 - False
Choose from 1, 2 [1]:
Select has_templates:
1 - True
2 - False
Choose from 1, 2 [1]:
documentation_URL: https://cli.github.com/manual/
```

It will create the following file structure:

```
github_cli_role
├── CHANGELOG.md
├── defaults
│   └── main.yml
├── files
├── handlers
│   └── main.yml
├── LICENSE
├── logo.gif
├── meta
│   └── main.yml
├── molecule
│   └── default
│       ├── converge.yml
│       ├── Dockerfile.j2
│       ├── molecule.yml
│       ├── tests
│       │   └── test_app.yml
│       └── verify.yml
├── Pipfile
├── Pipfile.lock
├── README.md
├── tasks
│   ├── config.yml
│   ├── install.yml
│   ├── main.yml
│   └── service.yml
├── templates
│   └── github_cli.service.j2
└── test-requirements.txt
```

## Testing 

Test the cookiecutter just by typing:

```./test.sh```

## Built With

![Cookiecutter](https://img.shields.io/badge/cookiecutter-1.7.0-green.svg)
![Python 3](https://img.shields.io/badge/python-3.7-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/cookiecutter-ansible-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/cookiecutter-ansible-role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.






