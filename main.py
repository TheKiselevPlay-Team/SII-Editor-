"""Точка входа: запуск графического приложения «Перенос транспорта ETS2/ATS»."""
from __future__ import annotations

import logging
import sys


def main() -> int:
    """Создать QApplication, главное окно и запустить цикл событий."""
    from PyQt6.QtCore import Qt
    from PyQt6.QtGui import QGuiApplication
    from PyQt6.QtWidgets import QApplication, QMessageBox

    from sii_transfer import APP_NAME
    from sii_transfer.logging_setup import setup_logging
    from ui.main_window import MainWindow

    # High-DPI: дробное масштабирование без округления (125%, 150% ...)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName("SiiVehicleTransfer")
    app.setStyle("Fusion")

    log_path = setup_logging()
    log = logging.getLogger("main")

    def excepthook(exc_type, exc, tb):  # непойманные исключения — в журнал и окно
        log.error("Непредвиденная ошибка", exc_info=(exc_type, exc, tb))
        QMessageBox.critical(None, "Непредвиденная ошибка", f"{exc_type.__name__}: {exc}")

    sys.excepthook = excepthook
    win = MainWindow()
    win.show()
    if log_path:
        log.info("Файл журнала: %s", log_path)
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
