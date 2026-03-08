import pytest
from src.sources import FileTaskSource, GeneratorTaskSource, APITaskSource

@pytest.fixture
def file_source(temp_task_file):
    """Фикстура для FileTaskSource"""
    return FileTaskSource(temp_task_file)

@pytest.fixture
def generator_source():
    """Фикстура для GeneratorTaskSource"""
    return GeneratorTaskSource(5)

@pytest.fixture
def api_source():
    """Фикстура для APITaskSource"""
    return APITaskSource()

@pytest.fixture
def temp_task_file(tmp_path):
    """Создает временный файл с задачами"""
    file_path = tmp_path / "tasks.txt"
    content = "Задача 1\nЗадача 2\nЗадача 3"
    file_path.write_text(content, encoding='utf-8')
    return str(file_path)
