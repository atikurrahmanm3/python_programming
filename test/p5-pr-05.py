# quots = input("write What\'s on your mind?: ")
# print(f"you wroted \'{quots}\' ")

letter = '''Dear, \nName: <|NAME|> \nGreatings From TechReview software firm i am glad to tell you about your selection  \n\'You are selected\' \nDate: <|DATE|> '''

name = input("Enter your name: ")
date = input("Enter a date: ")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)
