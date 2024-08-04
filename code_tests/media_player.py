### **2. Source Files (`src/`)**
#### **media_player.py**
class MediaPlayer:
    def __init__(self):
        self.playing = False
        self.current_track = None

    def play(self, track):
        self.current_track = track
        self.playing = True
        return f"Playing {track}"

    def pause(self):
        if self.playing:
            self.playing = False
            return "Playback paused"
        return "No track is currently playing"

    def stop(self):
        if self.playing:
            self.playing = False
            track = self.current_track
            self.current_track = None
            return f"Stopped playing {track}"
        return "No track is currently playing"
