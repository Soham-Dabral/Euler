import os
import sys

BASE_PATH = getattr(sys, "_MEIPASS", os.path.abspath("."))

def resource_path(path):
    return os.path.join(BASE_PATH, path)