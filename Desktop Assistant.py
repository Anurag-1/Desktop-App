import os

print("Desktop Assistant")
while True:
	print("Hi, how can I help? : "  , end='')
	userInput = input().lower()
	
	if ("run" in userInput) or ("open" in userInput) or ("execute" in userInput) or ("look" in userInput) or ("need" in userInput) or ("want" in userInput):
		if ("gmail" in userInput) or ("mail" in userInput):
			os.system("chrome gmail.com")
	
		elif ("browser" in userInput) or ("chrome" in userInput):
			os.system("chrome")
			
		elif ("firefox" in userInput):
			os.system("firefox")
	
		elif ("notepad++" in userInput) or ("editor++" in userInput):
			os.system("notepad++")
			
		elif ("notepad" in userInput) or ("editor" in userInput):
			os.system("notepad")
			
		elif (("audio" in userInput) or ("media" in userInput)) and ("player" in userInput):
			os.system("wmplayer")
			
		elif ("calc" in userInput) or ("calculator" in userInput):
			os.system("calc")
			
		elif ("skype" in userInput) or ("video call" in userInput):
			os.system("lync")
			
		elif ("excel" in userInput):
			os.system("EXCEL")
			
		elif ("msaccess" in userInput) or ("access" in userInput):
			os.system("MSACCESS")
			
		elif ("mspub" in userInput) or ("mspublisher" in userInput) or ("publisher" in userInput):
			os.system("MSPUB")
	
		elif ("outlook" in userInput) or ("office365" in userInput):
			os.system("OUTLOOK")
		
		elif ("ppt" in userInput) or ("powerpoint" in userInput):
			os.system("POWERPNT")

		elif ("word" in userInput) or ("document" in userInput):
			os.system("WINWORD")
		
		elif ("code" in userInput) or ("vscode" in userInput) or ("visual studio" in userInput):
			os.system("Code")	
			
		elif ("setting" in userInput):
			os.system("start ms-settings:")
		
		elif ("explorer" in userInput) or ("this pc" in userInput) or ("mycomputer" in userInput) or ("drive" in userInput):
			os.system("Explorer,")
			
		else:
			print(userInput,"doesn't support")
	
	elif ("exit" in userInput) or ("quit" in userInput) or ("close" in userInput) or ("terminate" in userInput):
		break
		
	elif (userInput != ""):
		print("try \"run "+userInput+"\" or \"open "+userInput+"\"")
		
	else:
		print("plz mention your requirement...")

	