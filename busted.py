from ttkbootstrap import Style
from tkinter import ttk

help_str = 'YOU BUSTED!\nYou lose the game!!'

style = Style(theme='flatly')
root = style.master
root.title('YOU LOSE')
ttk.Label(root, text='You Lose!',
          font=('Helvetica', 12)).pack(pady=10, padx=5)
ttk.Label(root, text=help_str).pack(padx=5)
ttk.Button(root,
           text="Ok",
           style='primary.TButton',
           command=lambda: root.destroy()).pack(side='bottom', padx=5, pady=10)
root.mainloop()
