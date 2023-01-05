#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open("/home/walttersly/Documents/MailMergeProject/Mail Merge Project/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("/home/walttersly/Documents/MailMergeProject/Mail Merge Project/Input/Names/invited_names.txt") as letter:
    letter_content = letter.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, strip_name)
        with open(f"/home/walttersly/Documents/MailMergeProject/Mail Merge Project/Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as fin_letter:
            fin_letter.write(new_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp