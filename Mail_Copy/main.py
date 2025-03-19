#TODO: Create a letter using starting_letter.txt
invited_name = []
letter_body = []
with open("./Input/Names/invited_names.txt", mode="r") as invited_name_file:
    for line in invited_name_file:
        line = line.strip()
        invited_name.append(line)

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    for line in starting_letter:
        line = line.strip()
        letter_body.append(line)

for index in range(len(invited_name)):
    letter_body[0] = "Dear," + invited_name[index]
    #print(letter_body)

    with open(f"./Output/ReadyToSend/{invited_name[index]}.txt", mode="w") as output_letter:
        for line in letter_body:
            line = str(line) +"\n"
            output_letter.write(line)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp