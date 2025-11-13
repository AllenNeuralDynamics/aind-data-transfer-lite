"""Unit tests for DataTransferLiteUI module."""

import unittest
from unittest.mock import patch

from magicgui.widgets import Label
from PyQt5.QtWidgets import QApplication

from aind_data_transfer_lite.ui import DataTransferLiteUI, main


class TestDataTransferLiteUI(unittest.TestCase):
    """Tests for DataTransferLiteUI class and its main launcher."""

    @classmethod  # pragma: no cover
    def setUpClass(cls) -> None:
        """Ensure a QApplication exists once for all tests."""
        app_instance = QApplication.instance()
        if app_instance is None:
            cls.app = QApplication([])
        else:
            cls.app = app_instance

    def test_ui_initialization(self):
        """Test that UI should initialize with a hello_label
        showing the greeting."""
        ui = DataTransferLiteUI()
        self.assertTrue(hasattr(ui, "hello_label"), "Missing hello_label")
        self.assertIsInstance(ui.hello_label, Label, "hello_label not a Label")
        self.assertEqual(
            ui.hello_label.value,
            "Hello, AIND Data Transfer Lite UI",
            "Label value should match greeting",
        )

    @patch("aind_data_transfer_lite.ui.DataTransferLiteUI.show")
    def test_main_runs_without_error(self, mock_show):
        """Test main() should run and call show()
        without opening a real window."""
        main()  # If it raises, unittest automatically fails
        mock_show.assert_called_with(run=True)


if __name__ == "__main__":
    unittest.main()
