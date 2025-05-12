# LTTG
LTTG, or Logic Truth Table Generator is a CLI tool that generates truth tables for boolean algebra with logic gates from a given scheme. The tool is written in Python and may later be rewritten or ported in Lisp.

## How it works
LTTG takes a boolean expression, parses it with tokenization and then generates a truth table based on the expression. LTTG also accounts for De Morgan's Laws and also prints corresponding expression simplifications.

The input should look similar to this:

```plaintext
(a OR b) AND (c OR d)
```

## Input Syntax
This tool supports the following logic operators:
- `AND`
- `OR`
- `NOT`

### Unsupported Gates
For unsupported gates like `XOR`, `NAND`, and `NOR`, you can rewrite them using `AND`, `OR`, and `NOT`:

- `A XOR B` → `(A AND NOT B) OR (NOT A AND B)`
- `A NAND B` → `NOT (A AND B)`
- `A NOR B` → `NOT (A OR B)`