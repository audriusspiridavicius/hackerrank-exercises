def getMoneySpent(keyboards, drives, budget):

    total_spent_values = [keyboard + drive for keyboard in keyboards for drive in drives if keyboard + drive <= budget]
    if not total_spent_values: total_spent_values = [-1]
    return max(total_spent_values)


if __name__ == "__main__":
    print(getMoneySpent([3,1],[5, 2, 8], 10))