from src.normalize.slugify import normalize_headers

def test_normalize_headers():
    h = ["First Name", "Email Address!!", "  USER-ID  "]
    assert normalize_headers(h) == ["first_name", "email_address", "user_id"]
