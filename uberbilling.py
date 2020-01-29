c = int(input('1. car\n2. bike\n3. auto\n\nEnter your choice: '))

carfare = 15
bikefare = 5
autofare = 10

km = int(input('Enter the distance travelled in km: '))

fare = 0

if c == 1:
    fare = km * carfare
elif c == 2:
    fare = km * bikefare
elif c == 3:
    fare = km * autofare
else:
    print('Invalid option')
    
print('Your fare is ', fare)
