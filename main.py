import sys
from PyQt6.QtWidgets import QApplication
from audio_engine import AudioEngine
from project_manager import ProjectManager
from ui import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion") # Good cross-platform modern look
    
    # Initialize Core Components
    audio_engine = AudioEngine()
    project_manager = ProjectManager()
    
    # Initialize UI
    window = MainWindow(audio_engine, project_manager)
    
    # Apply dark mode style
    app.setStyleSheet("""
        QMainWindow, QWidget { background-color: #2b2b2b; color: #e0e0e0; }
        QLabel { color: #e0e0e0; }
        QPushButton { background-color: #444; color: #fff; border: 1px solid #555; padding: 5px; border-radius: 3px; }
        QPushButton:hover { background-color: #555; }
        QComboBox { background-color: #444; color: #fff; border: 1px solid #555; padding: 2px; }
        QSpinBox { background-color: #444; color: #fff; border: 1px solid #555; padding: 2px; }
        QSlider::groove:horizontal { border: 1px solid #999; height: 8px; background: #444; margin: 2px 0; }
        QSlider::handle:horizontal { background: #888; border: 1px solid #555; width: 18px; margin: -2px 0; border-radius: 3px; }
    """)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
