print("The word counter program\n")
text = input('Enter Sentence: ').lower()
#lower_text = text.lower()
duplicate_words = {}

for word in text.split():
    
    if word in duplicate_words:
        duplicate_words[word] += 1
    else:    
        duplicate_words[word] = 1

       
print(f'{"WORD":<12}COUNT')
   
for word, count in sorted(duplicate_words.items()):
    if count > 1:
        print (f'{word:<14}{count}')

 
 
 
 
 
 
 
 
 
 
 
 
