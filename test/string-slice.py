data = "my name is atikur rahman"
# print(data[4::4])
# print(data[2::2])
# print(data[-1])
# for i in data:
#     print(i[-1])

# print(data[1:24:2])
# print(data[0:23:2])

story = "once upon a time Atikur Rahman created python tutorial with notes"
print(len(story))

# print(story.endswith("notes"))
# total=story.count('a')
# print(f"total a = {total}")

# total=story.count('b')
# print(f"total b = {total}")

# total=story.count('i')
# print(f"total i = {total}")

# total=story.count('c')
# print(f"total c = {total}")

# total=story.count('n')
# print(f"total n = {total}")

print("======================Capitalization=============================")

print(story.capitalize())
print(data.capitalize())
print(data.find("atikur"))
print(story.find("Atikur"))
print("================================replace=====================================")
print(story.replace("Atikur","Aoupo"))
print(story.replace("Rahman","Vai"))

print("==================================scape sequence==========================")
new_story="this is a new \tstory \nof our beautiful country"

print(new_story)