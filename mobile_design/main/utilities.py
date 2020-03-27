from datetime import datetime
from os.path import splitext


def get_timestamp_path(instance, filename):
    """Генерация имен сохраняемых в модели выгруженных файлов"""
    return f'{datetime.now().timestamp()}{splitext(filename)[1]}'