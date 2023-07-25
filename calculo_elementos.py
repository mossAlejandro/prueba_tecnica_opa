from itertools import combinations

from itertools import combinations

class Element:
    def __init__(self, name, weight, calories):
        self.name = name
        self.weight = weight
        self.calories = calories

def find_optimal_elements(elements, min_calories, max_weight):
    n = len(elements)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if elements[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - elements[i - 1].weight] + elements[i - 1].calories)
            else:
                dp[i][w] = dp[i - 1][w]
    optimal_elements = []

    w = max_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            optimal_elements.append(elements[i - 1])
            w -= elements[i - 1].weight

    return optimal_elements

if __name__ == "__main__":
    elements = []

    # Solicitar al usuario que ingrese los elementos
    amount = int(input("Cuantos elementos tiene? : "))
    for i in range(amount):
        name = input("Ingrese el nombre del elemento: ")
        weight = int(input("Ingrese el peso del elemento "+ name + ":"))
        calories = int(input("Ingrese las calorías del elemento "+  name +":"))
        elements.append(Element(name, weight, calories))

    min_calories = int(input("Ingrese la cantidad mínima de calorías requeridas: "))
    max_weight = int(input("Ingrese el peso máximo permitido: "))

    optimal_elements = find_optimal_elements(elements, min_calories, max_weight)

    if optimal_elements:
        print("Conjunto óptimo de elementos:")
        for element in optimal_elements:
            print(element.name)
    else:
        print("No se encontró una combinación que cumpla con los requisitos. Por favor intente nuevamente")
