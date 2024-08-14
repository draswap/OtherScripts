initial_reward = 50000
halving_interval = 2100000 
total_supply = 0
current_height = 0
current_reward = initial_reward
halving_count = 0
total_time = 0
block_time_seconds = 12 

print(f"{'Halving':<12} {'Reward':<15} {'Total Supply':<25} {'Block Height':<15} {'Time (Days)':<12} {'Accumulated Time (Days)':<15}")
print("=" * 107)

while current_reward >= 1:
    tokens_generated = current_reward * halving_interval
    total_supply += tokens_generated
    current_height += halving_interval

    period_time = (halving_interval * block_time_seconds) / (60 * 60 * 24)
    total_time += period_time
    
    print(f"{halving_count:<12} {current_reward:<15.2f} {total_supply:<26} {current_height:<16} {period_time:<15.2f} {total_time:<15.2f}")
    
    current_reward /= 2
    halving_count += 1

print("=" * 107)
print(f"  Total supply: {total_supply},   Total block height: {current_height},   Total time: {total_time:.2f} days")
