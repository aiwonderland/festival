# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.0-beta.4] - 2026-02-05
### Added
- test `version.py` files.
- test function `test_bar_error` in `test_bar.py`.

## [0.0.0-beta.3] - 2026-02-04
### Added
- test files.
- docstring in `Bar`.
### Fixed
- The `_Bar` class is missing the `__len__` method.
- Fix _draw() method in `_Bar` to return a string.
- Fix __eq__ method in `Bar` to not compare current values.

## [0.0.0-beta.2] - 2026-02-04
### Fixed
- The example in the README document contains a line of HTML(#1).

## [0.0.0-beta.1] - 2026-02-04
### Added
- Add new code examples to the `README.md`.
### Fixed
- Fixed an import error caused by `version.py`(now name) with a certain name.
### Changed
- Changed `__version__.py` s'file name to `version.py`
### Removed
- Removed redundant comments in `core/_text.py`. (These comments were commented-out code.)

