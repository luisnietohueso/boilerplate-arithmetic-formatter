def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    dash_line = ""
    answer_line = ""
    
    for problem in problems:
        operand1, operator, operand2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(operand1), len(operand2))

        top_line += operand1.rjust(max_width + 2)
        bottom_line += operator + operand2.rjust(max_width + 1)
        dash_line += "-" * (max_width + 2)

        if operator == '+':
            answer = int(operand1) + int(operand2)
        else:
            answer = int(operand1) - int(operand2)
        answer_line += str(answer).rjust(max_width + 2)

        if problem != problems[-1]:
            top_line += "    "
            bottom_line += "    "
            dash_line += "    "
            answer_line += "    "

    arranged_problems = top_line + "\n" + bottom_line + "\n" + dash_line
    if show_answers:
        arranged_problems += "\n" + answer_line

    return arranged_problems
