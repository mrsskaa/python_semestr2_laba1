class FileTaskSource:
    """Читает задачи из текстового файла."""

    def __init__(self, file_name: str):
        """
        Инициализирует источник с указанным файлом
        :param file_name: путь к файлу с задачами (каждая задача на новой строке)
        """
        self.file_name = file_name

    def get_tasks(self) -> list[str]:
        """
        Читает задачи из файла, игнорируя пустые строки
        :return: список задач (строк), прочитанных из файла. Если файл не найден, возвращает пустой список
        """
        try:
            tasks = []
            with open(self.file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    tasks.append(line)
            return tasks
        except FileNotFoundError:
            print(f"File {self.file_name} not found")
            return []


class GeneratorTaskSource:
    """Генерирует задачи по номеру."""

    def __init__(self, cnt: int):
        """
        Инициализирует генератор с указанным количеством задач
        :param cnt: количество задач для генерации (должно быть > 0)
        """
        if cnt <= 0:
            raise ValueError("cnt must be greater than 0")
        self._cnt = cnt

    @property
    def cnt(self):
        """
        Возвращает текущее количество задач
        :return: количество задач (целое число)
        """
        return self._cnt

    @cnt.setter
    def cnt(self, value: int):
        """
        Устанавливает новое количество задач
        :param value: новое количество задач (должно быть > 0)
        """
        if value <= 0:
            raise ValueError("cnt must be greater than 0")
        self._cnt = value

    def get_tasks(self) -> list[str]:
        """
        Генерирует задачи в формате "Task i"
        :return: список сгенерированных задач (строк)
        """
        tasks = []
        for i in range(1, self._cnt + 1):
            tasks.append(f"Task {i}")
        return tasks


class APITaskSource:
    """Заглушка API, возвращает фиксированный список задач."""

    def get_tasks(self) -> list[str]:
        """
        Возвращает заранее заданный список задач
        :return: фиксированный список задач (строк)
        """
        return ["Сделать лабу", "Написать ридми", "Отправить Cамиру", "Доделать дизайн",
                "Начать писать фронт по практике"]
