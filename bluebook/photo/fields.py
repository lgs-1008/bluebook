import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile

class ThumbnailImageFieldFile(ImageFieldFile): #3
    def _add_thumb(s): #4
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']: #5
            parts[-1] = 'jpg'
        return ".".join(parts)

    @property #6
    def thumb_path(self):
        return self._add_thumb(self.path)

    @property #7
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self, name, content, save=True): #8
        super().save(name, content, save) #9

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height) #10
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255)) #11
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2)) #12
        background.paste(img, box)
        background.save(self.thumb_path, 'JPEG') #13

    def delete(self, save=True): #14
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)

class ThumbnailImageField(ImageField): #15
    attr_class = ThumbnailImageFieldFile #16

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs): #17
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs) #18
