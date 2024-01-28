
import random

def get_numbers_ticket(min, max, quantity):
    for num in [min, max, quantity]:
        if not (1<= num <= 1000):
            return []
        random_numbers = random.sample(range(min, max+1), quantity)
        return sorted(random_numbers)
        
            
lottery_numbers = get_numbers_ticket(1, 70, 6)
print(lottery_numbers)
