from itertools import product

set = ['A', 'B', 'C', 'D',  'E', 'a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '$', '&', '%']
CAPs = ['A', 'B', 'C', 'D', 'E']
lower = ['a', 'b', 'c', 'd', 'e']
num = ['1', '2', '3', '4', '5']
spec = ['$', '&', '%']


current = 'AAAA'
chars = int(input("enter number of characters"))

while chars < 4:
    chars = int(input("enter number of characters \n"))
    print("chars must be >= 4")
if chars > 4:
    current += 'A' * (chars - 4)

with open("output.txt", "a") as file:
    for a in product(set, repeat = chars):
        curr_pass = "".join(a)#used all any for speed and swag

        if all(any(i in curr_pass for i in s) for s in [CAPs, lower, num, spec]):#embed if for read
            if sum(curr_pass.count(d) for d in CAPs) <=2 and sum(curr_pass.count(b) for b in spec) <=2:
                if a[0] in CAPs:
                    file.write(curr_pass)
                    file.write("\n")