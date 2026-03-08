from src.protocol import TaskSource


class TaskProcessor:
    """Обработчик задач из источника, соответствующего протоколу TaskSource"""
    def process(self, source: TaskSource) -> list[str]:
        """
        Проверяет источник, получает и выводит задачи
        :param source: источник
        :return: список задач, полученных от источника
        """
        if not isinstance(source, TaskSource):
            raise TypeError(f"The object {source} isn't the source of the tasks")

        tasks = source.get_tasks()
        print(f"Tasks cnt: {len(tasks)} tasks:  {tasks}")
        return tasks
