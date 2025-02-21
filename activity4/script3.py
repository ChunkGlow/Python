def count_notes(amount):

  denomonations = [1000, 500, 200, 100, 50, 20, 5, 1]
  note_count = {}

  index = 0

  while amount > 0: 
   
   if amount >= denomonations[index]:
       note_count[denomonations[index]] = amount // denomonations[index]
       amount %= denomonations[index]
       index += 1
       
  return note_count
 
# part ii

amount = int(input("Enter the Amount in PHP : "))

notes = count_notes(amount)

print("\n Minimium Number of Notes : ")
for note, count in notes.items():
  print(f"₱ {note} : {count} pcs")

