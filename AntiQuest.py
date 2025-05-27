import os
removed = 0
for file in os.listdir("C:/"):
    if file[:7] == "fba_ads":
        os.remove("C:/"+file)
        removed += 1
    elif file[-4:] == ".hdr":
        os.remove("C:/"+file)
        os.remove("C:/"+file[:-4])
        removed += 2
print("Successfully removed "+str(removed)+" files!")
