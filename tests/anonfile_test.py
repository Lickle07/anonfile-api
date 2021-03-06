import unittest
from anonfile import anonfile
import json


class AnonfileTest(unittest.TestCase):
    # Instantiate the test object
    def setUp(self):
        self.my_api_key = ''

        self.test_obj = anonfile.AnonFile(self.my_api_key)

    def test_returns_success_on_upload_file(self):
        status, self.file_obj = self.test_obj.upload_file('/home/ghost/my_test01')

        print("[*] File object -- " + json.dumps(self.file_obj))

        assert (status is True)
        assert (self.file_obj is not None)

        self.test_obj.download_file(self.file_obj)

    def test_returns_file_on_successful_download(self):
        location = '/home/ghost/PycharmProjects/anonfile-api/my_test01'
        file_exists = __import__('os').path.isfile(location)

        assert (file_exists)
