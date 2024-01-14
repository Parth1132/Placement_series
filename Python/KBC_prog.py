questions = [
    ["What is the capital of France?", "Paris", "Berlin", "London", "Rome", 4],
    [
        "Who wrote 'Romeo and Juliet'?", "William Shakespeare",
        "Charles Dickens", "Jane Austen", "Mark Twain", 3
    ],
    [
        "What is the largest mammal on Earth?", "Blue Whale", "Elephant",
        "Giraffe", "Hippopotamus", 2
    ],
    [
        "Which planet is known as the 'Red Planet'?", "Mars", "Venus",
        "Jupiter", "Saturn", 1
    ],
    [
        "What is the main ingredient in guacamole?", "Avocado", "Tomato",
        "Onion", "Cilantro", 3
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
i = 0
for i in range(0, len(questions)):
  question = questions[i]
  print(f"Questions for Rs. {levels[i]}")
  print(f"a. {question[1]}     b.{question[2]}")
  print(f"c. {question[3]}     d.{question[4]}")
  reply = int(input("Enter your answer (Type-in (1-4) or 0 to quit):"))

  if (reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if (i == 4):
      money = 10000
    elif (i == 9):
      money = 320000
    elif (i == 14):
      money = 10000000
  else:
    print("Sorry Wrong answers")
    break

print(f"Your takeaway money is {money}")