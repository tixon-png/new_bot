from vkbottle import Keyboard, Text, KeyboardButtonColor

def get_main_keyboard():
    keyboard = Keyboard(one_time=False, inline=False)
    
    # Первый ряд
    keyboard.add(Text("Привет"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Помощь"), color=KeyboardButtonColor.SECONDARY)
    
    # Второй ряд
    keyboard.row()
    keyboard.add(Text("Мой ID"), color=KeyboardButtonColor.POSITIVE)
    keyboard.add(Text("info"), color=KeyboardButtonColor.NEGATIVE)
    
    return keyboard.get_json()