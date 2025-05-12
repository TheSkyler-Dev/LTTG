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

### Unsupported Operators
For unsupported operators like `XOR`, `NAND`, and `NOR`, you can rewrite them using `AND`, `OR`, and `NOT`:

- `a XOR b` → `(a AND NOT b) OR (NOT a AND b)`
- `a NAND b` → `NOT (a AND b)`
- `a NOR b` → `NOT (a OR b)`
