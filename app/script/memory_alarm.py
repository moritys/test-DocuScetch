import psutil

import requests

import time

from constants import (
    INTERVAL_FOR_CHECKING_MEMORY_IN_SECONDS,
    MEMORY_ALARM_CRITICAL_PERCENT
)


def get_memory_usage_percent() -> int:
    """Функция для опредения потребления памяти в процентах."""

    memory_info = psutil.virtual_memory()
    return memory_info.percent


def main():
    """
    Функция для постоянного мониторинга потребления памяти.

    В случае превышения максимального порога,
    отправляет alarm в API приложения.

    Критическое значение и интервал проверки
    заполняется в файле constants.py.
    """

    try:
        print('Запущен скрипт мониторинга памяти')
        while True:
            current_memory_usage = get_memory_usage_percent()
            if current_memory_usage > MEMORY_ALARM_CRITICAL_PERCENT:
                print('alarm!')
                # response = requests.get('http://your-api-url')
            time.sleep(INTERVAL_FOR_CHECKING_MEMORY_IN_SECONDS)
    except KeyboardInterrupt:
        print('Работа скрипта прервана вручную')
    except Exception as e:
        print(f'Возникла ошибка при выполнении спринта: {e}')


if __name__ == '__main__':
    main()
