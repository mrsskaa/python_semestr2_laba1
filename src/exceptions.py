class TaskError(Exception):
    """Базовое исключение для всех ошибок в домене задач"""
    pass

class TaskValidationError(TaskError):
    """Исключение, выбрасываемое при попытке установить некорректное значение атрибута"""
    pass
