# Overview
Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.
## Example
### Function Call:
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
### Output:
```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```
### Function Call:
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
### Output:
```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
## Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.
  * Situations that will return an error:
    * If there are too many problems supplied to the function. The limit is five, anything more will return: `Error: Too many problems.`
    * The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: `Error: Operator must be '+' or '-'.`
    * Each number (operand) should only contain digits. Otherwise, the function will return: `Error: Numbers must only contain digits.`
    * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: `Error: Numbers cannot be more than four digits.`
  * If the user supplied the correct format of problems, the conversion you return will follow these rules:
    * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    * Numbers should be right-aligned.
    * There should be four spaces between each problem.
    * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
## My Solution
First, I declare a function that accepts two parameters:
  * `probs` is a list of strings that are arithmetic problems.
  * `ans` is an optional boolean that when `True`, includes the solutions to the arithmetic problems in the formatted output. By default, `ans` is set to `False`.
```python
def arithmetic_arranger(probs, ans=False) :
```

I verify that the maximum number of problems is not exceeded.
```python
if len(probs) > 5 :
    return "Error: Too many problems."
```

I verify that only addition or subtraction is being performed. I store the operators in a list.
```python
operators = list(map(lambda arg : arg.split()[1], probs))
if not set(operators).issubset({'+','-'}) :
    return "Error: Operator must be '+' or '-'."
```

I verify that all operands are comprised of only digits and do not contain more than 4 digits. I store the operands in a list.
```python
operands = []
for i in probs:
    ops = i.split()
    if ops[0].isdigit() and ops[-1].isdigit():
        if len(ops[0]) > 4 or len(ops[-1]) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            operands.extend([ops[0], ops[-1]])
    else:
        return "Error: Numbers must only contain digits."
```

I perform the arithmetic and format the output according to the rules previously stated.
```python
op1_row = ''
op2_row = ''
dashes_row = ''
solutions_row = ''
four_spaces = ' ' * 4
prob_solutions = list(map(lambda arg : eval(arg), probs))

for i in range(0, len(probs)):
    idx_op1 = i * 2
    idx_op2 = i * 2 + 1
    small_op_spaces = max(len(operands[idx_op1]), len(operands[idx_op2])) + 2
    big_op_spaces = small_op_spaces - 1
    op1_row += operands[idx_op1].rjust(small_op_spaces)
    op2_row += operators[i] + operands[idx_op2].rjust(big_op_spaces)
    dashes_row += '-' * small_op_spaces
    solutions_row += str(prob_solutions[i]).rjust(small_op_spaces)
    if i != len(probs) - 1:
        op1_row += four_spaces
        op2_row += four_spaces
        dashes_row += four_spaces
        solutions_row += four_spaces
```

Finally, I return the formatted output.
```python
if ans:
    return('\n'.join((op1_row, op2_row, dashes_row, solutions_row)))
else:
    return('\n'.join((op1_row, op2_row, dashes_row)))
```

Proper execution can be verified by executing the unit tests [here](https://replit.com/@caglej1/boilerplate-arithmetic-formatter#arithmetic_arranger.py).
