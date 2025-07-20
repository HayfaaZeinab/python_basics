
print("Daily Diary!\n")

thoughts=input("Enter yiur thoughts : ")

# Appending to a file
with open("diary.txt", "a") as file:
    file.write(thoughts)


print("Your thoughts have been saved to diary.txt")


print("High Scores Tracker\n")
file=open("highscores.txt", "w")
file=open("highscores.txt", "r")
lines=file.readlines()
file.close()

print("Current high scores:")
for line in lines:
    print(line.strip())

name=input("\nEnter your name: ")
score=input("Enter your score: ")


file=open("highscores.txt", "a")
file.write(f"{name}: {score}\n")
file.close()

print("Score saved!")

    




