from customtkinter import *
from PIL import Image
from core.resource import resource_path

background_color = "#0B0F14"
hover_buttons_color = "#334155"
user_message_box_color = '#1E40AF'
prompt_box_color = '#1A2332'
text_color = '#E6EDF3'
text_font = 'JetBrainsMono'

class StartUI():
    def __init__(self):
        self.win = CTk(fg_color=background_color)
        self.win.title("Euler v0.6")
        
        self.win.iconbitmap(resource_path("assets/logo/logo.ico"))
        
        self.win.geometry("900x400+400+250")
        self.win.resizable(True, True)
        self.win.minsize(width=700, height=300)

        #Later use of logo for more designing and better UI
        # self.logo = CTkImage(light_image=Image.open("assets/logo/Logo.png"), size=(120,120))
        # self.logo_label = CTkLabel(self.win, image=self.logo, text='')
        # self.logo_label.pack(pady=15)

        self.bottom_frame = CTkFrame(self.win, fg_color=prompt_box_color) #corner_radius=20)

        self.prompt_entry = CTkEntry(self.bottom_frame,
                                    placeholder_text='Waiting for your command, sir',
                                    height=45,
                                    text_color=text_color,
                                    fg_color='transparent',
                                    border_color=prompt_box_color,
                                    font=(text_font, 15),
                                    # corner_radius=20
                                    )   
    
        self.chat = CTkScrollableFrame(self.win, fg_color=background_color)

        #Key bindings
        self.prompt_entry.bind("<Return>", self.send_command)
        self.on_send = None

        self.voice_button = CTkButton(self.bottom_frame, 
                        text='🎙',
                        width=60,
                        height=30,
                        text_color=text_color,
                        fg_color=prompt_box_color,
                        hover_color= hover_buttons_color,
                        font=(text_font, 30)
                        )

        self.send_button = CTkButton(self.bottom_frame, 
                        command=self.send_command,
                        text='➤',
                        width=100,
                        height=30,
                        text_color=text_color,
                        fg_color=prompt_box_color,
                        hover_color= hover_buttons_color,
                        font=(text_font, 30)
                        )

        self.bottom_frame.pack(side='bottom', fill='x', padx=30, pady=30)
        self.chat.pack(side='top', expand=True, fill='both')
        self.prompt_entry.pack(side='left', expand=True, fill='x')
        self.send_button.pack(side='right')
        self.voice_button.pack(side='right')

    def show_user_messages(self, prompt):
        user_prompt_row = CTkFrame(self.chat, 
                                   fg_color='transparent',
                                   corner_radius=20
                                   )

        user_prompt_frame = CTkFrame(user_prompt_row, 
                                    fg_color=user_message_box_color,
                                    corner_radius=20
                                    )
        
        user_prompt_label =CTkLabel(user_prompt_frame,
                                    text=prompt,
                                    fg_color='transparent',
                                    font=('Segoe UI', 18)
                                    )
        
        user_prompt_row.pack(side='top', expand=True, fill='x')
        user_prompt_frame.pack(side='right')
        user_prompt_label.pack(padx=10, pady=10)

    def show_euler_messages(self, output):
        euler_prompt_row = CTkFrame(self.chat, 
                                   fg_color='transparent',
                                   corner_radius=20
                                   )

        euler_prompt_frame = CTkFrame(euler_prompt_row, 
                                    fg_color='transparent',
                                    corner_radius=20
                                    )
        
        euler_prompt_label =CTkLabel(euler_prompt_frame,
                                    text=output,
                                    fg_color='transparent',
                                    font=('Segoe UI', 18)
                                    )
        
        euler_prompt_row.pack(side='top', expand=True, fill='x')
        euler_prompt_frame.pack(side='left')
        euler_prompt_label.pack(padx=10, pady=30)

    def send_command(self, event=None):
        prompt = self.prompt_entry.get()

        if not prompt: #Equivalent to if len(prompt) == 0: or if prompt = '':
            return
        
        self.show_user_messages(prompt)
        self.prompt_entry.delete(0, END)

        if self.on_send: #Currently, falsy value as it is None right now so it doesn't run but when later connected with manager.py it becomes = handle_prompt so this becomes a truthy value
            response = self.on_send(prompt)
            self.show_euler_messages(response)

    def send_voice_activation():
        ...
    
    def run(self):
        self.win.mainloop()