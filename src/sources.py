import logging

logger = logging.getLogger(__name__)


class FileTaskSource:
    """Читает задачи из текстового файла."""

    def __init__(self, file_name: str):
        """
        Инициализирует источник с указанным файлом.

        :param file_name: путь к файлу с задачами
        """
        self.file_name = file_name
        logger.info(f"FileTaskSource создан с файлом: {file_name}")

    def get_tasks(self) -> list[str]:
        """
        Читает задачи из файла, игнорируя пустые строки.

        :return: список задач или пустой список при ошибке
        """
        logger.debug(f"Чтение задач из файла: {self.file_name}")
        try:
            tasks = []
            with open(self.file_name, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    if not line:
                        logger.debug(f"Строка {line_num} пустая, пропускаем")
                        continue
                    tasks.append(line)
                    logger.debug(f"Прочитана задача: {line}")

            logger.info(f"Из файла {self.file_name} прочитано {len(tasks)} задач")
            return tasks

        except FileNotFoundError:
            logger.error(f"Файл {self.file_name} не найден")
            print(f"File {self.file_name} not found")
            return []
        except Exception as e:
            logger.exception(f"Неожиданная ошибка при чтении файла: {e}")
            return []


class GeneratorTaskSource:
    """Генерирует задачи по номеру."""

    def __init__(self, cnt: int):
        """
        Инициализирует генератор с указанным количеством задач.

        :param cnt: количество задач (должно быть > 0)
        :raises ValueError: если cnt <= 0
        """
        if cnt <= 0:
            logger.error(f"Попытка создать генератор с некорректным значением: {cnt}")
            raise ValueError("cnt must be greater than 0")

        self._cnt = cnt
        logger.info(f"GeneratorTaskSource создан с количеством задач: {cnt}")

    @property
    def cnt(self):
        """Возвращает текущее количество задач."""
        return self._cnt

    @cnt.setter
    def cnt(self, value: int):
        """
        Устанавливает новое количество задач.

        :param value: новое количество задач (должно быть > 0)
        :raises ValueError: если value <= 0
        """
        logger.debug(f"Попытка изменить cnt с {self._cnt} на {value}")
        if value <= 0:
            logger.error(f"Попытка установить некорректное значение cnt: {value}")
            raise ValueError("cnt must be greater than 0")

        old_value = self._cnt
        self._cnt = value
        logger.info(f"cnt изменён с {old_value} на {value}")

    def get_tasks(self) -> list[str]:
        """
        Генерирует задачи в формате "Task i".

        :return: список сгенерированных задач
        """
        logger.debug(f"Генерация {self._cnt} задач")
        tasks = []
        for i in range(1, self._cnt + 1):
            task = f"Task {i}"
            tasks.append(task)
            logger.debug(f"Сгенерирована задача: {task}")

        logger.info(f"Сгенерировано {len(tasks)} задач")
        return tasks


class APITaskSource:
    """Заглушка API, возвращает фиксированный список задач."""

    def __init__(self):
        """Инициализирует API-заглушку."""
        logger.info("APITaskSource создан")

    def get_tasks(self) -> list[str]:
        """
        Возвращает заранее заданный список задач.

        :return: фиксированный список задач
        """
        tasks = [
            "Сделать лабу",
            "Написать ридми",
            "Отправить Cамиру",
            "Доделать дизайн",
            "Начать писать фронт по практике"
        ]
        logger.info(f"API-заглушка вернула {len(tasks)} задач")
        logger.debug(f"Задачи из API: {tasks}")
        return tasks
