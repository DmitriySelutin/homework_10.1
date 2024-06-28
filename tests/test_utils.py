import json
import unittest
from unittest.mock import MagicMock, mock_open, patch

from src.utils import get_transactions


class TestGetTransactions(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_financial_transactions_valid_file(self, mock_file: MagicMock) -> None:
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = get_transactions("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_get_transactions_invalid_content(self, mock_file: MagicMock) -> None:
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_transactions_empty_file(self, mock_file: MagicMock) -> None:
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_transactions_file_not_found(self, mock_file: MagicMock) -> None:
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='{"transaction": "data"}')
    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_get_transactions_json_decode_error(self, mock_json_load: MagicMock, mock_file: MagicMock) -> None:
        result = get_transactions("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]',
    )
    def test_get_transactions_json(self, mock_file: MagicMock) -> None:
        result = get_transactions("test.json")
        self.assertEqual(result, [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}])
