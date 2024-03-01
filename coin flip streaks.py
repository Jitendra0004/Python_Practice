import random
streak = 0
coin_toss = []

# first generate randomly selected heads and tails
for experiments in range(10000):
    for i in range(100):
        coin_toss += [random.choice(['H','T'])] #heads or tails
    #print(coin_toss)
    #print(len(coin_toss))

    #second checks if there is a streak in it 

    for i in range(94):
        if coin_toss[i:i+6] == ['H', 'H', 'H', 'H', 'H','H' ] or coin_toss[i:i+6] == ['T','T','T','T','T','T'] :
            streak += 1
            #print(coin_toss[i:i+6])

print(f'percentage of streak of 6 is {streak/100/10000}%')
     
