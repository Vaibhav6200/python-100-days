def greet(name):
    print(f"Hello {name}")
    print("How are you")
    print("Congratulations you have made till day 8")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Your Location: {location}")

greet("Vaibhav")
greet_with("Vaibhav", "Ahmedabad")

greet_with(location="Ahmedabad", name="Vaibhav")
