import glob
import os

# Hämta den exakta mappen där detta skript sparats
skript_mapp = os.path.dirname(os.path.abspath(__file__))
sok_monster = os.path.join(skript_mapp, "**", "*.py")
utfil_sokvag = os.path.join(skript_mapp, "alla_losningar.txt")

with open(utfil_sokvag, "w", encoding="utf-8") as outfile:
    for filename in sorted(glob.glob(sok_monster, recursive=True)):
        # Hoppa över utfilen eller skriptet självt
        if filename == utfil_sokvag or filename.endswith("samla_filer.py"):
            continue

        relativ_sokvag = os.path.relpath(filename, skript_mapp)

        outfile.write(f"========================================\n")
        outfile.write(f"FIL: {relativ_sokvag}\n")
        outfile.write(f"========================================\n\n")

        with open(filename, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())

        outfile.write("\n\n\n")

print(f"Klart! Filen skapades i: {utfil_sokvag}")