# kivy_timer
Basic timer using Kivy for GUI

Тестове завдання:

Потрібно створити в фреймворке KIVY UI-компонент з такими елементами:
*Інпут (діапазон значень: 0 ≤ int ≤ 300),
*Кнопка "Start",
*Лейбл для відображення таймера.

📌 Функціонал:
Користувач вводить число в інпут.
Натискає кнопку "Start".
Запускається таймер зворотного відліку (countdown).
Лейбл динамічно оновлюється та показує значення таймера в режимі реального часу з точністю до десятої секунди (наприклад, 10.0 → 9.9 → 9.8 і т.д.).
⚙️ Вимоги:
✅ Використовувати VerticalBoxLayout.
✅ Без використання kv-розмітки – вся логіка в коді Python.


# Instruction
1) to setup environment run setup_env.bat - it will create virtual environment and install needed packages
2) to create executable (.exe) run make_build.bat
Note: it is expected that batch files will be run from setup_project folder


# Some moments to improve (not complete list)
1) move some constants like range for time interval to configuration file
2) move used strings to separate module, for example 'resources'
3) UI improvements: use better styles, make components more scalable
