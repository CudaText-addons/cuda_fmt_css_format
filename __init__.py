import os
import json
from cuda_fmt import get_config_filename
from . import cssbeautifier
from . import cssformatter

formatter = cssformatter.CssFormater()

def options():

    op = cssbeautifier.default_options()
    fn = get_config_filename('CSS Beautify')
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)
        op.indent_size                = d.get('indent_size', 4)
        op.indent_char                = d.get('indent_char', ' ')
        op.selector_separator_newline = d.get('selector_separator_newline', True)
        op.end_with_newline           = d.get('end_with_newline', False)
    return op


def do_format(text):

    return cssbeautifier.beautify(text, options())

def do_format_expand(text):

    return formatter.run(text, 'expand')

def do_format_compact(text):

    return formatter.run(text, 'compact')

def do_format_compress(text):

    return formatter.run(text, 'compress')
