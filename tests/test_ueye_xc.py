import unittest

import ids

# FIXME: Hardcoded
HANDLE = 50
COLOR = ids.ids_core.COLOR_BGR8


class TestIds(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.cam = ids.Camera(handle = HANDLE, color = COLOR)

    def test_camera_initialisation(self):
        self.assertIsInstance(self.cam, ids.Camera)

    def test_trigger_mode(self):
        mode = self.cam.trigger_mode
        self.assertGreaterEqual(mode, ids.ids_core.TRIGGER_OFF)
        self.assertLessEqual(mode, 0x0050)

    def test_set_image_format(self):
        self.cam.trigger_mode = ids.ids_core.TRIGGER_SOFTWARE
        self.cam.image_format = 33
