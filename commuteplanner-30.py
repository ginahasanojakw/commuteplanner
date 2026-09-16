# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: CommutePlanner
def parse_date(date_str):
        """Parse a date string in YYYY-MM-DD or DD/MM/YYYY format."""
        try:
            if '-' in date_str:
                return datetime.strptime(date_str, '%Y-%m-%d')
            elif '/' in date_str:
                return datetime.strptime(date_str, '%d/%m/%Y')
            else:
                raise ValueError(f"Unrecognized date format: '{date_str}'")
        except ValueError as e:
            raise ValueError(f"Invalid date: '{date_str}' ({e})") from e
