#Task 1

city = "london"

print(city)

#Task 2

city = "Berlin"

population = 3645000

print(city, str(population), sep =":")

#Task 3

city = "London"

population = 9000000

print("City:", city, str(isinstance(city, str)), "\nPopulation:", population)

#Task 4

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital "

# word_to_find = "capital"
# found = text.find(word_to_find)

# if found !=-1:
#     print(f"{word_to_find}: {found}")

found = text.find("capital")

if found !=-1:
    print(f"capital: {found}")

#Task 5
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

new_text = text.split(" ")
print(new_text)


#Task 6

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(text.replace("capital", "capital of Germany"))
