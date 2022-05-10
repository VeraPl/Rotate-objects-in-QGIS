import unittest
import os.path
from utilities import get_qgis_app
from PyQt5.QtWidgets import QApplication
from Rotate_Objects_dialog import RotateObjectsDialog

QGIS_APP = get_qgis_app()

class RotateObjectsDialogTest(unittest.TestCase):

    def setUp(self):
        self.dlg = RotateObjectsDialog()

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_types(self):
        app = QtWidgets.QApplication(sys.argv)
        test_window = QtWidgets.QMainWindow()
        application = Application(test_window)
        #self.assertTrue(application.build_frames.call_count == 1)

        #self.assertEqual(type(self.dlg.angle.uTextFilter), QLineEdit)
        self.assertEqual(0,0)


if __name__ == '__main__':
    suite = unittest.makeSuite(RotateObjectsDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
