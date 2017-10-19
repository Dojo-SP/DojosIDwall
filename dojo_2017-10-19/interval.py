# Problema: Intervalos
#
# http://dojopuzzles.com/problemas/exibe/intervalos/
#
# Dado uma lista de números inteiros,
# agrupe a lista em um conjunto de intervalos
#
# Exemplo:
# Entrada: 100, 101, 102, 103, 104, 105,
#          110, 111, 113, 114, 115, 150
# Saída: [100-105], [110-111], [113-115], [150]

def interval(values):
    if values == []:
        return []
    elif len(values) == 2 and values[0] + 1 == values[1]:
        return [values]
    elif len(values) == 2 and values[1] + 1 == values[0]:
        return [values[::-1]]

    elif len(values) == 2:
        if values[1] < values[0]:
           values = values[::-1]

        return [[values[0]], [values[1]]]
    return [values]


def test_one_number():
    assert interval([200]) == [[200]]
    assert interval([150]) == [[150]]
    assert interval([100]) == [[100]]
    assert interval([90]) == [[90]]

def test_no_number():
    assert interval([]) == []

def test_two_numbers():
    assert interval([115, 150]) == [[115], [150]]
    assert interval([117, 140]) == [[117], [140]]
    assert interval([119, 130]) == [[119], [130]]
    assert interval([150, 115]) == [[115], [150]]
    assert interval([140, 117]) == [[117], [140]]
    assert interval([130, 119]) == [[119], [130]]

def test_two_consecutive():
    assert interval([110, 111]) == [[110, 111]]
    assert interval([113, 114]) == [[113, 114]]
    assert interval([114, 113]) == [[113, 114]]
