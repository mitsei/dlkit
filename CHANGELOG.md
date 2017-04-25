# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.3.2] - 2017-04-25
### Added
- Manifest file so that transcript XML template and license
  are part of the distributable.

## [0.3.1] - 2017-04-25
### Fixed
- Old `dlkit_runtime` import in `aws_adapter` changed to
  `dlkit.runtime`.

## [0.3.0] - 2017-04-24
### Added
- `label-ortho-faces` record.
- `edx-numeric-response` record.
- Self evaluation for CLIx and edX records.
- Check in MC Answer form to not add a `None` choice.
- Method in services to grab an `AssetContentLookupSession`.

### Fixed
- CLIx imports that used `dlkit_runtime` to `dlkit.runtime`.

### Changed
- Numeric response `set_answer_value` definition.
- Feedback answers record check for existence of
  `confusedLearningObjectiveIds`.

## [0.2.1] - 2017-04-24
### Fixed
- Changed `fbw` import in the CLIx magic item records
  to point to renamed `adaptive` path.

## [0.2.0] - 2017-04-21
### Added
- Item record entries for `edx-numeric-response-item`
  and `label-ortho-faces`.

## [0.1.1] - 2017-04-21
### Changed
- Project-level config directory is now `dlkit_configs`.

## [0.1.0] - 2017-04-21
### Added
- Media accessibility records.

## [0.0.1] - 2017-04-21
### Added
- Initial public release.

[0.3.2]: https://github.com/mitsei/dlkit/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/mitsei/dlkit/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/mitsei/dlkit/compare/0.2.1...0.3.0
[0.2.1]: https://github.com/mitsei/dlkit/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/mitsei/dlkit/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/mitsei/dlkit/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/mitsei/dlkit/compare/0.0.1...0.1.0
[0.0.1]: https://github.com/mitsei/dlkit/compare/0.0.1...0.0.1
