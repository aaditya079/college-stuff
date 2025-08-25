from itertools import permutations

def solve_cryptarithmetic(puzzle):
    term1, term2, result = puzzle

    unique_chars = set(char for word in puzzle for char in word if char.isalnum())
    unique_chars = sorted(unique_chars)
    for digits in permutations(range(10), len(unique_chars)):
        char_to_digit = {char: digit for char, digit in zip(unique_chars, digits)}
   
        numeric_term1 = int("".join(str(char_to_digit[char]) for char in term1))
        numeric_term2 = int("".join(str(char_to_digit[char]) for char in term2))
        numeric_result = int("".join(str(char_to_digit[char]) for char in result))
        if any(word[0]=='0' and len(word)>1 for word in [term1,term2,result]):
               continue
        if numeric_term1 + numeric_term2 == numeric_result:
            return char_to_digit    
    return None

if __name__ == "__main__":
    puzzle = ('CAR', 'BUS', 'TRUCK')
    solution = solve_cryptarithmetic(puzzle)    
    if solution:
        term1_num = "".join(str(solution[char]) for char in puzzle[0])
        term2_num = "".join(str(solution[char]) for char in puzzle[1])
        result_num = "".join(str(solution[char]) for char in puzzle[2])
        print(f"{term1_num}+{term2_num}={result_num}")
    else:
        print("No solution found.")
