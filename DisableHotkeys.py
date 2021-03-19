import keyboard

def DisableHotkeys(hotkeys = ["alt + f4", "alt + tab"]):
	for i in range(len(hotkeys)):
		keyboard.add_hotkey(hotkeys[i], lambda: None, suppress = True)


def EnableHotkeys(hotkeys = ["alt + f4", "alt + tab"]):
	for i in range(len(hotkeys)):
		keyboard.add_hotkey(hotkeys[i], lambda: None, suppress = False)
	#keyboard.add_hotkey("ctrl + alt + del", lambda: None, suppress =True)