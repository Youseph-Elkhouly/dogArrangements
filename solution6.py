def dogArrangements(nPassive, nAggressive):
    # The problem has a more complex solution involving  (which I have some prior knowledge in). The key insight is to calculate
    # the number of ways aggressive dogs can be placed between passive dogs (including at the ends)
    # and then multiply by the permutations of each group of dogs since they are distinguishable.

    # If there are more aggressive dogs than can be separated by passive dogs, return 0.
    if nAggressive > nPassive + 1:
        return 0

    # Factorial helper function to calculate permutations
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    # Calculate the permutations of passive and aggressive dogs
    permPassive = factorial(nPassive)
    permAggressive = factorial(nAggressive)

    # The number of slots where aggressive dogs can be placed is nPassive + 1 (between and at the ends of passive dogs)
    # For each aggressive dog, we choose a slot, which is a combinatorial problem: C(slots, nAggressive)
    slots = nPassive + 1

    # Calculate combinations of choosing nAggressive slots out of available slots
    def combinations(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    # Total arrangements is the product of combinations of slots for aggressive dogs and permutations of each dog type
    totalArrangements = combinations(slots, nAggressive) * permPassive * permAggressive

    return totalArrangements


#Main function to test the solution
def main():
    testArgs = [[0,0,1],[1,1,2],[0,2,0],[2,2,12]]
    for arg in testArgs:
        passive, aggressive, answer = arg
        result = dogArrangements(passive, aggressive)
        if result != answer:
            print(f"Failed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed dogArrangements test with args nPassive={passive} nAggressive={aggressive}.")
    return 0

main()
