s1 = raw_input("Type the important thing in brackets: ")

left = s1.find('[')
leftone = left + 1

s2 = s1[leftone:]

right = s2.find(']')

s3 = s2[:right]

print(s3)