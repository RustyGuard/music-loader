from typing import Callable


def input_int(prompt: str, is_correct: Callable[[int], bool] | None = None, default_value: int | None = None) -> int:
    while True:
        try:
            input_string = input(prompt)
            if input_string == "" and default_value is not None:
                return default_value

            input_result = int(input_string)

            if is_correct is not None and not is_correct(input_result):
                print("Некорректный ввод")
                continue

            return input_result
        except ValueError:
            print("Вы ввели не число.")
