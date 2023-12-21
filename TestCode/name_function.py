def get_formatted_name(first,last,mid=''):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + mid + (' ' if mid else '') + last
    return full_name.title()

