# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Jack Bauer", "Nowhere")
greet_with(location="Everywhere", name="Jack Bauer")
