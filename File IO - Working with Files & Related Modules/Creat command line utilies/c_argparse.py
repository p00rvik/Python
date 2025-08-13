import argparse
par = argparse.ArgumentParser(description="Simple Calaculator")
par.add_argument("num1", type=float, help="First number")
par.add_argument("num2", type=float, help="Second number")
par.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
args = par.parse_args()
print(args)
if args.operation == "add":
    print(args.num1 + args.num2)    
elif args.operation == "subtract":
    print(args.num1 - args.num2)    
elif args.operation == "multiply":
    print(args.num1 * args.num2)
elif args.operation == "divide":
    if args.num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(args.num1 / args.num2)
else:
    print("Invalid operation")
    
    