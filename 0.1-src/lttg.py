#LTTG (c) TheSkyler-Dev, Licensed under MIT License

import itertools
import re

# --- Node Classes ---

# noinspection SpellCheckingInspection
class LTTG:
    def __init__ (self, expression):
        self.expression = expression
        self.variables = self.eval_var()

    def eval_var(self):
        """Evaluate unique variables from boolean expression."""
        return sorted(set(re.findall(r'\b[a-z]\b', self.expression)) - {'x'})
    
    @staticmethod
    def eval_expr(expression, values):
        """Evaluate the expression with the given variables."""
        for var, val in values.items():
            expression = re.sub(rf'\b{var}\b', str(val), expression)

        # Replace logical operators with Python equivalents
        expression = re.sub(r'\bAND\b', 'and', expression)
        expression = re.sub(r'\bOR\b', 'or', expression)
        expression = re.sub(r'\bNOT\b', 'not', expression)

        # Evaluate the expression
        return eval(expression)
    
    def generate_truth_table(self):
        """Generate a truth table for the expression."""
        table = []
        headers = self.variables + ['Result']
        combinations = list(itertools.product([0, 1], repeat=len(self.variables)))

        for combination in combinations:
            values = dict(zip(self.variables, combination))
            result = self.eval_expr(self.expression, values)
            table.append(list(combination) + [int(result)])

        return headers, table
    
    def print_truth_table(self):
        """Print the truth table with formatted output."""
        headers, table = self.generate_truth_table()

        # Print headers
        print(' | '.join(headers))
        print('-' * (len(headers) * 4))

        # Print rows with formatting
        for row in table:
            formatted_row = [
                f"\033[41m{val}\033[0m" if val == 0 else f"\033[1;42m{val}\033[0m"
                for val in row
            ]
            print(' | '.join(formatted_row))


# noinspection SpellCheckingInspection
class Main:
    def __init__(self):
        self.lttg = None

    def run(self):
        expression = input("Enter a boolean expression: ")
        self.lttg = LTTG(expression)
        self.lttg.print_truth_table()

if __name__ == "__main__":
    Main().run()