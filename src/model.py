import datetime
import logging
from src.descriptors import PriorityDescriptor, StatusDescriptor, DescriptionDescriptor, ReadyDescriptor
from src.exceptions import TaskValidationError

logger = logging.getLogger(__name__)


class Task:
    """
    Класс задачи платформы обработки задач.

    Атрибуты:
        id: идентификатор задачи (только для чтения, > 0)
        description: описание задачи (валидация: длина от 5 до 200 символов)
        priority: приоритет задачи (валидация: int от 1 до 5)
        status: статус задачи (валидация: pending, in_progress, completed)
        created_at: время создания задачи (только для чтения)
        is_ready: вычисляемое свойство готовности к выполнению

    Атрибуты description, priority, status управляются data-дескрипторами.
    Атрибут is_ready управляется non-data дескриптором.
    Атрибуты id и created_at защищены property.
    """
    _id: int
    _created_at: datetime.datetime

    priority = PriorityDescriptor()
    status = StatusDescriptor()
    description = DescriptionDescriptor()
    is_ready = ReadyDescriptor()

    def __init__(self, id: int, description: str, priority: int, status: str) -> None:
        """
        Инициализирует задачу с указанными параметрами.

        :param id: идентификатор задачи (должен быть > 0)
        :param description: описание задачи (длина от 5 до 200 символов)
        :param priority: приоритет задачи (от 1 до 5)
        :param status: статус задачи (pending, in_progress, completed)
        :raises TaskValidationError: если любой из параметров не проходит валидацию
        """
        logger.info(f"Создание задачи с id={id}")

        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self._created_at = datetime.datetime.now()

        logger.debug(
            f"Задача создана: id={id}, description={description[:50]}..., priority={priority}, status={status}")

    @property
    def id(self) -> int:
        """
        Идентификатор задачи. Только для чтения.

        :return: идентификатор задачи
        """
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        """
        Устанавливает идентификатор задачи. Может быть вызван только один раз.

        :param value: идентификатор задачи (> 0)
        :raises AttributeError: при попытке изменить id после создания
        :raises TaskValidationError: если id <= 0
        """
        if hasattr(self, '_id'):
            logger.error(f"Попытка изменить id с {self._id} на {value}")
            raise AttributeError("id нельзя изменить после создания")
        if value <= 0:
            logger.error(f"Попытка установить id = {value} (<= 0)")
            raise TaskValidationError("id должен быть больше 0")

        self._id = value
        logger.debug(f"id установлен в {value}")

    @property
    def created_at(self) -> datetime.datetime:
        """
        Время создания задачи. Только для чтения.

        :return: время создания задачи
        """
        return self._created_at
