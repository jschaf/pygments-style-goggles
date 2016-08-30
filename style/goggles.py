from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


BACKGROUND = "#ffffff"
CURRENT_LINE = "#efefef"
SELECTION = "#d6d6d6"
FOREGROUND = "#000000"
COMMENT = "#880000"
RED = "#880000"
GREEN = "#008800"
AQUA = "#006666"
BLUE = "#000088"
PURPLE = "#006666"


class GogglesStyle(Style):

    """
    A colorful style.
    """

    default_style = ''

    styles = {
        # No corresponding class for the following:
        Text:                      FOREGROUND,  # class:  ''
        Whitespace:                "",          # class: 'w'
        Error:                     RED,         # class: 'err'
        Other:                     "",          # class 'x'

        Comment:                   RED,       # class: 'c'
        Comment.Multiline:         "",        # class: 'cm'
        Comment.Preproc:           "",        # class: 'cp'
        Comment.Single:            "",        # class: 'c1'
        Comment.Special:           "",        # class: 'cs'

        Keyword:                   BLUE, # class: 'k'
        Keyword.Constant:          "",   # class: 'kc'
        Keyword.Declaration:       "",   # class: 'kd'
        Keyword.Namespace:         "",   # class: 'kn'
        Keyword.Pseudo:            "",   # class: 'kp'
        Keyword.Reserved:          "",   # class: 'kr'
        Keyword.Type:              "",   # class: 'kt'

        Operator:                  AQUA,      # class: 'o'
        Operator.Word:             "",        # class: 'ow' - like keywords

        Punctuation:               FOREGROUND,  # class: 'p'

        Name:                      FOREGROUND, # class: 'n'
        Name.Attribute:            "",         # class: 'na' - to be revised
        Name.Builtin:              "",         # class: 'nb'
        Name.Builtin.Pseudo:       "",         # class: 'bp'
        Name.Class:                "",         # class: 'nc' - to be revised
        Name.Constant:             "",         # class: 'no' - to be revised
        Name.Decorator:            "",         # class: 'nd' - to be revised
        Name.Entity:               "",         # class: 'ni'
        Name.Exception:            "",         # class: 'ne'
        Name.Function:             "",         # class: 'nf'
        Name.Property:             "",         # class: 'py'
        Name.Label:                "",         # class: 'nl'
        Name.Namespace:            "",         # class: 'nn' - to be revised
        Name.Other:                "",         # class: 'nx'
        Name.Tag:                  "",         # class: 'nt' - like a keyword
        Name.Variable:             "",         # class: 'nv' - to be revised
        Name.Variable.Class:       "",         # class: 'vc' - to be revised
        Name.Variable.Global:      "",         # class: 'vg' - to be revised
        Name.Variable.Instance:    "",         # class: 'vi' - to be revised

        Number:                    FOREGROUND, # class: 'm'
        Number.Float:              "",         # class: 'mf'
        Number.Hex:                "",         # class: 'mh'
        Number.Integer:            "",         # class: 'mi'
        Number.Integer.Long:       "",         # class: 'il'
        Number.Oct:                "",         # class: 'mo'

        Literal:                   GREEN,    # class: 'l'
        Literal.Date:              "",       # class: 'ld'

        String:                    GREEN,       # class: 's'
        String.Backtick:           "",          # class: 'sb'
        String.Char:               FOREGROUND,  # class: 'sc'
        String.Doc:                COMMENT,     # class: 'sd' - like a comment
        String.Double:             "",          # class: 's2'
        String.Escape:             "",          # class: 'se'
        String.Heredoc:            "",          # class: 'sh'
        String.Interpol:           "",          # class: 'si'
        String.Other:              "",          # class: 'sx'
        String.Regex:              "",          # class: 'sr'
        String.Single:             "",          # class: 's1'
        String.Symbol:             "",          # class: 'ss'

        Generic:                   "",     # class: 'g'
        Generic.Deleted:           PURPLE, # class: 'gd',
        Generic.Emph:              "",     # class: 'ge'
        Generic.Error:             "",     # class: 'gr'
        Generic.Heading:           "",     # class: 'gh'
        Generic.Inserted:          "",     # class: 'gi'
        Generic.Output:            "",     # class: 'go'
        Generic.Prompt:            "",     # class: 'gp'
        Generic.Strong:            "",     # class: 'gs'
        Generic.Subheading:        "",     # class: 'gu'
        Generic.Traceback:         "",     # class: 'gt'
    }
