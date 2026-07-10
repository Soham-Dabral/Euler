from core.router import handle_prompt
from core.response_builder import handle_response
from memory.logger import log

def main():
    print("\nEuler v0.5 initialization complete... \n")
    print("Good day, sir. I trust you are having a pleasant day.")
    while True:
        prompt = input(">>> ").strip().lower()
        if prompt in ["exit", "quit"]:
            response = "Have a great day sir"
            error = None
            print(response)
            log(prompt, response, error)
            break

        else:
            facts, error = handle_prompt(prompt)
            response = handle_response(facts, error)
            print(response)
            log(prompt, response, error)

if __name__ == "__main__":
    main()
