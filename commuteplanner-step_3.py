# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: CommutePlanner
def validate_required(value, field_name=''):
    if not value:
        raise ValueError(f"Field '{field_name}' is required.")
    return value

def validate_positive(value, field_name=''):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive number.")
    return value

def validate_integer(value, field_name=''):
    if not isinstance(value, int):
        raise ValueError(f"Field '{field_name}' must be an integer.")
    return value

def validate_positive_integer(value, field_name=''):
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive integer.")
    return value

def validate_short_text(value, max_length=50, field_name=''):
    if not isinstance(value, str) or len(value) == 0:
        raise ValueError(f"Field '{field_name}' must be a non-empty string.")
    if len(value) > max_length:
        raise ValueError(f"Field '{field_name}' exceeds max length of {max_length}.")
    return value

def validate_identifier(value, field_name=''):
    if not isinstance(value, str) or not value.isalnum():
        raise ValueError(f"Field '{field_name}' must be a valid alphanumeric identifier.")
    return value

def validate_day(value, field_name=''):
    if value not in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
        raise ValueError(f"Field '{field_name}' must be a valid day of the week.")
    return value

def validate_time(value, field_name=''):
    if not isinstance(value, str) or len(value) != 5 or value[2] != ':':
        raise ValueError(f"Field '{field_name}' must be in HH:MM format.")
    try:
        hours, minutes = int(value[0:2]), int(value[3:5])
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError
    except ValueError:
        raise ValueError(f"Field '{field_name}' must be in valid HH:MM format.")
    return value
