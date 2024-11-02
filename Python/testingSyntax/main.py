import random as rn
import Character as Character

def main():
    a = Character.Character("test", ["test", "test"], ["hi", "hello", "bye"])
    while True:
        tx = a.Chat(input("you: "))
        print(a.name + ': ' + tx)
if __name__ == '__main__':
    main()
    