def get_elements():
    
    elements_count = int(input().strip())
    elements = input().strip().split()
    
    return elements_count, set(elements)

def get_operations():
    operations = []
    operations_number = int(input().strip())
    
    for _ in range(operations_number):
        operation = input().strip().split()
        if operation:
            operations.append({"operation":operation[0], "value":int(operation[1]) if len(operation)==2 else None})
    return operations

def execute_operations(elements:set,operations:list):
    
    for operation in operations:
        if operation["operation"] == "pop":
            elements.pop()
        elif operation["operation"] == "remove" and operation["value"] in elements:
            elements.remove(operation["value"])
        elif operation["operation"] == "discard":
            elements.discard(operation["value"])
    return elements
    
def main():
    
    elements_count, elements = get_elements()
    operations = get_operations()
    
    execute_operations(elements, operations)
    print(sum(elements))
        
    
if __name__ == "__main__":
    main()