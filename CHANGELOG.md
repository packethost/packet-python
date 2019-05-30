# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.38.2] - 2019-05-30
### Added
- Test fixtures to sdist

## [1.38.1] - 2019-05-30
### Fixed
- Changelog

## [1.38.0] - 2019-05-30
### Added
- Support for python3.7
- `legacy` param to `get_capacity` function
### Removed
- Support for python3.3
### Changed
- setup.py no longer converts markdown to reST because pypi now supports markdown, woop.

## [1.37.1] - 2018-01-08
### Fixed
- Version number in setup.py

## [1.37.0] - 2018-01-08
### Added
- Spot Market Support
- Ability to specify ssh keys on device creation

## [1.36.0] - 2017-10-16
### Added
- Better tests using PacketMockManager
- Test on 2.7 and 3.[3-6]
- Changelog

### Changed
- Use tox for testing

## [1.35] - 2017-08-04
### Fixed
- Some tests were broken

## [1.35]
### Added
- `public_ipv4_subnet_size`

## [1.34] - 2017-08-04
### Added
- Custom iPXE and `always_pxe` setting
- Volume coloning
- Device Tags

### Fixed
- Handling of error messages from api response

## [1.33] - 2017-03-15
### Fixed
- Default payment method
