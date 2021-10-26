from ttkbootstrap import Style
from tkinter import ttk

help_str = '''The object of blackjack is to get the closest score to 21 without going over.\n\nHow to play:\n\tTo hit (get another card), press h\n\tTo stay (your turn is done, dealer goes), press s\n\tTo leave the game, press esc or q'''

style = Style(theme='flatly')
root = style.master
root.title('Blackjack Help')
ttk.Label(root, text='Help for Python Blackjack',
          font=('Helvetica', 12)).pack(pady=10, padx=5)
ttk.Label(root, text=help_str).pack(padx=5)
ttk.Button(root,
           text="Ok",
           style='primary.TButton',
           command=lambda: root.destroy()).pack(side='bottom', padx=5, pady=10)
root.mainloop()
