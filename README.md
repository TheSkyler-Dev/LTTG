# LTTG
LTTG, or Logic Truth Table Generator is a CLI tool that generates truth tables for boolean algebra with logic gates from a given scheme. The tool is written in Python and may later be rewritten or ported in Lisp.

## How it works
LTTG takes a boolean expression, parses it with tokenization and then generates a truth table based on the expression. LTTG also accounts for De Morgan's Laws and also prints corresponding expression simplifications.

The input should look similar to this:

```plaintext
(a OR b) AND (c OR d)
```

## Input syntax
This section outlines the general input syntax for LTTG:

- Channels/Variables: any lowercase single letter (preferably in alphabetic order, `x` is reserved for output)
- Logic Operators: `AND`, `OR`, `NAND`, `XOR`, `NOR`, `NOT`
- negated values: e.g. `(NOT a)`