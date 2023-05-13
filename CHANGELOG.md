# Changelog

## [0.7] - 2023-05-13

### Changed
- `orbits.ListOfOSVs.to_dataframe` method: changed type of `absolute_orbit`
  column from `orbits.AbsoluteOrbit` to integer.

## [0.6] - 2023-03-30

### Added
- `orbits.ListOfOSVs.to_dataframe` method

## [0.5] - 2023-03-28

### Added
- `exceptions` module.

### Changed
- Move `PositionComponent` and `VelocityComponent` from `basic` to `orbits`.

## [0.4] - 2023-03-04

### Added
- `get_parser` and `get_serializer` functions.

## [0.3] - 2023-02-26

### Added
- Added `py.typed`.

## [0.2] - 2023-02-26

### Changed
- Date time patterns in `eopfiles.time`.
- `ValidityPeriod.validity_start` and `ValidityPeriod.validity_stop` types from
  `Optional[str]` to `str`.

## [0.1] - 2023-02-15

### Added
- Support for Restituted Orbit File and Orbit State Vector file (`AUX_ORBREF`).
- Support for Predicted orbit File (`MPL_ORBPRE`).
