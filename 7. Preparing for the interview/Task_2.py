from Task_1 import Stack

noraml_list = ["(((([{}]))))", "[([])((([[[]]])))]{()}", "{{[()]}}"]
abnormal_list = ["}{}", "{{[(])]}}", "[[{())}]"]


# def check_string(query):
#     stack = Stack()
#     for elem in query:
#         if elem in stack:
#             stack.push(elem)
#         elif elem ==


if __name__ == "__main__":
    r = True
    while r:
        x = "[([])((([[[]]])))]{()}"
        res = x.replace("{}", "")
        res_1 = res.replace("[]", "")
        print(res_1)