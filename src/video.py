"""A video class."""

from typing import Sequence

class FlagError(Exception):
    pass

class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id
        self._tags = tuple(video_tags)
        self._flag_reason = None

    @property
    def title(self) -> str:
        #Returns the video title.
        return self._title

    @property
    def video_id(self) -> str:
        #Returns the video id.
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        #Returns the video tag.
        return self._tags

    @property
    def tags_string(self) -> str:
        return ' '.join(self.tags)

    def __str__(self):
        #This function prints the video
        result = f'{self.title} ({self.video_id}) [{self.tags_string}]'
        if self.is_flagged:
            result += f' - FLAGGED {self.formatted_flag_reason}'
        return result

    def flag(self, flag_reason: str):
        if self.is_flagged:
            raise FlagError("Video is already flagged")
        self._flag_reason = flag_reason

    def unflag(self):
        if not self.is_flagged:
            raise FlagError("Video is not flagged")
        self._flag_reason = None

    @property
    def is_flagged(self):
        return self._flag_reason is not None

    def check_allowed(self):
        #True is returened if the video is not currently flagged
        if self.is_flagged:
            raise FlagError(f"Video is currently flagged {self.formatted_flag_reason}")

    @property
    def formatted_flag_reason(self):
        if self.is_flagged:
            return f'(reason: {self._flag_reason})'
        else:
            return ''