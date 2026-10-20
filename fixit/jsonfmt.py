"""JSON pretty-printer."""
import json


def format_json(raw: str, indent: int = 2) -> str:
    """Format a JSON string with indentation.

    Example:
        format_json('{"name":"Sam"}') returns '{\n  "name": "Sam"\n}'.
    """
    try:
        data = json.loads(raw)
        return json.dumps(data, indent=indent)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON")
