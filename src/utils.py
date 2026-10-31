class Logger:
    _RESET = "\003[0m"
    _BOLD = "\003[1m"

    _COLORS = {
        "amber":"\033[38;2;255;191;0m",
        "blue":"\033[38;2;0;0;255m",
        "chartreuse":"\033[38;2;127;255;0m",
        "gray":"\033[38;2;85;85;85m",
        "green":"\033[38;2;0;128;0m",
        "magenta":"\033[38;2;255;0;255m",
        "orange":"\033[38;2;255;140;0m",
        "purple":"\033[38;2;128;0;128m",
        "red":"\033[38;2;255;0;0m",
        "teal":"\033[38;2;0;128;128m",
        "vermilion":"\033[38;2;255;69;0m",
        "violet":"\033[38;2;75;0;130m",
        "white":"\033[38;2;255;255;255m",
        "yellow":"\033[38;2;255;230;0m"
    }

    @classmethod
    def color_text(cls, text: str, color: str, bold: bool = False) -> str:
        color_code = cls._COLORS.get(color.lower(), "")
        style_code = cls._BOLD if bold else ""

        if not color_code and not style_code:
            return text

        return f"{style_code}{color_code}{text}{cls._RESET}"

    @classmethod
    def success(cls,message: str):
        print(cls.color_text(f"[SUCCESS] {message}","chartreuse",bold=True))

    @classmethod
    def info(cls,message: str):
        print(cls.color_text(f"[INFO] {message}","teal"))

    @classmethod
    def warning(cls,message: str):
        print(cls.color_text(f"[WARNING] {message}","amber",bold=True))

    @classmethod
    def error(cls,message: str):
        print(cls.color_text(f"[ERROR] {message}","vermilion",bold=True))

import time
from functools import wraps

class Util:

    @staticmethod
    def timer(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            result = func(*args,**kwargs)
            end_time = time.perf_counter()

            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' executed in {execution_time:.2f} seconds")

            return result

        return wrapper