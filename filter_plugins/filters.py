"""Filters for Kerneladmin."""


def gvariant(lst):
    """Turn list of strings to gvariant list."""
    assert isinstance(lst, list), "{} is not a list".format(lst)
    content = ", ".join(
        "'{}'".format(l) for l in lst
    )
    return '[{}]'.format(content)


class FilterModule:
    """FilterModule."""

    def filters(self):
        """Return all jinja filters."""
        return {
            'gvariant': gvariant
        }
