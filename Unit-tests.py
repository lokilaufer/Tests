import unittest
from unittest.mock import patch

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_person(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return "Документ не найден"


def get_shelf(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден на полках"


class TestDocumentsFunctions(unittest.TestCase):

    def test_get_person_existing_document(self):
        with patch('builtins.input', return_value="2207 876234"):
            self.assertEqual(get_person("2207 876234"), "Василий Гупкин")

    def test_get_person_non_existing_document(self):
        with patch('builtins.input', return_value="12345"):
            self.assertEqual(get_person("12345"), "Документ не найден")

    def test_get_shelf_existing_document(self):
        with patch('builtins.input', return_value="2207 876234"):
            self.assertEqual(get_shelf("2207 876234"), "1")

    def test_get_shelf_non_existing_document(self):
        with patch('builtins.input', return_value="12345"):
            self.assertEqual(get_shelf("12345"), "Документ не найден на полках")


if __name__ == '__main__':
    unittest.main()
