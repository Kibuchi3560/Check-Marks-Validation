# marks = input(int(What is your marks?))
def InputCheck():
    try:
        marks = float(input("What is your marks?"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None
    

def ValidateInput(marks):
    if marks is None:
        return
    
    if marks < 0:
        print("Underscale")
    elif marks >= 50 and (marks <= 100):
        print("Pass")
    elif marks > 100:
        print(f"Marks should be less than 100, you entered {marks}")
    else:
        print("Fail")
    


ValidateInput(InputCheck())

            
  


