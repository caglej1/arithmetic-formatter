'''
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
'''

def arithmetic_arranger(probs, ans=False) :
    if len(probs) > 5 :
        return "Error: Too many problems."

    # Store all operators and verify only + or - operation
    operators = list(map(lambda arg : arg.split()[1], probs))
    if not set(operators).issubset({'+','-'}) :
        return "Error: Operator must be '+' or '-'."

    # Store all operands, verify operands are only digits and <= 4 digits
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

    # Math and formatting
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

    if ans:
        return('\n'.join((op1_row, op2_row, dashes_row, solutions_row)))
    else:
        return('\n'.join((op1_row, op2_row, dashes_row)))
