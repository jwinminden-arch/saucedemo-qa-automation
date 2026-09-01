from pathlib import Path
from PIL import Image, ImageTk, ImageSequence


MEGAMAN_FILE = Path(__file__).parent / "megaman.gif"


class AnimatedGif:

    def __init__(
        self,
        root,
        label,
        gif_file=MEGAMAN_FILE,
        size=(100, 100),
        delay=100
    ):

        self.root = root
        self.label = label
        self.delay = delay

        self.frames = []
        self.frame_index = 0

        gif = Image.open(gif_file)

        for frame in ImageSequence.Iterator(gif):

            frame = frame.copy()

            frame.thumbnail(
                size
            )

            self.frames.append(
                ImageTk.PhotoImage(frame)
            )


    def start(self):

        self.animate()


    def animate(self):

        if not self.frames:
            return

        self.label.config(
            image=self.frames[self.frame_index]
        )

        self.frame_index = (
            self.frame_index + 1
        ) % len(self.frames)

        self.root.after(
            self.delay,
            self.animate
        )