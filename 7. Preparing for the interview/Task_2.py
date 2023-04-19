from Task_1 import Stack

noraml_list = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}"]
abnormal_list = ["}{}", "{{[(])]}}", "[[{())}]"]


def check_string(query):
    stack = Stack()
    if len(query) % 2 != 0:
        return False
    else:
        for i in query:
            if i in "([{":
                stack.push(i)
            elif i not in "([{":
                if stack.peek() == "(" and i == ")":
                    stack.pop()
                elif stack.peek() == "[" and i == "]":
                    stack.pop()
                elif stack.peek() == "{" and i == "}":
                    stack.pop()
                else:
                    return False
            else:
                return False
    return True


if __name__ == "__main__":
    for query in noraml_list + abnormal_list:
        if check_string(query):
            print(f"{query:<22} | Сбалансировано")
        else:
            print(f"{query:<22} | Несбалансировано")
