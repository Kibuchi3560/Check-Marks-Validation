# marks = input(int(What is your marks?))
def InputCheck():
    try:
        marks = float(input("What is your marks?"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
    return marks

def ValidateInput(marks):
    
    if isinstance(marks, (int, float)):
        if marks < 0:
            print("Underscale")
        elif marks >= 50 and (marks < 100):
            print("Pass")
        elif marks > 100:
            print(f"Marks should be less than 100, you entered {marks}")
        else:
            print("Fail")
    else:   
        print("Input should be an an integer or a decimal")

I = InputCheck()
ValidateInput(I)

            
  


