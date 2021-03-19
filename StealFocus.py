import ctypes

#   store some stuff for win api interaction
set_to_foreground = ctypes.windll.user32.SetForegroundWindow
keybd_event = ctypes.windll.user32.keybd_event

alt_key = 0x12
extended_key = 0x0001
key_up = 0x0002


def steal_focus():
    keybd_event(alt_key, 0, extended_key | 0, 0)
    set_to_foreground(window.winfo_id())
    keybd_event(alt_key, 0, extended_key | key_up, 0)

    entry.focus_set()