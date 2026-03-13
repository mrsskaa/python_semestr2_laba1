from src.sources import FileTaskSource, GeneratorTaskSource, APITaskSource
from src.processor import TaskProcessor
from src.logger_config import LOGGING_CONFIG
import logging.config
import logging


def main() -> None:
    """
    Демонстрирует работу процессора с разными источниками
    :return: None
    """
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)

    processor = TaskProcessor()

    logger.info("Создание файлового источника")
    file_source = FileTaskSource("tasks.txt")

    logger.info("Создание генератора задач")
    gen_source = GeneratorTaskSource(5)

    logger.info("Создание API-заглушки")
    api_source = APITaskSource()

    logger.info("Обработка файлового источника")
    processor.process(file_source)

    logger.info("Обработка генератора")
    processor.process(gen_source)

    logger.info("Обработка API-заглушки")
    processor.process(api_source)


if __name__ == "__main__":
    main()
