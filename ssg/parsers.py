import shutil
from typing import List
from pathlib import Path


class Parser:

    @List[str]
    extensions = []

    def valid_extension(self, extension):
        return extension in self.extensions

    @Path
    def parse(self, path, source, dest):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))


class ResourceParser(Parser):
    extenstions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)