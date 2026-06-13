from core.router import handle_prompt
from memory.logger import log
from core.response_builder import handle_response

def main():
    print("Euler v0.4 initialization complete... \n")
    print("Good day, sir. I trust you are having a pleasant day.")
    while True:
        prompt = input(">>> ").strip().lower()
        if prompt in ["exit", "quit"]:
            response = "Have a great day sir\n"
            error = None
            print(response)
            log(prompt, response, error)
            break

        else:
            facts, error = handle_prompt(prompt)
            response = handle_response(facts)
            print(response)
            log(prompt, response, error)

if __name__ == "__main__":
    main()
