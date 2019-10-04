import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimeSheets(TestCase):
    """ Mock input() to for it to return '2' """

    @patch('builtins.input', side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)


    @patch('builtins.input', side_effect=['cat', '123pizza', '2.4'])
    def test_get_hours_for_day_validation(self, mock_input):
        hours = timesheets.get_hours_for_day('whatever')
        self.assertEqual(2.4, hours)


    @patch('builtins.print')
    def test_display_total(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')


    @patch('timesheets.alert')
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)
        mock_alert.assert_called_once()


    @patch('timesheets.alert')
    def test_alert_meet_min_hours_exceed(self, mock_alert):
        timesheets.alert_not_meet_min_hours(45, 30)
        mock_alert.assert_not_called()


    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):
        mock_hours = [5, 7, 9]
        mock_get_hours.side_effect = mock_hours
        days = ['m', 't', 'w']
        expected_hours = dict(zip(days, mock_hours))
        hours = timesheets.get_hours(days)
        self.assertDictEqual(expected_hours, hours)


    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        example = {'M':3, 'T': 12, 'W': 8.5}

        expected_table_calls = [
            call('Day            Hours Worked   '),
            call('M              3              '),
            call('T              12             '),
            call('W              8.5            ')
        ]

        timesheets.display_hours(example)
        mock_print.assert_has_calls(expected_table_calls)


if __name__ == '__main__':
    unittest.main()