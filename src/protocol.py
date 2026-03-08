from typing import Protocol, List, runtime_checkable


@runtime_checkable
class TaskSource(Protocol):
    """Протокол источника задач. Требует метод get_tasks"""

    def get_tasks(self) -> List[str]:
        """
        Возвращает список задач.
        :return: список задач (строк)
        """
        ...
