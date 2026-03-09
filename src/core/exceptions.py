class WranglerError(Exception):
    """Base exception."""

class DialectDetectionError(WranglerError):
    """Raised when delimiter cannot be inferred."""

class SchemaMismatchError(WranglerError):
    """Raised when record width deviates from header."""
