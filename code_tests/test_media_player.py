import pytest
from media_player import MediaPlayer

@pytest.fixture
def media_player():
    return MediaPlayer()

def test_play(media_player):
    response = media_player.play("Track 1")
    assert response == "Playing Track 1"
    assert media_player.playing is True

def test_pause(media_player):
    media_player.play("Track 1")
    response = media_player.pause()
    assert response == "Playback paused"
    assert media_player.playing is False

def test_stop(media_player):
    media_player.play("Track 1")
    response = media_player.stop()
    assert response == "Stopped playing Track 1"
    assert media_player.playing is False
    assert media_player.current_track is None
