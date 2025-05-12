#LTTG (c) TheSkyler-Dev, Licensed under MIT License

import itertools
import re

# --- Node Classes ---

class LTTG:
    def __init__ (self, expression):
        self.expression = expression
        self.variables = self.eval_var()

    def eval_var(self):
        """Evaluate unique variables from boolean expression."""
        return sorted(set(re.findall(r'\b[a-z]\b', self.expression)) - {'x'})
    
    def eval_expr(self, expression, values):
        """Evaluate the expression with the given variables."""
        for var, val in values.items():
            expression = re.sub(rf'\b{var}\b', str(val), expression)

        # Replace logical operators with Python equivalents
        expression = re.sub(r'\bAND\b', 'and', expression)
        expression = re.sub(r'\bOR\b', 'or', expression)
        expression = re.sub(r'\bNOT\b', 'not', expression)

        # Evaluate the expression
        return eval(expression)
    
    def generate_TruthTable(self):
        """Generate a truth table for the expression."""
        table = []
        headers = self.variables + ['Result']
        combinations = list(itertools.product([0, 1], repeat=len(self.variables)))

        for combination in combinations:
            values = dict(zip(self.variables, combination))
            result = self.eval_expr(self.expression, values)
            table.append(list(combination) + [int(result)])

        return headers, table
    
    def print_TruthTable(self):
        """Print the truth table."""
        headers, table = self.generate_TruthTable()
        print(' | '.join(headers))
        print('-' * (len(headers) * 4))
        for row in table:
            print(' | '.join(map(str, row)))

class main:
    def __init__(self):
        self.lttg = None

    def run(self):
        expression = input("Enter a boolean expression: ")
        self.lttg = LTTG(expression)
        self.lttg.print_TruthTable()

if __name__ == "__main__":
    main().run()