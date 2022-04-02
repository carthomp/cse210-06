from game.scripting.action import Action


class EndDrawingAction(Action):
    """Clears the buffer after drawing."""
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._video_service.flush_buffer()
