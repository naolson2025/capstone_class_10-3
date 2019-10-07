import unittest
from unittest import TestCase
from unittest.mock import patch, call
import bitcoinAPI

class TestTimeSheets(TestCase):

    @patch('bitcoinAPI.api')
    def test_convert(self, mock_rates):
        mock_rate = 15.34
        example_api_response = {"description":"United States Dollar","rate_float":mock_rate}
        mock_rates.side_effect = [example_api_response]
        converted = bitcoinAPI.convert(100, mock_rate)
        self.assertEqual(1534, converted)


if __name__ == '__main__':
    unittest.main()