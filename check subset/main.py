def read_input_data():
    
    tests = []
    tests_count = int(input().strip())
    for _ in range(tests_count):
        set_a_length = int(input())
        set_a = set([int(number) for number in input().strip().split()])
        set_b_length = int(input())
        set_b = set([int(number) for number in input().strip().split()])
        tests.append({"a":set_a,"b":set_b})
    return tests



def main():
    tests = read_input_data()
    for test in tests:
        print(True) if test["a"].issubset(test["b"]) else print(False)
if __name__ == "__main__":
    main()    