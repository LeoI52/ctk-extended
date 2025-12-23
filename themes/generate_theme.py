"""
@author : Léo IMBERT
@created : 21/04/2025
@updated : 21/04/2025
"""

import os

os.system("cls")

def ask_color(name:str)-> tuple:
    light = input(f"Enter light {name} color (hex, e.g. #FFFFFF): ").strip()
    dark = input(f"Enter dark {name} color (hex, e.g. #000000): ").strip()
    return light, dark

colors = {
    "background": ask_color("background"),
    "shade": ask_color("shade"),#f5f3f7
    "border": ask_color("border"),
    "border_hover": ask_color("border hover"),
    "action": ask_color("action"),
    "action_hover": ask_color("action hover"),
    "text": ask_color("text"),
    "text_disabled": ask_color("text disabled")
}
corner_radius = input("Enter the corner radius: ")

template_replacements = {
    "background_light": colors["background"][0],
    "background_dark": colors["background"][1],
    "shade_light": colors["shade"][0],
    "shade_dark": colors["shade"][1],
    "border_light": colors["border"][0],
    "border_dark": colors["border"][1],
    "border_hover_light": colors["border_hover"][0],
    "border_hover_dark": colors["border_hover"][1],
    "action_light": colors["action"][0],
    "action_dark": colors["action"][1],
    "action_hover_light": colors["action_hover"][0],
    "action_hover_dark": colors["action_hover"][1],
    "text_light": colors["text"][0],
    "text_dark": colors["text"][1],
    "text_disabled_light": colors["text_disabled"][0],
    "text_disabled_dark": colors["text_disabled"][1],
    '"corner_radius_value"': corner_radius
}

with open("themes/template.json", "r") as file:
    template_str = file.read()

for key, value in template_replacements.items():
    template_str = template_str.replace(key, value)

output_theme = input("Enter the theme name: ")
with open(f"themes/{output_theme}.json", "w") as f:
    f.write(template_str)

print(f"✅ Theme file '{output_theme}.json' created successfully!")