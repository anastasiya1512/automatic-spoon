import pytest
from string_utils import StringUtils

@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # обычный случай
    ("skyPro", "Skypro"),          # с заглавной буквой в середине
    ("", ""),                        # пустая строка
    ("a", "A"),                     # строка из одной буквы
    ("ABC", "Abc"),                 # строка из заглавных букв
])
def test_capitalize(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),        # пробелы в начале
    ("skypro  ", "skypro  "),      # пробелы в конце не удаляются
    ("   ", ""),                    # только пробелы
    ("", ""),                        # пустая строка
])
def test_trim(input_str, expected):
    string_utils = StringUtils()
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),          # символ есть в начале
    ("SkyPro", "o", True),          # символ есть в конце
    ("SkyPro", "P", True),          # символ есть в середине
    ("SkyPro", "U", False),         # символ отсутствует
    ("", "a", False),               # пустая строка
])
def test_contains(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),       # удаление символа
    ("SkyPro", "Pro", "Sky"),       # удаление подстроки в конце
    ("SkyPro", "s", "SkyPro"),      # символ отсутствует
    ("", "a", ""),                   # пустая строка
])
def test_delete_symbol(input_str, symbol, expected):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == expected


def test_capitalize_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

def test_capitalize_with_dict():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize({})

def test_trim_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim(None)

def test_trim_with_list():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim([])

def test_trim_with_dict():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim({})

# Для contains с некорректными типами строки
def test_contains_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")

def test_contains_with_dict():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.contains({}, "a")

def test_delete_symbol_with_none():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")

def test_delete_symbol_with_dict():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.delete_symbol({}, "a")

def test_contains_empty_symbol():
    string_utils = StringUtils()
    assert string_utils.contains("Some text", "") is True  # Метод возвращает True для пустой строки


def test_capitalize_invalid_type():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.capitalize(123)

def test_trim_invalid_type():
    string_utils = StringUtils()
    with pytest.raises(AttributeError):
        string_utils.trim(123.456)


def test_contains_invalid_type():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.contains("Hello", 3)

def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    assert string_utils.delete_symbol("", "a") == ""

def test_delete_symbol_invalid_char_type():
    string_utils = StringUtils()
    with pytest.raises(TypeError):
        string_utils.delete_symbol("Hello", 3)
