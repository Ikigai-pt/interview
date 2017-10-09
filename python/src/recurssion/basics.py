# Learing recurssion:
#     RecursiveCounter

def r_counter(counter):
    if counter == 0:
        return;
    else:
        print(counter)
        r_counter(counter-1)

def r_factorial(number):
    if number == 1 :
        return 1;
    else:
        return number * r_factorial(number-1)

r_counter(10);
print(r_factorial(5));


