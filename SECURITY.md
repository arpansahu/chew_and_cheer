# Security Policy

## Supported Versions

We provide security patches for the latest release of our project. Users are encouraged to always update to the latest version to ensure they have the most recent security fixes.

| Version       | Supported          | End of Support |
| ------------- | ------------------ | -------------- |
| 2.0.x         | :white_check_mark: | Active         |
| 1.0.x         | :warning: Limited  | 2026-06-30     |
| < 1.0.0       | :x:                | Unsupported    |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly. **Do not** open a public issue.

### How to Report

Send an email to [arpansahu@zohomail.in](mailto:arpansahu@zohomail.in) with the following information:

- **Type of vulnerability** (e.g., SQL injection, XSS, CSRF, authentication bypass)
- **Full path of source file(s)** related to the vulnerability
- **Location of the affected source code** (tag/branch/commit or direct URL)
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact assessment** (what an attacker could achieve)
- **Suggested fix** (if you have one)

### Response Time

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Fix Timeline**: Based on severity (Critical: 7 days, High: 14 days, Medium: 30 days)

### Vulnerability Handling Process

1. **Acknowledgment**: We acknowledge receipt of your report within 48 hours
2. **Validation**: We validate and reproduce the vulnerability
3. **Severity Assessment**: We assess severity using CVSS scoring
4. **Fix Development**: We develop and test a fix
5. **Patch Release**: We release a security patch for supported versions
6. **Disclosure**: We coordinate public disclosure with the reporter
7. **Credit**: We credit the reporter (unless anonymity is requested)

## Security Features

This application implements several security measures:

### Authentication & Authorization
- Secure user authentication with Django's built-in system
- Session management with secure cookies
- Password hashing using PBKDF2 algorithm
- CSRF protection on all forms
- Permission-based access control

### Data Protection
- SSL/TLS encryption for all connections (PostgreSQL, Redis)
- Secure storage integration with MinIO
- Environment-based secrets management
- Database connection pooling with SSL

### API Security
- Rate limiting on API endpoints
- Token-based authentication for API access
- CORS configuration with allowed origins
- Input validation and sanitization
- GraphQL query depth limiting

### Infrastructure Security
- Sentry integration for error tracking
- Redis cache with SSL support
- PostgreSQL with SSL connections
- Container security with Harbor registry
- Jenkins CI/CD with credential management

### Monitoring & Logging
- Comprehensive application logging
- Sentry error tracking and alerting
- Health check endpoints
- Audit trails for critical operations

## Security Best Practices for Deployment

### Required Configuration
- [ ] Set `DEBUG = False` in production
- [ ] Use strong `SECRET_KEY` (rotate regularly)
- [ ] Configure `ALLOWED_HOSTS` properly
- [ ] Enable SSL/TLS for all connections
- [ ] Set secure cookie flags (`SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`)
- [ ] Configure `SECURE_HSTS_SECONDS` for HTTPS enforcement
- [ ] Implement proper CORS settings
- [ ] Use environment variables for all secrets

### Regular Maintenance
- Keep Django and all dependencies updated
- Monitor security advisories for used packages
- Regularly review and rotate credentials
- Perform periodic security audits
- Review and update access controls
- Monitor application logs for suspicious activity

### Database Security
- Use strong database passwords (20+ characters)
- Enable SSL for database connections
- Limit database user permissions
- Regular database backups with encryption
- Network isolation for database access

### Application Security
- Validate all user inputs
- Sanitize outputs to prevent XSS
- Use parameterized queries (Django ORM handles this)
- Implement rate limiting on sensitive endpoints
- Use secure session configuration
- Enable Content Security Policy (CSP)

## Dependency Management

We regularly update dependencies to address security vulnerabilities:

- **Automated scanning**: GitHub Dependabot alerts
- **Manual review**: Monthly dependency audits
- **Update policy**: Critical vulnerabilities patched within 7 days

To check for vulnerabilities in dependencies:
```bash
pip install safety
safety check -r requirements.txt
```

## Security Testing

We employ multiple testing approaches:

- **Unit tests**: Comprehensive test coverage with django-test-enforcer
- **Integration tests**: Testing authentication and authorization flows
- **UI tests**: Selenium-based security testing
- **Static analysis**: Code review for security issues
- **Dependency scanning**: Regular vulnerability checks

## Incident Response

In case of a security incident:

1. **Detect**: Monitor logs and alerts via Sentry
2. **Contain**: Isolate affected systems if necessary
3. **Investigate**: Determine scope and impact
4. **Remediate**: Apply fixes and patches
5. **Recover**: Restore normal operations
6. **Review**: Post-incident analysis and improvements

## Compliance

This application follows:

- OWASP Top 10 security guidelines
- Django security best practices
- Secure coding standards for Python
- Data protection principles

## Contact

For security-related questions or concerns:

- **Email**: [arpansahu@zohomail.in](mailto:arpansahu@zohomail.in)
- **Response Time**: 24-48 hours for security inquiries

## Security Credits

We appreciate responsible disclosure and will credit security researchers (with permission):

*No vulnerabilities have been reported to date.*

---

**Last Updated**: February 17, 2026  
**Document Version**: 2.0