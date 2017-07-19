# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [0.5.5] - 2017-07-19
### Added
- `dupliate_item` and `duplicate_assessment` methods with tests.

## [0.5.4] - 2017-07-19
### Added
- Tests for the `edX` and `lore` `repository` record extensions.
- Decorator in AWS and Filesystem adapters to remove `None` proxy for
  Manager methods.
- Test cassettes for AWS tests.
- Tests for most `primordium` objects.
- Cataloging tests.

### Changed
- Temporal record extension returns `DateTime` object, not `dict`.

### Fixed
- Various bugs in the `edX` and `lore` `repository` record extensions.

### Removed
- Unused `duplicate_X` methods.
- Auto-enclosure on create and update asset forms.

## [0.5.3] - 2017-07-07
### Fixed
- Fix method names for creating and updating sequence rules in `assessment_utilities.py`.
- Getting existing `mdata` values returns key with matching type, i.e. returns `existing_date_time_values` instead of `existing_object_values`.
- Fixed method name when checking if `Assessment` has shuffled sections. (out of spec)
- Missing `Id` use when getting `items` for an `AssessmentTaken`.
- Extraneous argument when checking `priority` is valid, in `osid.logging.LogEntryForm.set_priority` template.
- `delete_question` uses the right key to query the database.
- Handle notification sessions in services better.
- Fixed various templates in `ResourceBinAssignmentSession` methods to use template contexts, instead of the `resource` words like `bin` and `resource`.
- Fix `services` builder to handle sub-package methods better.
- Learning `Activity` methods to check what type of `Activity` it is.
- Drag and drop record type handles missing `description` field.
- QTI record type handles non-multilanguage QTI.

### Changed
- Updated many `mdata` values from basic strings to `DisplayText` objects.
- `GradeSystem` timestamps to be stored as actual `datetime` objects, not dictionaries.
- Mocked out external service calls for Handcar and AWS tests.
- Ignored profile files, `app_configs` and `abstract_osid` directories for coverage reporting.

### Added
- Unimplemented methods:
   - `_get_previous_assessment_section`
   - `SequenceRuleQuery` `__init__`
   - `GradebookColumnSummaryQuery` `__init__`
   - `osid.logging.LogEntryForm.clear_priority_template`
   - Various authz adapter passthroughs that were missing
- More extensive testing:
   - Change skipped tests to actually test for `Unimplemented` exception.
   - Parameterized tests using `pytest`, to test across different service configurations.
   - Switch to `pytest` syntax instead of `unittest` syntax.
- Cataloging package.
- Series of hand-written tests put in the `tests/other` directory.

## [0.5.2] - 2017-06-12
### Fixed
- Compatibility with `pymongo` 2 and 3.

## [0.5.1] - 2017-06-06
### Changed
- Unlock Previous changed to simple string, instead of DisplayText.

## [0.5.0] - 2017-06-05
### Added
- Tests for CLIx `N of M` records.
- Tests for reviewable assessment offered and taken records.
- CLIx record for `unlockPrev` setting for the previous button.

## [0.4.2] - 2017-05-31
### Fixed
- Unicode handling in two records, for Python 2 / 3 compatibility.

## [0.4.1] - 2017-05-31
### Added
- Tests for json and filesystem utilities.
- Mock handcar adapter tests with `vcrpy` library.

### Changed
- MongoListener handles filesystem and test cases better.
- Filesystem `.json` encoding forced to `utf8`.
- Handcar adapter uses `requests` library.

### Fixed
- Filesystem query method `len()` of keys check.
- Helper iterator forces lists to be iterators.

## [0.4.0] - 2017-05-26
### Changed
- Python 3.4+ compatibility.

## [0.3.7] - 2017-05-10
### Added
- Tests for various records.

### Fixed
- Check for `text` is not `None` in `FilesRecord` when replacing
  urls.

## [0.3.6] - 2017-05-08
### Fixed
- For Windows, use `b` flag in `get_data()` of `filesystem_adapter`.

## [0.3.5] - 2017-04-28
### Added
- Tests for various sessions and managers.

## [0.3.4] - 2017-04-26
### Added
- Some basic tests for the `aws_adapter`. Requires setting
  configurations for AWS S3 and CloudFront.

## [0.3.3] - 2017-04-25
### Added
- Transcript XML template file added to `package_data` in
  `setup.py`.

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

[0.5.5]: https://github.com/mitsei/dlkit/compare/0.5.4...0.5.5
[0.5.4]: https://github.com/mitsei/dlkit/compare/0.5.3...0.5.4
[0.5.3]: https://github.com/mitsei/dlkit/compare/0.5.2...0.5.3
[0.5.2]: https://github.com/mitsei/dlkit/compare/0.5.1...0.5.2
[0.5.1]: https://github.com/mitsei/dlkit/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/mitsei/dlkit/compare/0.4.2...0.5.0
[0.4.2]: https://github.com/mitsei/dlkit/compare/0.4.1...0.4.2
[0.4.1]: https://github.com/mitsei/dlkit/compare/0.4.0...0.4.1
[0.4.0]: https://github.com/mitsei/dlkit/compare/0.3.7...0.4.0
[0.3.7]: https://github.com/mitsei/dlkit/compare/0.3.6...0.3.7
[0.3.6]: https://github.com/mitsei/dlkit/compare/0.3.5...0.3.6
[0.3.5]: https://github.com/mitsei/dlkit/compare/0.3.4...0.3.5
[0.3.4]: https://github.com/mitsei/dlkit/compare/0.3.3...0.3.4
[0.3.3]: https://github.com/mitsei/dlkit/compare/0.3.2...0.3.3
[0.3.2]: https://github.com/mitsei/dlkit/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/mitsei/dlkit/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/mitsei/dlkit/compare/0.2.1...0.3.0
[0.2.1]: https://github.com/mitsei/dlkit/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/mitsei/dlkit/compare/0.1.1...0.2.0
[0.1.1]: https://github.com/mitsei/dlkit/compare/0.1.0...0.1.1
[0.1.0]: https://github.com/mitsei/dlkit/compare/0.0.1...0.1.0
[0.0.1]: https://github.com/mitsei/dlkit/compare/0.0.1...0.0.1
