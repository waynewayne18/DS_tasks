
#slicing very fast
caps = ['A', 'B', 'C', 'D',  'E'] #multiple array quicker to access than 1
lower = ['a', 'b', 'c', 'd', 'e']
num = ['1', '2', '3', '4', '5']
spec = ['$', '&', '%']

caps_no = 0
lower_no = 0
num_no = 0
spec_no = 0

current_pass_elements_bank = ["C", "L", "N", "S"]
current_pass_elements = ["C", "L", "N", "S"]
current_pass = "Aa1$"     

while chars >= 4:
    chars = int(input("enter number of characters"))
    if chars < 4:
        print("chars must be >= 4")
chars -= 4
current_pass += caps[0] * chars
current_pass_elements(["C"] * chars)

def bruteforce(current_pass, caps_no, lower_no, num_no, spec_no, caps, lower, num, spec):
    for i in range(current_pass):
        if current_pass[i] not in caps:
            caps_no += 1
            current_pass_elements[i] = current_pass_elements_bank[0]

        elif current_pass[i] not in lower:
            lower_no += 1
            current_pass_elements[i] = current_pass_elements_bank[1]

        elif current_pass[i] not in num:
            num_no += 1
            current_pass_elements[i] = current_pass_elements_bank[2]

        elif current_pass[i] not in spec:
            spec_no += 1
            current_pass_elements[i] = current_pass_elements_bank[3]

        if current_pass_elements[i] == "C":
            for iter_cap in caps:
                if iter_cap != current_pass[i]:
                    current_pass[i] = iter_cap

        elif current_pass_elements[i] == "L":
            for iter_lower in caps:
                if iter_lower != current_pass[i]:
                    current_pass[i] = iter_lower
        
        elif current_pass_elements[i] == "N":
            for iter_num in caps:
                if iter_num != current_pass[i]:
                    current_pass[i] = iter_num
        
        elif current_pass_elements[i] == "S":
            for iter_spec in caps:
                if iter_spec != current_pass[i]:
                    current_pass[i] = iter_spec

        
        
    


    return bruteforce(current_pass)



bruteforce(current_pass, chars, caps_no, lower_no, num_no, spec_no)
with open ('output.txt', 'w') as file:
    file.write(current_pass)