#Euler v0.2 main program
#Run this program to run Euler v0.2

from utils.router import handle_prompt

def main():
    print("Euler v1 initialization complete... \n")
    print("Good day, sir. I trust you are having a pleasant day.")
    while True:
        command = input(">>> ").strip().lower()
        if command in ["exit", "quit"]:
            print("Have a great day sir")
            break
        else:
            response = handle_prompt(command)
            print(response)

if __name__ == "__main__":
    main()