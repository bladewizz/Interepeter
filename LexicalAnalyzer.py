import re


class LexicalAnalyzer:
    # Token row
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('MAIN', r'main'),          # main
             ('id', r'[a-zA-Z]\w*'),   # id
            ('literal_integer', r'\d(\d)*'),
             ('le_operator', r'<='),
             ('lt_operator', r'<'),
             ('ge_operator', r'>='),
             ('gt_operator', r'>'),
             ('eq_operator', r'=='),
             ('assignment_operator', r'='),
             ('ne_operator', r'~='),
             ('add_operator', r'\+'),
             ('sub_operator', r'\-'),
             ('mul_operator', r'\*'),
             ('div_operator', r'\/'),
             ('INT', r'int'),            # int
            # ('FLOAT', r'float'),        # float
            # ('STRING', r'string'),      # string
            # ('S_LIT', r'"[a-zA-Z]\w*"'),# string literal
            # ('IF', r'if'),              # if
            # ('ELSE', r'else'),          # else"
            # ('WHILE', r'while'),        # while
            # ('READ', r'read'),          # read
            # ('PRINT', r'print'),        # print
            # ('LBRACKET', r'\('),        # (
            # ('RBRACKET', r'\)'),        # )
            # ('LBRACE', r'\{'),          # {
            # ('RBRACE', r'\}'),          # }
            # ('COMMA', r','),            # ,
            # ('SEMICOLON', r';'),           # ;
             ('EQ', r'=='),              # ==
            # ('NE', r'!='),              # !=
            # ('LE', r'<='),              # <=
            # ('GE', r'>='),              # >=
            # ('OR', r'\|\|'),            # ||
            # ('AND', r'&&'),             # &&
             ('ATTR', r'\='),            # =
            # ('LT', r'<'),               # <
            # ('GT', r'>'),               # >
            # ('ADD_OP', r'\+'),            # +
            # ('HYPHEN', r'-'),            # -
            # ('MULT', r'\*'),            # *
            # ('DIV', r'\/'),             # /
            # ('ID', r'[a-zA-Z]\w*'),     # IDENTIFIERS
            # ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            # ('INTEGER_CONST', r'\d(\d)*'),          # INT
             ('NEWLINE', r'\n'),         # NEW LINE
             ('SKIP', r'[ \t]+'),        # SPACE and TABS
            # ('MISMATCH', r'.'),         # ANOTHER CHARACTER
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0

        # Lists of output for the program
        token = []
        lexeme = []
        row = []
        column = []

        # It analyzes the code to find the lexemes and their respective Tokens
        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                lin_start = m.end()
                self.lin_num += 1
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
            else:
                    col = m.start() - lin_start
                    column.append(col)
                    token.append(token_type)
                    lexeme.append(token_lexeme)
                    row.append(self.lin_num)
                    # To print information about a Token
                    print('Token = {0}, Lexeme = \'{1}\', Line Number = {2}'.format(token_type, token_lexeme, self.lin_num))

        return token, lexeme, row, column,
