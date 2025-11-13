"""Simple MagicGUI-based UI launcher for AIND Data Transfer Lite."""

import sys

from magicclass import magicclass
from magicgui.widgets import Label
from PyQt5.QtWidgets import QApplication


@magicclass(name="Data Transfer Lite UI", layout="vertical")
class DataTransferLiteUI:
    """A minimal UI showing a greeting for AIND Data Transfer Lite."""

    def __init__(self):
        """Initialize the UI with a visible greeting label."""
        self.hello_label = Label(value="Hello, AIND Data Transfer Lite UI")
        self.append(self.hello_label)


def main():
    """Launch the Data Transfer Lite UI."""
    # Ensure QApplication exists (safe for repeated runs)
    QApplication.instance() or QApplication(sys.argv)

    ui = DataTransferLiteUI()
    # Show window; run=True starts the event loop
    ui.show(run=True)


if __name__ == "__main__":
    main()
