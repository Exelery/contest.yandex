'''Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n,
упорядоченные лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).
В задаче используются только круглые скобки.
Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных
последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.'''

def foo(string, left, right, pairs):
    if left == pairs and right == pairs:
        print(string)
    else:
        if left < pairs:
            foo(string + '(', left + 1, right, pairs)
        if right < left:
            foo(string + ')', left, right + 1, pairs)

number = int(input())

foo('', 0, 0, number)
