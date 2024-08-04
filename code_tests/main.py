from media_player import MediaPlayer


if __name__ == "__main__":
    # Initialize components
    media_player = MediaPlayer()
    navigation = Navigation()
    settings = Settings()

    # Sample usage
    print(media_player.play("Track 1"))
    print(media_player.pause())
    print(media_player.stop())


