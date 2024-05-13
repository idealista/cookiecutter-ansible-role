# Change Log

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## Added
- *[#103](https://github.com/idealista/cookiecutter-ansible-role/pull/103) (2024-01-17)- Add ".gitattributes" file for linguist detection.* @ygomezsaiz

## Unreleased

## [2.10.2](https://github.com/idealista/cookiecutter-ansible-role/tree/2.10.2)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.10.1...2.10.2)

### Changed

- *[98](https://github.com/idealista/cookiecutter-ansible-role/issues/98)* Change goss URL @Marionv91

## [2.10.1](https://github.com/idealista/cookiecutter-ansible-role/tree/2.10.)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.10.0...2.10.1)

### Fixed

- *[95](https://github.com/idealista/cookiecutter-ansible-role/issues/95)* Failing travis test builds due to pipenv @ultraheroe

## [2.10.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.10.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.9.0...2.10.0)

### Changed

- *Improve README init scrips to avoid errors when create two roles on same path because already pipenv exists.* @adrian-arapiles
- *Change travis.yml order of email notification as documentation explains.* @adrian-arapiles
- *Add first line `---` to ansible-lint file because it's a yml.* @adrian-arapiles

### Fixed

- *[92](https://github.com/idealista/cookiecutter-ansible-role/issues/92) Fix meta.yml lint warning from `galaxy-tags` to `galaxy_tags`.* @adrian-arapiles

## [2.9.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.9.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.8.1...2.9.0)

### Changed

- *[#86](https://github.com/idealista/cookiecutter-ansible-role/issues/86) Upgrade molecule config to test under debian bullseye* @santi-eidu
- *[#86](https://github.com/idealista/cookiecutter-ansible-role/issues/86) Upgrade ansible to v5.2.0 and ansible lint to v5.3.2 to avoid lint error* @santi-eidu

## [2.8.1](https://github.com/idealista/cookiecutter-ansible-role/tree/2.8.1)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.8.0...2.8.1)

### Fixed

- *[#87](https://github.com/idealista/cookiecutter-ansible-role/issues/87) Travis build image and link are broken in the README template* @emepege

## [2.8.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.8.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.7.0...2.8.0)

### Added

- *[#81](https://github.com/idealista/cookiecutter-ansible-role/issues/81) Add log path variable in defaults* @blalop
- *[#79](https://github.com/idealista/cookiecutter-ansible-role/issues/79) Add molecule-docker support* @blalop
- *[#79](https://github.com/idealista/cookiecutter-ansible-role/issues/79) Add default versions for Python packages* @blalop
- *[#83](https://github.com/idealista/cookiecutter-ansible-role/issues/83) Don't leave empty lines when using jinja* @blalop

## [2.7.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.7.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.6.1...2.7.0)

### Added

- *[#76](https://github.com/idealista/cookiecutter-ansible-role/issues/76) Create shell user variable* @emepege

## [2.6.1](https://github.com/idealista/cookiecutter-ansible-role/tree/2.6.1)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.6.0...2.6.1)

### Changed

- *[#73](https://github.com/idealista/cookiecutter-ansible-role/issues/73) Add document start to .yml files* @blalop

## [2.6.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.6.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.5.1...2.6.0)

### Added

- *[#69](https://github.com/idealista/cookiecutter-ansible-role/issues/69) Email notifications in travis.* @vicsufer

### Changed

### Fixed

- *[#67](https://github.com/idealista/cookiecutter-ansible-role/issues/67) fix needed task in check_mode- @vicsufer

### Removed

## [2.5.1](https://github.com/idealista/cookiecutter-ansible-role/tree/2.5.1)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.5.0...2.5.1)

### Changed

- *[#63](https://github.com/idealista/cookiecutter-ansible-role/issues/63) Ignore html in gitattributes file* @blalop

### Fixed

- *[#62](https://github.com/idealista/cookiecutter-ansible-role/issues/62) molecule verify fails and breaks the run when at least one test fail* @ultraheroe
- *[#60](https://github.com/idealista/cookiecutter-ansible-role/issues/60) [BUG] Wrong state option in "Ensure skeleton log paths" task* @emepege

## [2.5.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.5.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.4.1...2.5.0)

### Added

- *[#57](https://github.com/idealista/cookiecutter-ansible-role/issues/57) Added gitattributes file* @blalop

### Changed

- *[#55](https://github.com/idealista/cookiecutter-ansible-role/issues/55) Excluded non-role files from linting* @blalop

## [2.4.1](https://github.com/idealista/cookiecutter-ansible-role/tree/2.4.1)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.4.0...2.4.1)

### Fixed

- *[#50](https://github.com/idealista/cookiecutter-ansible-role/issues/50) Tags not applied properly from playbook* @vicsufer

## [2.4.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.4.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.3.0...2.4.0)

### Added

- *[#45](https://github.com/idealista/cookiecutter-ansible-role/issues/45) Documentation link provided on role generation* @xtianae7

### Changed

- *[#47](https://github.com/idealista/cookiecutter-ansible-role/pull/47) Bump goss version from 0.3.14 to 0.3.16* @vicsufer
- *[#46](https://github.com/idealista/cookiecutter-ansible-role/issues/46) Static tests instead of parameters* @xtianae7

## [2.3.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.3.0)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.2.0...2.3.0)

### Fixed

- *[#40](https://github.com/idealista/cookiecutter-ansible-role/issues/40) Updated yamllint configuration* @frantsao

### Changed

- *[#38](https://github.com/idealista/cookiecutter-ansible-role/pull/38) Bump goss version from 0.3.11 to 0.3.14* @vicsufer
- *[#30](https://github.com/idealista/cookiecutter-ansible-role/issues/30) Using a new version for issue template* @xtianae7

### Removed

- *[#39](https://github.com/idealista/cookiecutter-ansible-role/pull/39) Community health files* @vicsufer
- *[#30](https://github.com/idealista/cookiecutter-ansible-role/issues/30) PULL_REQUEST_TEMPLATE removed, replaced with default community health file* @xtianae7

## [2.2.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.2.0) (2020-11-10)

### [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.1.0...2.2.0)

### Fixed

- *[#27](https://github.com/idealista/cookiecutter-ansible-role/issues/27) Adding Probot configuration to Ansible Role template* @dortegau

### Changed

- *[#27](https://github.com/idealista/cookiecutter-ansible-role/issues/27) Increase to 90 days the minimum days to declare a PR/Issue as `staled`* @dortegau
- *[#32](https://github.com/idealista/cookiecutter-ansible-role/pull/32) Avoid closing automatically good first issues* @vicsufer

### Removed

- *[#29](https://github.com/idealista/cookiecutter-ansible-role/issues/29) Removing redudant script in .travis.yml* @xtianae7

## [2.1.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.1.0) (2020-10-19)

## [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/2.0.0...2.1.0)

### Added

- *[#20](https://github.com/idealista/cookiecutter-ansible-role/issues/20) Add basic configuration in order to enable Probot to delete automatically abandoned PRs/issues* @dortegau

### Fixed

- *[#23](https://github.com/idealista/cookiecutter-ansible-role/issues/23) Change references to branch master to main* @pgomezcaldito

## [2.0.0](https://github.com/idealista/cookiecutter-ansible-role/tree/2.0.0) (2020-10-13)

## [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/1.0.1...2.0.0)

### Removed

- *[#16](https://github.com/idealista/cookiecutter-ansible-role/issues/16) Remove debian jessie support* @pablogcaldito

### Added

- *[#15](https://github.com/idealista/cookiecutter-ansible-role/issues/15) Add pipenv wrapper* @pablogcaldito
- *Add boilerplate README.md* @vicsufer

## [1.0.1](https://github.com/idealista/cookiecutter-ansible-role/tree/1.0.1) (2020-09-17)

## [Full Changelog](https://github.com/idealista/cookiecutter-ansible-role/compare/1.0.0...1.0.1)

### Removed

- *[#9](https://github.com/idealista/cookiecutter-ansible-role/issues/9) Remove Vagrant pattern from role gitignore file* @vicsufer

### Added

- *[#4](https://github.com/idealista/cookiecutter-ansible-role/issues/4) Upgrade to Goss v0.3.11* @pablogcaldito

### Fixed

- *[#11](https://github.com/idealista/cookiecutter-ansible-role/issues/11) Fix parameterization of PrivateTmp* @pablogcaldito
- *[#7](https://github.com/idealista/cookiecutter-ansible-role/issues/7) Fix bug in in the check version task in install.yml* @pablogcaldito
- *[#3](https://github.com/idealista/cookiecutter-ansible-role/issues/3) Fix typo in both contributing files* @pablogcaldito

## [1.0.0](https://github.com/idealista/cookiecutter-ansible-role/tree/1.0.0) (2020-04-28)

### Added

- *First release* @pablogcaldito
