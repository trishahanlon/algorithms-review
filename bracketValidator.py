def is_valid(code):
    # openers_to_closers = {
    #     '(': ')',
    #     '{': '}',
    #     '[': ']',
    # }
    #
    # openers = set(openers_to_closers.keys())
    # closers = set(openers_to_closers.values())

    openers = ['(', '{', '[']
    closers = [')', '}', ']']

    corresponding_dict = {'(': ')', '{': '}', '[': ']'}

    openers_stack = []

    for char in code:
        if char in openers:
            openers_stack.append(char)
            print('adding to the openers stack:', openers_stack)
        elif char in closers:
            if not openers_stack:
                print("We didn't find a corresponding opening bracket, Error!")
                return False
            else:
                last_unclosed_opener = openers_stack.pop()
                print("popping the last opener, because we found a closer")
                print(last_unclosed_opener)
                # if this closer doesn't correspond to the most
                # recently seen unclosed opener, short-circuit, return False
                if corresponding_dict[last_unclosed_opener] != char:
                    print("oops, you didn't close the right character", char)
                    return False

    return openers_stack == []


print(is_valid("here {[opened and ()then closed]}"))
