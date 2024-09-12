import sys

def default():
    print("Hello Chris")


def dog():
    print("woof")

def cat():
    print("meow")

def main():
    animal_name: str = sys.argv
    if animal_name and animal_name[1].lower() == "cat":
        cat()
    elif animal_name and animal_name[1].lower() == "dog":
        dog()
    else:
        default()

if __name__ == "__main__":
    main()
