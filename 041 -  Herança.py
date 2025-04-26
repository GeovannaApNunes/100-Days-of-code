# Classe base
class CSSCommand:
    def __init__(self, selector):
        self.selector = selector

    def apply_style(self):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses.")

# Subclasse BackgroundColor
class BackgroundColor(CSSCommand):
    def apply_style(self):
        return f"{self.selector} {{ background-color: red; }}"

# Subclasse FontSize
class FontSize(CSSCommand):
    def apply_style(self):
        return f"{self.selector} {{ font-size: 20px; }}"

# Subclasse Margin
class Margin(CSSCommand):
    def apply_style(self):
        return f"{self.selector} {{ margin: 10px; }}"

# Subclasse Padding
class Padding(CSSCommand):
    def apply_style(self):
        return f"{self.selector} {{ padding: 5px; }}"

# Criando instâncias das classes
css_commands = [
    BackgroundColor(".header"),
    FontSize(".content"),
    Margin(".footer"),
    Padding(".container")
]

# Exibindo os comandos CSS
for command in css_commands:
    print(command.apply_style())