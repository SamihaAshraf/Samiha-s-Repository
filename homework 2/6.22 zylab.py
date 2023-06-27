#Samiha Ashraf
#1884227
def find_integer_solution(a, b, c, d, e, f):
    solutions = [(x, y) for x in range(-10, 11) for y in range(-10, 11) if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2]
    return solutions[0] if solutions else None


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


solution = find_integer_solution(a, b, c, d, e, f)


if solution is None:
    print("No solution")
else:
    print(solution[0], solution[1])