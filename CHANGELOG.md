# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [1.45.0] - Unreleased
### Added
### Changed
### Fixed

## [1.44.3] - 2022-07-27
### Fixed
- Fix handling non-dict error data in ResponseError #128 #129

## [1.44.2] - 2021-11-18
### Fixed
- Fix logic behind `validate_metro_capacity` #125

## [1.44.1] - 2021-09-20
### Fixed
- Fix metros URL used in Metro API lists #122
- Catch TypeError when HardwareReservations do not have a device assignment #120

## [1.44.0] - 2021-05-19
### Added
- User-Agent header added to client requests #113
- `Metro` class added (https://feedback.equinixmetal.com/changelog/new-metros-feature-live) #110
- Adds `metro` property to `DeviceBatch`, `Device`, `IPAddress`, `VLan` #110
- Adds `metro` to `create_device`, `reserve_ip_address`, `create_vlan`, `create_connection` #110
- Adds `list_metros`, `validate_metro_capacity` to `Manager` #110
- Adds `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `OWNERS.md` #102, #101, #100
- Adds package metadata for `author`, `author_email`, `copyright` #114
### Changed
- `facility` is now optional in `create_device`, `reserve_ip_address`, `create_vlan`, `create_connection` #110
- CI is using GH Actions instead of Drone #115
### Fixed
- Handles when IPAddress Facility is null in API responses #117

## [1.43.1] - 2020-09-04
### Fixed
- ResponseError fixed for Python2.7 compatibility

## [1.43.0] - 2020-07-14
### Added
- Support for reinstalling the operating system to a device, including changing the operating system.
- `Manager.create_vlan` now includes a description argument
### Changed
- `ResponseError` will now be raised when an API call results in an error
### Fixed
- `Manager.validate_capacity` now considers availability
- `Manager.create_project_ssh_key` will retry when it encounters 404 responses following a successful creation.
- API responses with `{"error":""}` keys were not handled well, and will now be handled just like `{"errors":[""]}` keys.

## [1.42.0] - 2020-02-14
### Added
- Capturing of `available_in` to Plan
- Capturing of `hardware_reservation`, `spot_price_max`, `termination_time`, and `provisioning_percentage` to `Device`
- Support for creating project ssh keys
- Support for passing `custom_data` when creating a device
### Fixed
- Black not building for CI and thus failing

## [1.41.0] - 2019-10-16
### Added
- Support for retrieval of hardware reservations
- CPR support at device creation

## [1.40.0] - 2019-10-14
### Added
- Integration tests are only run if `PACKET_PYTHON_TEST_ACTUAL_API` envvar is set
- Rescue action and along with test
- Missing SPDX and source encoding meta comments
### Removed
- Use of Travis CI

## [1.39.1] - 2019-09-17
### Added
- Support for `hardware_reservation_id`

## [1.39.0] - 2019-08-26
### Added
- Support for Organizations, Events, Emails, VLAN, Snapshot Policies, Batches, Ports, VPN and IPs.
- Live tests

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
