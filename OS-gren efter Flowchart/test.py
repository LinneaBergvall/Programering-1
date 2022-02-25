yes = ["Yes", "yes", "Y", "y", "Yes!", "yes!", "Ja", "ja"]
no = ["No", "no", "N", "n", "No!", "no!", "Nej", "nej"]
stop = ["Stop", "stop", "Stop!", "stop!"]
cancel = ["Cancel", "cancel"]

lists = [yes[:], no[:], stop[:], cancel[:]]
if input(">") in lists:
    print("YES")
