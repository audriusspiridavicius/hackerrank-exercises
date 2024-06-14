def get_elements():
    
    elements_count = int(input().strip())
    elements = input().strip().split()
    
    return elements_count, elements

def get_operations():
    operations = []
    operations_number = int(input().strip())
    
    for _ in range(operations_number):
        operation = input().strip().split()
        if operation:
            operations.append({"operation":operation[0], "value":operation[1] if len(operations)==2 else None})
    return operations