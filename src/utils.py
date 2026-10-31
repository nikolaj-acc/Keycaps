import logging
from pathlib import Path

class Logger:
    _RESET = "\033[0m"
    _BOLD = "\033[1m"

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

    _log_path = Path(__file__).parent / "assets" / "docs" / "logging" / "keycap-logs.log"
    _logger_configured = False

    @classmethod
    def _ensure_logger_configured(cls):
        if not cls._logger_configured:
            cls._log_path.parent.mkdir(parents=True, exist_ok=True)
            logging.basicConfig(
                filename=cls._log_path,
                format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d [%(filename)s])',
                datefmt='%d-%m-%Y %I:%M:%S %p',
                encoding="utf-8",
                level=logging.INFO,
            )
            cls._logger_configured = True

    @classmethod
    def color_text(cls, text: str, color: str, bold: bool = False) -> str:
        color_code = cls._COLORS.get(color.lower(), "")
        style_code = cls._BOLD if bold else ""

        if not color_code and not style_code:
            return text

        return f"{style_code}{color_code}{text}{cls._RESET}"

    @classmethod
    def success(cls,message: str):
        cls._ensure_logger_configured()
        print(cls.color_text(f"[SUCCESS] {message}","chartreuse",bold=True))
        logging.info(f"[SUCCESS] {message}")

    @classmethod
    def info(cls,message: str):
        cls._ensure_logger_configured()
        print(cls.color_text(f"[INFO] {message}","teal"))
        logging.info(f"[INFO] {message}")

    @classmethod
    def warning(cls,message: str):
        cls._ensure_logger_configured()
        print(cls.color_text(f"[WARNING] {message}","amber",bold=True))
        logging.warning(f"[WARNING] {message}")

    @classmethod
    def error(cls,message: str):
        cls._ensure_logger_configured()
        print(cls.color_text(f"[ERROR] {message}","vermilion",bold=True))
        logging.error(f"[ERROR] {message}")

    @classmethod
    def test(cls):
        cls.info("Testing...")
        cls.warning("Testing...")
        cls.error("Testing...")
        print(cls.color_text("Testing...","blue"))
        print(cls.color_text("Testing...","violet"))
        print(cls.color_text("Testing...","gray"))
        cls.success("Testing...")

import time
import os
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
            print(f"Function '\033[38;2;255;0;255m{func.__name__}\033[0m' executed in {execution_time:.2f} seconds")

            logging.info(f"Function '{func.__name__}' executed in {execution_time:.2f} seconds")

            return result

        return wrapper

    @staticmethod
    def find_path(file_path):
        if not os.path.exists(file_path):
            Logger.error(f"File: '{file_path}' doesn't exist!")
            return False

        if os.path.isfile(file_path):
            Logger.success(f"File: '{file_path}' loaded")
        elif os.path.isdir(file_path):
            Logger.success(f"Directory: '{file_path}' loaded")
        return True