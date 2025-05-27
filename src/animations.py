class Animation:
    def __init__(self, name: str, frames: list, frame_duration: int):
        self.name = name
        self.frames = frames
        self.frame_duration = frame_duration

        self.frame_count = len(self.frames)


    def get_current_frame(self):
        """Return the current frame of the animation."""
        return self.frames[self.current_frame]