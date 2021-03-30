



r = open("allfolders.txt", "w")
r.write('''Desktop/    Downloads/  Pictures/  snap/       Videos/
Documents/  Music/      Public/    Templates/
''')

r.close()
with open("allfolders.txt", "r") as f:
	f.read()


