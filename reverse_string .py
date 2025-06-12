#reverse_string 
text = "Hello"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text) 
print(reversed_text[0:1])