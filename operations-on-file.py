# Notes cleaner
#Topic: read(n), readlines(), loop through files, filter lines, copy off lines

#part 1 - sneak peak
n = int(input("how many characters to preview?"))
file = open("class-notes.txt", "r")
print(file.read(n))
file.close()
print()

#part 2 - all lines as a list
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
print("total lines: ", len(lines))
for i in range(len(lines)):
    print(f" i = {i}, ==> {lines[i].strip()}")
print()

#part 3 - filter lines
word = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip =>", line.strip())
    else:
        print("keep =>", line.strip())
file.close()
print()


#part 4 - copy odd lines to new files
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len*(lines), 2):
    out.write(lines[i])
out.close()
print("odd lines saved to odd-lines.txt")