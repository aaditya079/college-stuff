from itertools import permutations

def solve_cryptarithmetic(puzzle):
    term1, term2, result = puzzle

    # Collect all unique characters
    unique_chars = set(term1 + term2 + result)
    if len(unique_chars) > 10:
        return None  # Not solvable with digits 0–9

    unique_chars = sorted(unique_chars)

    for digits in permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, digits))

        # No leading zeros
        if (char_to_digit[term1[0]] == 0 or
            char_to_digit[term2[0]] == 0 or
            char_to_digit[result[0]] == 0):
            continue

        # Convert words to numbers
        num1 = int("".join(str(char_to_digit[c]) for c in term1))
        num2 = int("".join(str(char_to_digit[c]) for c in term2))
        num_result = int("".join(str(char_to_digit[c]) for c in result))

        if num1 + num2 == num_result:
            return char_to_digit

    return None

if __name__ == "__main__":
    puzzle = ('CAR', 'BUS', 'TRUCK')
    solution = solve_cryptarithmetic(puzzle)
    if solution:
        term1_num = "".join(str(solution[c]) for c in puzzle[0])
        term2_num = "".join(str(solution[c]) for c in puzzle[1])
        result_num = "".join(str(solution[c]) for c in puzzle[2])
        print(f"{term1_num} + {term2_num} = {result_num}")
    else:
        print("No solution found.")
