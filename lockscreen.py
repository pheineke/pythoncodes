import ctypes

def lock_screen():
    ctypes.windll.user32.LockWorkStation()

# Beispielaufruf
lock_screen()