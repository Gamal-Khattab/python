# python-assignments-lesson-from-51-to-55#######[1]########
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# my_nums.sort(reverse=True)
# n = 0
# for numbers in my_nums:
#     if numbers % 5 == 0:
#         n += 1
#         print(f"{n} => {numbers}")
# else:
#     print("the loop is finished!")

# python-assignments-lesson-from-51-to-55#######[2]########
# for x in range(1, 21):
#     if x < 10:
#         if x == 6 or x == 8:
#             continue
#         else:

#             x = str(x)
#             print(x.zfill(2))
#     elif x == 12:
#         continue
#     else:
#         print(x)
# else:
#     print("the loop is finished!")

# python-assignments-lesson-from-51-to-55#######[3]########
# my_ranks = {
#     'Math': 'A',
#     "Science": 'B',
#     'Drawing': 'A',
#     'Sports': 'C'
# }
# m = 0
# for skill_key, skill_value in my_ranks.items():
#     if skill_key == "Math" and skill_value == "A":
#         skill_value = 100
#         print(f"my rank in {skill_key} is A => {skill_value} points ")
#         m += skill_value
#     if skill_key == "Science" and skill_value == "B":
#         skill_value = 80
#         print(f"my rank in {skill_key} is B => {skill_value} points ")
#         m += skill_value
#     if skill_key == "Drawing" and skill_value == "A":
#         skill_value = 100
#         print(f"my rank in {skill_key} is A => {skill_value} points ")
#         m += skill_value

#     if skill_key == "Sports" and skill_value == "C":
#         skill_value = 40
#         print(f"my rank in {skill_key} is C => {skill_value} points ")
#         m += skill_value

# else:
#     print(f"all total points equal => {m}")


# python-assignments-lesson-from-51-to-55#######[4]########
# students = {
#     "Ahmed": {
#         "Math": "A",
#         "Science": "D",
#         "Draw": "B",
#         "Sports": "C",
#         "Thinking": "A"
#     },
#     "Sayed": {
#         "Math": "B",
#         "Science": "B",
#         "Draw": "B",
#         "Sports": "D",
#         "Thinking": "A"
#     },
#     "Mahmoud": {
#         "Math": "D",
#         "Science": "A",
#         "Draw": "A",
#         "Sports": "B",
#         "Thinking": "B"
#     }
# }
# a = 0
# b = 0
# c = 0
# for student_key, students_value in students.items():
#     for child_key, child_value in students_value.items():
#         if student_key == "Ahmed":
#             if child_value == "B":
#                 child_value = 80
#                 a += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "A":
#                 child_value = 100
#                 a += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "B":
#                 child_value = 80
#                 a += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "C":
#                 child_value = 40
#                 a += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "D":
#                 child_value = 20
#                 a += child_value

#                 print(f"{child_key} => {child_value} points ")
#         elif student_key == "Sayed":
#             if child_value == "B":
#                 child_value = 80
#                 b += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "A":
#                 child_value = 100
#                 b += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "B":
#                 child_value = 80
#                 b += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "C":
#                 child_value = 40
#                 b += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "D":
#                 child_value = 20
#                 b += child_value

#                 print(f"{child_key} => {child_value} points ")
#         elif student_key == "Mahmoud":
#             if child_value == "B":
#                 child_value = 80
#                 c += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "A":
#                 child_value = 100
#                 c += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "B":
#                 child_value = 80
#                 c += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "C":
#                 child_value = 40
#                 c += child_value
#                 print(f"{child_key} => {child_value} points ")
#             elif child_value == "D":
#                 child_value = 20
#                 c += child_value

#             print(f"{child_key} => {child_value} points ")

#     else:
#         print(
#             f"total points for ahmed is {a} for sayed is {b} for mahoumed is {c} ")
