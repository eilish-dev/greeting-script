def greet(names):
    try:
        if not names:
            return "No names provided"
        for name in names:
            print(f"Hello, {name}!")
        return "Greetings complete"
    except TypeError:
        return "Invalid input"
    
print(greet(["Alice", "Bob"]))    
print(greet([]))
print(greet(123))