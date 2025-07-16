def claculator ():
    num1 = float(input("Ennter first number : "))
    operator = input("Enter operator (+,-,*,/):")
    num2 = float(input("Enter second number : "))
    match operator:
        case "+":
            print(f"Result:{num1+num2}")
        case "-":
            print(f"Result:{num1-num2}")
        case "*":
            print(f"Result:{num1*num2}")
        case "/":
            print(f"Result:{num1/num2}")
        case "_":
            print(f"Invalid operator !")

claculator()