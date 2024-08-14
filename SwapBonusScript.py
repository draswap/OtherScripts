# Parameters
T = 50000  # Total reward (DNB)
FACTOR = 100  # Adjustment factor

# User data (transaction volume V_i and NFT data (quantity, level))
user_data = {
    'User1': {'V': 1000, 'NFT': [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]},
    'User2': {'V': 500, 'NFT': [(3, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]},
    'User3': {'V': 300, 'NFT': [(0, 1), (2, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]},
    'User4': {'V': 200, 'NFT': [(1, 1), (1, 3), (0, 2), (0, 4), (0, 5), (0, 6), (0, 7)]},
    'User5': {'V': 100, 'NFT': [(1, 1), (0, 2), (1, 4), (0, 5), (0, 6), (0, 7)]},
}

# NFT weights
NFT_WEIGHTS = {
    1: 1,
    2: 3,
    3: 12,
    4: 74,
    5: 823,
    6: 24690,
    7: 17283000
}

# Calculate total NFT weight W_i
def calculate_total_nft_weight(nft_list):
    return sum(quantity * NFT_WEIGHTS[level] for quantity, level in nft_list)

# Calculate impact factor F_i
def calculate_impact_factor(V, W):
    return V + FACTOR * W

# Calculate reward for each user
def calculate_reward(F_i, F_total):
    return (F_i / F_total) * T

# Calculate impact factor for each user
total_impact_factor = 0
user_impact_factors = {}
user_weights = {}

for user, data in user_data.items():
    V = data['V']
    nft_list = data['NFT']
    W = calculate_total_nft_weight(nft_list)
    F_i = calculate_impact_factor(V, W)
    user_impact_factors[user] = F_i
    user_weights[user] = W
    total_impact_factor += F_i

# Calculate reward for each user
user_rewards = {}
for user, F_i in user_impact_factors.items():
    user_rewards[user] = calculate_reward(F_i, total_impact_factor)

# Print transaction volume, total NFT weight, impact factor, and reward for each user
print("User Details:")
for user in user_data.keys():
    V = user_data[user]['V']
    W = user_weights[user]
    F_i = user_impact_factors[user]
    reward = user_rewards[user]
    print(f"{user}: Transaction Volume = {V}, Total NFT Weight = {W}, Impact Factor = {F_i:.2f}, Reward = {reward:.18f} DNB")

# Print total impact factor
print(f"\nTotal Impact Factor: {total_impact_factor:.2f}")

# Verify total reward distribution equals 50,000 DNB
total_reward = sum(user_rewards.values())
print(f"\nTotal Reward Distribution: {total_reward:.2f} DNB")
print(f"Calculation result is correct: {abs(total_reward - T) < 1e-2}")
