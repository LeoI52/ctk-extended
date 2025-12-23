"""
@author : Léo IMBERT
@created : 16/04/2025
@updated : 23/12/2025
"""

from tkinter import Toplevel, Frame
import customtkinter as ctk
import time
import sys

#! ---------------------------------------- EXAMPLE CLASS ---------------------------------------- !#

class WidgetName(ctk.CTkFrame):
    def __init__(self, *args, width:int=100, height:int=32, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

#! ----------------------------------------------------------------------------------------------- !#

#? ---------------------------------------- CLASSES ---------------------------------------- ?#

class CTkSpinbox(ctk.CTkFrame):

    def __init__(self, master, width:int=100, height:int=40, start_value:int=0, min_value:int=0, max_value:int=100, step_value:int=1, scroll_value:int=5, variable=None, font:tuple=('X', 20), fg_color:str=None, border_color:str=('#AAA', '#555'), text_color:str=('Black', 'White'), button_color:str=('#BBB','#444'), button_hover_color:str=('#AAA', '#555'), border_width:int=2, corner_radius:int=5, button_corner_radius:int=5, button_border_width:int=2, button_border_color:str=('#AAA', '#555'), state:str='normal', command=None)-> None:
        super().__init__(master, height=height, width=width, fg_color=fg_color, border_color=border_color, border_width=border_width, corner_radius=corner_radius)

        self.start_value = max(min(start_value, max_value), min_value)
        self.min_value = min_value
        self.max_value = max_value
        self.step_value = abs(step_value)
        self.scroll_value = abs(scroll_value)
        self.variable = variable
        if self.variable:
            self.variable.set(self.start_value)
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.button_hover_color = button_hover_color
        self.button_corner_radius = button_corner_radius 
        self.button_border_width = button_border_width
        self.button_border_color = button_border_color
        self.state = state
        self.command = command

        self.counter_var = ctk.IntVar(value = self.start_value)
        self.counter = ctk.CTkLabel(self, text='Error', textvariable=self.counter_var, font=self.font, text_color=self.text_color)

        self.decrement = ctk.CTkButton(self, text='-', font=self.font, text_color=self.text_color, fg_color=self.button_color, hover_color=self.button_hover_color, text_color_disabled='#888', corner_radius=self.button_corner_radius, border_width=self.button_border_width, border_color=self.button_border_color, command=self.decrement_counter)

        self.increment = ctk.CTkButton(self, text='+', font=self.font, text_color=self.text_color, fg_color=self.button_color, hover_color=self.button_hover_color, text_color_disabled='#888', corner_radius=self.button_corner_radius, border_width=self.button_border_width, border_color=self.button_border_color, command=self.increment_counter)
        
        self.rowconfigure(0, weight=1, uniform='X')
        self.columnconfigure((0,2), weight=11, uniform='X')
        self.columnconfigure(1, weight=10, uniform='X')
        self.grid_propagate(False)

        self.decrement.grid(row=0, column=0, sticky='news', padx=(4,0), pady=4)
        self.counter.grid(row=0, column=1, sticky='news', padx=0, pady=4)
        self.increment.grid(row=0, column=2, sticky='news', padx=(0,4), pady=4)

        self.bind('<MouseWheel>', self.scroll)

        if self.state == 'disabled':
            self.disable()

    def decrement_counter(self)-> None:
        """Decrements the value of the counter by the step value."""
        self.counter_var.set(self.counter_var.get() - self.step_value)
        self.update_counter()

    def increment_counter(self)-> None:
        """Increments the value of the counter by the step value."""
        self.counter_var.set(self.counter_var.get() + self.step_value)
        self.update_counter()

    def scroll(self, scroll)-> None:
        """Increments/Decrements the value of the counter by the scroll value depending on scroll direction."""
        if self.state == 'normal':
            dirn = 1 if scroll.delta > 0 else -1
            if dirn == -1: self.counter_var.set(self.counter_var.get() - self.scroll_value)
            else: self.counter_var.set(self.counter_var.get() + self.scroll_value)
            self.update_counter()

    def get(self)-> None:
        """Returns the value of the counter."""
        return self.counter_var.get()
    
    def set(self, value:int)-> None:
        """Sets the counter to a particular value."""
        self.counter_var.set(max(min(value, self.max_value), self.min_value))
    
    def disable(self)-> None:
        """Disables the functionality of the counter."""
        self.state = 'disabled'
        self.increment.configure(state='disabled')
        self.decrement.configure(state='disabled')

    def enable(self)-> None:
        """Enables the functionality of the counter."""
        self.state = 'normal'
        self.increment.configure(state='normal')
        self.decrement.configure(state='normal')

    def bind(self, key, function, add=True)-> None:
        """Binds a key to a function."""
        super().bind(key, function, add)
        self.counter.bind(key, function, add)
        self.increment.bind(key, function, add)
        self.decrement.bind(key, function, add)

    def update_counter(self)-> None:
        """Updates the counter variable and calls the counter command."""
        self.limit_counter()
        if self.variable: self.variable.set(self.counter_var.get())
        if self.command: self.command(self.counter_var.get())

    def limit_counter(self)-> None:
        """Limits the value of the counter within the minimum and maximum values."""
        counter_value = self.counter_var.get()
        new_counter_value = max(min(counter_value, self.max_value), self.min_value)
        self.counter_var.set(new_counter_value)

    def configure(self, **kwargs)-> None:
        """Update widget values."""
        
        for value in ['font', 'text_color', 'button_color', 'button_hover_color', 'button_corner_radius', 'button_border_color', 'button_border_width']:
            if value in kwargs:
                new_value = kwargs.pop(value)
                if value not in ['font', 'button_corner_radius']:
                    if value not in ['button_hover_color', 'button_color', 'button_corner_radius']:
                        exec(f"self.counter.configure({value} = '{new_value}')")
                    value = {'button_color' : 'fg_color'}[value] if value in ['button_color', 'button_corner_radius'] else value
                    exec(f"self.increment.configure({value} = '{new_value}')")
                    exec(f"self.decrement.configure({value} = '{new_value}')")
                else:
                    value = {'button_corner_radius' : 'corner_radius'}[value] if value in ['button_color', 'button_corner_radius'] else value
                    exec(f"self.increment.configure({value} = {new_value})")
                    exec(f"self.decrement.configure({value} = {new_value})")
                    if value == 'font':
                        exec(f"self.counter.configure({value} = {new_value})")

        for value in ['min_value', 'max_value', 'step_value', 'scroll_value', 'variable']:
            if value in kwargs:
                new_value = kwargs.pop(value)
                exec(f'self.{value} = {new_value}')

        if 'command' in kwargs:
            self.command = kwargs.pop('command')
        elif 'state' in kwargs:
            self.state = kwargs.pop('state')
            if self.state == 'normal':
                self.enable()
            elif self.state == 'disabled':
                self.disable()

        super().configure(**kwargs)

class CTkToolTip(Toplevel):

    def __init__(self, widget, message:str=None, delay:float=0.2, follow:bool=True, x_offset:int=+20, y_offset:int=+10, bg_color:str=None, corner_radius:int=10, border_width:int=0, border_color:str=None, alpha:float=0.95, padding:tuple=(10, 2), **message_kwargs)-> None:
        super().__init__()

        self.widget = widget

        self.withdraw()

        self.overrideredirect(True)

        if sys.platform.startswith("win"):
            self.transparent_color = self.widget._apply_appearance_mode(ctk.ThemeManager.theme["CTkToplevel"]["fg_color"])
            self.attributes("-transparentcolor", self.transparent_color)
            self.transient()
        elif sys.platform.startswith("darwin"):
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
            self.transient(self.master)
        else:
            self.transparent_color = '#000001'
            corner_radius = 0
            self.transient()

        self.resizable(width=True, height=True)

        self.config(background=self.transparent_color)

        self.messageVar = ctk.StringVar()
        self.message = message
        self.messageVar.set(self.message)

        self.delay = delay
        self.follow = follow
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.corner_radius = corner_radius
        self.alpha = alpha
        self.border_width = border_width
        self.padding = padding
        self.bg_color = ctk.ThemeManager.theme["CTkFrame"]["fg_color"] if bg_color is None else bg_color
        self.border_color = border_color
        self.disable = False

        self.status = "outside"
        self.last_moved = 0
        self.attributes('-alpha', self.alpha)

        if sys.platform.startswith("win"):
            if self.widget._apply_appearance_mode(self.bg_color) == self.transparent_color:
                self.transparent_color = "#000001"
                self.config(background=self.transparent_color)
                self.attributes("-transparentcolor", self.transparent_color)

        self.transparent_frame = Frame(self, bg=self.transparent_color)
        self.transparent_frame.pack(padx=0, pady=0, fill="both", expand=True)

        self.frame = ctk.CTkFrame(self.transparent_frame, bg_color=self.transparent_color, corner_radius=self.corner_radius, border_width=self.border_width, fg_color=self.bg_color, border_color=self.border_color)
        self.frame.pack(padx=0, pady=0, fill="both", expand=True)

        self.message_label = ctk.CTkLabel(self.frame, textvariable=self.messageVar, **message_kwargs)
        self.message_label.pack(fill="both", padx=self.padding[0] + self.border_width, pady=self.padding[1] + self.border_width, expand=True)

        if self.widget.winfo_name() != "tk":
            if self.frame.cget("fg_color") == self.widget.cget("bg_color"):
                if not bg_color:
                    self._top_fg_color = self.frame._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["top_fg_color"])
                    if self._top_fg_color != self.transparent_color:
                        self.frame.configure(fg_color=self._top_fg_color)

        self.widget.bind("<Enter>", self.on_enter, add="+")
        self.widget.bind("<Leave>", self.on_leave, add="+")
        self.widget.bind("<Motion>", self.on_enter, add="+")
        self.widget.bind("<B1-Motion>", self.on_enter, add="+")
        self.widget.bind("<Destroy>", lambda _: self.hide(), add="+")

    def show(self)-> None:
        """Enable the widget."""
        self.disable = False

    def on_enter(self, event)-> None:
        """Processes motion within the widget including entering and moving."""
        if self.disable:
            return
        self.last_moved = time.time()

        if self.status == "outside":
            self.status = "inside"

        if not self.follow:
            self.status = "inside"
            self.withdraw()

        root_width = self.winfo_screenwidth()
        widget_x = event.x_root
        space_on_right = root_width - widget_x

        text_width = self.message_label.winfo_reqwidth()

        offset_x = self.x_offset
        if space_on_right < text_width + 20:
            offset_x = -text_width - 20

        self.geometry(f"+{event.x_root + offset_x}+{event.y_root + self.y_offset}")

        self.after(int(self.delay * 1000), self._show)

    def on_leave(self, event=None)-> None:
        """Hides the ToolTip temporarily."""
        if self.disable: return
        self.status = "outside"
        self.withdraw()

    def _show(self)-> None:
        """Displays the ToolTip."""
        if not self.widget.winfo_exists():
            self.hide()
            self.destroy()

        if self.status == "inside" and time.time() - self.last_moved >= self.delay:
            self.status = "visible"
            self.deiconify()

    def hide(self)-> None:
        """Disable the widget from appearing."""
        if not self.winfo_exists():
            return
        self.withdraw()
        self.disable = True

    def is_disabled(self)-> None:
        """Return the window state"""
        return self.disable

    def get(self)-> None:
        """Returns the text on the tooltip."""
        return self.messageVar.get()

    def configure(self, message:str=None, delay:float=None, bg_color:str=None, **kwargs)-> None:
        """Set new message or configure the label parameters."""
        if delay: self.delay = delay
        if bg_color: self.frame.configure(fg_color=bg_color)

        self.messageVar.set(message)
        self.message_label.configure(**kwargs)

