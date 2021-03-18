import ctypes
from ctypes.wintypes import DWORD, ULONG
from ctypes import windll, c_bool, c_int, POINTER, Structure
from PyQt5.QtCore import Qt



class AccentPolicy(Structure):
    _fields_ = [
        ('AccentState', DWORD),
        ('AccentFlags', DWORD),
        ('GradientColor', DWORD),
        ('AnimationId', DWORD),
    ]


# SOURCE: http://undoc.airesoft.co.uk/user32.dll/GetWindowCompositionAttribute.php
class WINCOMPATTRDATA(Structure):
    _fields_ = [
        ('Attribute', DWORD),
        ('Data', POINTER(AccentPolicy)),
        ('SizeOfData', ULONG),
    ]


def SetGlassBg(Window):
    SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
    SetWindowCompositionAttribute.restype = c_bool
    SetWindowCompositionAttribute.argtypes = [c_int, POINTER(WINCOMPATTRDATA)]




    #Window.setWindowFlags(Qt.FramelessWindowHint)




    Window.setAttribute(Qt.WA_TranslucentBackground)
    #Window.setAttribute(Qt.WA_NoSystemBackground) #No nice
    #Window.setStyleSheet("background-color: transparent")

        # SOURCE: http://howtucode.com/c-pinvoke-user32dll-getwindowcompositionattribute-13192.html
    accent_policy = AccentPolicy()
    accent_policy.AccentState = 3  # ACCENT_ENABLE_BLURBEHIND;

    win_comp_attr_data = WINCOMPATTRDATA()
    win_comp_attr_data.Attribute = 19  # WCA_ACCENT_POLICY
    win_comp_attr_data.SizeOfData = ctypes.sizeof(accent_policy)
    win_comp_attr_data.Data = ctypes.pointer(accent_policy)

    hwnd = c_int(Window.winId())
    return SetWindowCompositionAttribute(hwnd, ctypes.pointer(win_comp_attr_data))
