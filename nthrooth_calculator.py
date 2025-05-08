'''
This program calculates the nth root of a given value using the Newton-Raphson method.
It handles edge cases such as negative values and zero roots.
It also includes error handling for invalid inputs.


Author: Francis Mike John Camogao
Date: 8, May 2025
'''

def nth_rooth(value: float, degree: float) -> float:
    try: 
        if degree == 0:
            raise ValueError("Root degree cannot be zero.")
        if value < 0 and degree % 2 == 0:
            raise ValueError("Cannot compute even root of a negative number.")
        
        guess     = value / degree if value != 0 else 0.0
        tolerance = 1e-10  # Set a tolerance for convergence
        
        while True:
            next_guess: float = ((degree - 1) * guess + value / (guess ** (degree - 1))) / degree
            if abs(next_guess - guess) < tolerance:
                return next_guess
            guess: float = next_guess
            
            print(f"{get_input_root:.0f}-th root of {get_input_value} is {guess}") #the final print result is the final guess
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    get_input_root  = float(input("Enter root: "))
    get_input_value = float(input("Enter value: "))
    nth_rooth(get_input_value, get_input_root)