#? ---------------------------------------- EXAMPLE ---------------------------------------- ?#

class Example(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Custom Widgets Example")
        self.geometry("400x250")

        #?  title 
        title = ctk.CTkLabel(
            self,
            text="Spinbox + Tooltip demo",
            font=("SF Pro Display", 22, "bold")
        )
        title.pack(pady=(20, 10))

        #?  variable linked to spinbox 
        self.value_var = ctk.IntVar(value=10)

        #?  spinbox 
        self.spinbox = CTkSpinbox(
            self,
            start_value=10,
            min_value=0,
            max_value=100,
            step_value=1,
            scroll_value=5,
            variable=self.value_var,
            font=("SF Pro Display", 18),
            width=180,
            height=50,
            corner_radius=10,
            command=self.on_spinbox_change
        )
        self.spinbox.pack(pady=10)

        #?  tooltip 
        CTkToolTip(
            self.spinbox,
            message="Use + / - or mouse wheel\nRange: 0 → 100",
            delay=0.3,
            corner_radius=8,
            padding=(12, 6)
        )

        #?  value label 
        self.value_label = ctk.CTkLabel(
            self,
            text=f"Current value: {self.value_var.get()}",
            font=("SF Pro Display", 16)
        )
        self.value_label.pack(pady=(10, 20))

        #?  buttons 
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack()

        ctk.CTkButton(
            btn_frame,
            text="Disable",
            command=self.spinbox.disable,
            width=100
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            btn_frame,
            text="Enable",
            command=self.spinbox.enable,
            width=100
        ).pack(side="left", padx=5)

    def on_spinbox_change(self, value: int):
        """Called every time the spinbox value changes."""
        self.value_label.configure(text=f"Current value: {value}")

if __name__ == "__main__":
    Example().mainloop()
