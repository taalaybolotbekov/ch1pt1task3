def is_odd(b):
    b=int(input("vvedite chislo"))
    if b % 2 == 0:
        return False
    else:
        return True
# for i in range (25):
print(is_odd(8))


# DO NOT remove lines below here, this is designed to test your code. 

def test_is_odd():
    assert is_odd (2) == False
    assert is_odd (3) == True
    assert is_odd (8) == False
    assert is_odd (100) == False
    assert is_odd (101) == True
print("YOUR CODE IS CORRECT!")

# test your code by un-commenting the line(s) below test_is_odd()
