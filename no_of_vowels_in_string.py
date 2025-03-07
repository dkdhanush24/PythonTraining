vowels = ['a','e','i','o','u','A','E','I','O','U']
string = input()
count = 0
for i in range(len(string)):
    if(string[i] in vowels):
        count+=1
if count == 0:
    print("No vowels were found.")
else:
    print(f"Total number of vowels: {count}")
    
