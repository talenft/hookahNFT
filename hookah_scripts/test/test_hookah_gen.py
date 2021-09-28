import pathlib
from hookah_generator import HookahGenerator

if __name__ == '__main__':
    generator = HookahGenerator()
    generator.generate_hookah(pathlib.PurePath("hookah2.jpeg"), pathlib.PurePath("dest_hookah.jpeg"))
