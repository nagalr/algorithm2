# Faster option O(n) run, O(n) space
def recurring_counter(input):
    numbers = set()

    for item in input:
        if item in numbers:
            return item
        else:
            numbers.add(item)


# Slow option O(n^2) run, O(1) space
def recurring_counter2(input):
    input_length = len(input)
    found_recurring = None
    i = 0

    while i < input_length:
        j = i + 1
        while j < input_length:
            if input[i] == input[j]:
                input_length = j  # shorten the list
                found_recurring = input[j]
            else:
                j += 1
        i += 1

    return found_recurring


# item index [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
given_list = [3, 2, 1, 1, 2, 3, 5, 2, 6, 2]
print(recurring_counter2(given_list))

'''
Explain run(recurring_counter2) on the given input(given_list):
- First and second 'while' will loop over the list
- First iteration of the second 'while' will find recurring 3 at idx 5
- A shorten of the list will occur (to the value of 3, idx 5)
- Now the question is: Do we have a recurring in the sublist?
- If we do, that means that we have a shorter recurring number
- Continue and find recurring of 2 in idx 4, shorten to a sublist
- Do we have another recurring in the new sublist?
- Continue to find recurring of 1 in idx 3, shorten and finish
'''
