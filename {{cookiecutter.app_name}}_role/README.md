# {{ cookiecutter.app_name | replace('_',' ') | title }} Ansible role
![Logo](logo.gif)

[![Build Status](https://app.travis-ci.com/idealista/{{ cookiecutter.app_name }}_role.svg)](https://app.travis-ci.com/github/idealista/{{ cookiecutter.app_name }}_role)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-idealista.{{ cookiecutter.app_name }}_role-B62682.svg)](https://galaxy.ansible.com/idealista/{{ cookiecutter.app_name }}_role)



This ansible role installs {% if cookiecutter.documentation_URL != "" %}[{% endif %}{{ cookiecutter.app_name | replace('_',' ') | title }}{% if cookiecutter.documentation_URL != "" %}]({{ cookiecutter.documentation_URL }}){% endif %} in a Debian environment. It has been tested for the following Debian versions:
{% if cookiecutter.debian_bullseye_support == 'True' %}* Bulleye{% endif %}
{% if cookiecutter.debian_buster_support == 'True' %}* Buster{% endif %}

This role has been generated using the [cookiecutter](https://github.com/cookiecutter/cookiecutter) tool, you can generate a similar role that fits your needs using the this [cookiecutter template](https://github.com/idealista/cookiecutter-ansible-role).

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started
These instructions will get you a copy of the role for your Ansible playbook. Once launched, it will install {{ cookiecutter.app_name | replace('_',' ') | title }} in a Debian system.

### Prerequisities

Ansible {{ cookiecutter.ansible_version }} version installed.

Molecule 3.x.x version installed.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver and [Goss](https://github.com/goss-org/goss) as verifier.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: idealista.{{ cookiecutter.app_name }}_role
  version: 1.0.0
  name: {{ cookiecutter.app_name }}_role
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: {{ cookiecutter.app_name }}_role
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties, it is very likely that you will not need to override any variables.


## Testing

### Install dependencies

```sh
$ pipenv sync
```

For more information read the [pipenv docs](ipenv-fork.readthedocs.io/en/latest/).

### Testing

```sh
$ pipenv run molecule test 
```

## Built With

![Ansible](https://img.shields.io/badge/ansible-{{ cookiecutter.ansible_version }}-green.svg)
![Molecule](https://img.shields.io/badge/molecule-{{ cookiecutter.molecule_version }}-green.svg)
![Goss](https://img.shields.io/badge/goss-0.3.16-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.app_name }}_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.app_name }}_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
