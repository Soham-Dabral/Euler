from core.router import handle_prompt
from core.response_builder import handle_response
from memory.logger import log
from ui.ui import StartUI

def process_prompt(prompt):
    facts, error = handle_prompt(prompt)
    response = handle_response(facts, error)
    log(prompt, response, error)
    return response

def manager():
    ui = StartUI()
    ui.show_euler_messages("Euler v0.6 initialization complete... \nGood day, user. I trust you are having a pleasant day.")
    ui.on_send = process_prompt
    ui.run()
