#LTTG (c) TheSkyler-Dev, Licensed under MIT License

import itertools
import re

# --- Node Classes ---

class LTTG:
    def __init__ (self, expression):
        self.expression = expression
        self.variables = self.extract_variables()

    def eval_var(self):
        """Evaluate unique variables from boolean expression."""
        return sorted(set(re.findall(r'\b[a-z]\b', self.expression)) - {'x'})
    
    def eval_expr(self, expression, values):
        """Evaluate the expression with the given variables."""
        for var, val in values.items():
            expression = re.sub(rf'\b{var}\b', str(val), expression)

        # replace logical operators with Python equivalents
        expression = expression.replace('AND', 'and')
        expression = expression.replace('OR', 'or')
        expression = expression.replace('NOT', 'not')
        expression = expression.replace('NAND', 'not (').replace(')', ')')
        expression = expression.replace('NOR', 'not (').replace(')', ')')
        expression = expression.replace('XOR', '^')

        # Evaluate the expression
        return eval(expression)
    
    def generate_TruthTable(self):
        """Generate a truth table for the expression."""
        table = []
        headers = self.variables + ['Result']