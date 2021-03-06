import unittest
from pylistfm.config import Config
from pylistfm.playlist import Playlist
from pylistfm.sources.example import API


class PlaylistTests(unittest.TestCase):

    def test_init_sources(self):
        config = Config().load()
        config.pylistfm.sources = ['example']
        playlist = Playlist(config.pylistfm, )
        self.assertEqual(playlist._sources, {'example': API})
