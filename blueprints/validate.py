"""Validate a curated blueprint string via factorio-draftsman
(third-party dependency, see requirements.txt - pip install -r
requirements.txt). Separate from codec.py, which stays stdlib-only by
design (base64/zlib/json - no install needed just to decode/measure);
this is specifically for the stronger validation draftsman provides
(known entity/item names, valid placement) before a new entry is added
to curated/.

Usage: python blueprints/validate.py blueprints/curated/*.txt
"""

import sys

from draftsman.blueprintable import get_blueprintable_from_string


def validate_blueprint_string(blueprint_string: str):
    """Parse + validate via draftsman. Returns a draftsman
    ValidationResult (`.error_list`/`.warning_list` attributes - both
    empty means clean). Raises if the string can't even be parsed
    (corrupt, or not a real blueprint string at all).
    """
    blueprintable = get_blueprintable_from_string(blueprint_string)
    return blueprintable.validate()


if __name__ == "__main__":
    exit_code = 0
    for path in sys.argv[1:]:
        with open(path) as f:
            bp_str = f.read()
        try:
            result = validate_blueprint_string(bp_str)
        except Exception as err:
            print(f"{path}: FAILED TO PARSE - {err}")
            exit_code = 1
            continue
        errors = result.error_list
        warnings = result.warning_list
        status = "OK" if not errors else "ERRORS"
        print(f"{path}: {status} ({len(errors)} errors, {len(warnings)} warnings)")
        for e in errors:
            print(f"  ERROR: {e}")
        for w in warnings:
            print(f"  WARNING: {w}")
        if errors:
            exit_code = 1
    sys.exit(exit_code)
