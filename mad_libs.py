   # Python Mad Libs Warm-Up Activity

   # Welcome message
print("Welcome to Python Mad Libs!")
print("Answer the following questions to create your very own silly story.\n")

name = input("Enter a name: ")
name2 = input("Enter another name: ")
adjective = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ") 
adjective3 = input("Enter another adjective: ") 
noun = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb = input("Enter a verb: ")
verb2 = input("Enter another verb: ")   
adverb = input("Enter an adverb: ") 
adverb2 = input("Enter another adverb: ")   
onomatopoeia = input("Enter an onomatopoeia: ")
item = input("Enter an item: ")


   # Build the story using an f-string
story = (
    f"Today,{name} saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
    f"I couldn't believe my eyes because it went {onomatopoeia}!\n"
    f"I was so {adjective2} that I {verb2} {adverb2} too!\n"
    f"{name2} then went and obtained a {adjective3} {item} that made him very {adjective}.\n"
    f"{name2} was so {adjective} that he {verb2} {adverb2}. \n"
    f"{name} and {name2} now were going to see if the {item} was {adjective3}.\n"
    f"They got the shop and the shopkeeper was very {adjective}.\n"
    f"The {item} was {adjective3} and {name2} was very {adjective}.\n"
    f"{name} said that they were finally done with quest and they both were {adjective2}.\n"
    f"{name} and {name2} could finally rest end their day with a {adjective} {noun2}."
   )

   # Display the completed story
print("\nHere is your story:")
print(story)

for i in range(10):
    restart = input("Do you want to create another story? (yes/no): ")
    if restart == "no":
        print("Thank you for playing Python Mad Libs!")
        break
    print("Let's create another story! \n")
    name = input("Enter a name: ")
    name2 = input("Enter another name: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ") 
    adjective3 = input("Enter another adjective: ") 
    noun = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")   
    adverb = input("Enter an adverb: ") 
    adverb2 = input("Enter another adverb: ")   
    onomatopoeia = input("Enter an onomatopoeia: ")
    item = input("Enter an item: ")
    story = (
        f"Today,{name} saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
        f"I couldn't believe my eyes because it went {onomatopoeia}!"
   )
    print("\nHere is your new story:")
    print(story)
 



