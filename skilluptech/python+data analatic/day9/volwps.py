letter = input("Enter the word: ")
store=0

for ch in letter:
    if ch.lower() in ['a','e','i','o','u']:
        print("vowel present")
        store=1
        break

# if no vowls
if store==0:
    print("No vowrls presrnt")

			
