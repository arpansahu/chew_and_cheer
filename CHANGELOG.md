# Changelog

## [2.0.0] - 2026-02-13
### Added
- Migrated to new infrastructure with unified database (arpansahu.space)
- Updated PostgreSQL schema to chew_and_cheer with SSL support
- Integrated with MinIO storage (arpansahu-one-bucket)
- Added Redis cache with SSL support (redis.arpansahu.space:9551)
- Configured Jenkins CI/CD with automated credentials management
- Added Harbor registry support for container images
- Integrated Sentry for error tracking and monitoring
- Added django-test-enforcer for comprehensive test coverage
- Updated domain to chew.arpansahu.space

### Changed
- Updated AWS credentials to use arpansahu user
- Migrated Redis from port 6380 to 9551 with SSL
- Updated database password and connection to use SSL
- Switched from postgres.arpansahu.space to arpansahu.space

### Fixed
- Fixed database schema creation for PostgreSQL
- Corrected environment variable configuration
- Updated Jenkins credentials with proper .env file

## [1.0.0] - 2024-06-27
### Added
- Initial release of the project.
- User authentication module.
- GraphQL API support
- CRUD operations with Ajax and Django forms
- REST API with DRF