import subprocess
import shutil

"""
Text color              Background color
Black	\033[30m	    Black	\033[40m
Red	    \033[31m	    Red	    \033[41m
Green	\033[32m	    Green	\033[42m
Yellow	\033[33m	    Yellow	\033[43m
Blue	\033[34m	    Blue	\033[44m
Magenta	\033[35m	    Magenta	\033[45m
Cyan	\033[36m	    Cyan	\033[46m
White	\033[37m	    White	\033[47m
Reset (Default)	\033[0m	Reset (Default)	\033[0m


Style	                                ANSI Code
Bold	                                \033[1m
Dim (faint)	                            \033[2m
Italic (not widely supported)	        \033[3m
Underline	                            \033[4m
Blink (slow)	                        \033[5m
Blink (rapid)	                        \033[6m
Inverse (swap foreground/background)	\033[7m
Hidden (conceal text)	                \033[8m
Strikethrough	                        \033[9m
Reset (normal text)	                    \033[0m

\033[TEXT_COLOR;BACKGROUND_COLORm;STYLE
"""

equations = ["5 + 4 * X + X^2= X^2",
            "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
            "5 * X^0 + 4 * X^1 = 4 * X^0",
            "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
            "42 * X^0 = 42 * X^0",
            "1 = 1",
            "1 .2 * X^0 + 4 * X^1 = 4 * X^0",
            "1 * X^0b + 1 *  X^1z = 4 * X^q^0"]

terminal_width = int(shutil.get_terminal_size().columns/2)
print(terminal_width)

print("\n\n---- COMPUTOR V1 TESTS ----\n")
for equation in equations:

    basic_text = f" Testing: {equation} "
    text = f"\033[32m\033[42m\033[1m{basic_text.center(terminal_width, ".")}\033[0m"
    print(text)
    subprocess.run(["python", "computor.py", equation])
    print()
