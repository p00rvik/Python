def example_func(required, *args, **kwargs):
    print(f"Required parameter: {required}")
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

example_func(1, 2, 3, a=4, b=5)
