from os import name

import requests
import unittest


class TestYandexDiskAPI(unittest.TestCase):

    def setUp(self):
        self.api_url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.folder_name = "TestFolder"
        self.headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }


def test_create_folder_success(self):
    url = f"{self.api_url}?path=disk:/test/{self.folder_name}"
    response = requests.put(url, headers=self.headers)
    self.assertEqual(response.status_code, 201)  # Created
    self.assertTrue(self.folder_name in response.json().get('hrefs'))


def test_create_folder_already_exists(self):
    url = f"{self.api_url}?path=disk:/test/{self.folder_name}"
    response = requests.put(url, headers=self.headers)
    self.assertEqual(response.status_code, 409)  # Conflict


def test_create_folder_invalid_path(self):
    url = f"{self.api_url}?path=disk:/invalidpath/{self.folder_name}"
    response = requests.put(url, headers=self.headers)
    self.assertEqual(response.status_code, 400)  # Bad Request


if name == 'main':
    unittest.main()
