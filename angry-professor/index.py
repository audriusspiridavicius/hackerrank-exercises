
def angryProfessor(k, a):
    
    
    students_on_time = sum([1 for t in a if t < 1])
    
    if students_on_time >= k:
        return "NO"
    else:
        return "YES"
    
if __name__ == "__main__":
    print(angryProfessor(2,[1, 1, 1, 5, 6, 2, 3]))
    print(angryProfessor(2,[1, 1, 1, 0, 6, 2, 3]))
    print(angryProfessor(2,[1, 1, 1, 0, 6, 2, -3]))