import random
from collections import Counter

# WRITTEN UNDER ASSUMPTION YOU HAVE PREMIUM AND ALWAYS USE DOUBLE GEMS

time_in_seconds = 365 * 86400  # how long the simulation will run (86400 secs = 24 hrs)
number_of_drops = time_in_seconds // 7
double_luck = False  # (True = double luck activated) (False = no double luck)

# sell_value was only applied to auras that have a good chance of selling on market
# sell_value is the average price according to death-ball.fandom.com/wiki/Auras
aura_drops = {
    "Wind": {"chance": 1 / 10, "gems": 78, "sell_value": 0},
    "Ember": {"chance": 1 / 20, "gems": 78, "sell_value": 0},
    "Calm": {"chance": 1 / 30, "gems": 78, "sell_value": 0},
    "Shine": {"chance": 1 / 50, "gems": 78, "sell_value": 0},
    "Flower": {"chance": 1 / 75, "gems": 78, "sell_value": 0},
    "Spirit": {"chance": 1 / 100, "gems": 78, "sell_value": 0},
    "Poison": {"chance": 1 / 200, "gems": 102, "sell_value": 0},
    "Blood": {"chance": 1 / 300, "gems": 102, "sell_value": 0},
    "Inferno": {"chance": 1 / 500, "gems": 102, "sell_value": 0},
    "Electrical": {"chance": 1 / 750, "gems": 102, "sell_value": 0},
    "Rose": {"chance": 1 / 1000, "gems": 102, "sell_value": 0},
    "Shadow": {"chance": 1 / 5000, "gems": 102, "sell_value": 0},
    "Lunar": {"chance": 1 / 20000, "gems": 204, "sell_value": 35000},
    "Hallowtide": {"chance": 1 / 30000, "gems": 204, "sell_value": 25000},
    "Constellation": {"chance": 1 / 50000, "gems": 204, "sell_value": 50000},
    "Eclipse": {"chance": 1 / 75000, "gems": 204, "sell_value": 70000},
    "Angel": {"chance": 1 / 100000, "gems": 204, "sell_value": 275000},
    "Void": {"chance": 1 / 200000, "gems": 384, "sell_value": 175000},
    "Dark Angel": {"chance": 1 / 400000, "gems": 384, "sell_value": 1150000},
    "Portal": {"chance": 1 / 500000, "gems": 384, "sell_value": 375000},
    "Dreamwalker": {"chance": 1 / 700000, "gems": 384, "sell_value": 675000},
    "Timekeeper": {"chance": 1 / 1000000, "gems": 384, "sell_value": 1100000}
}

if double_luck:
    for aura in aura_drops.values():
        aura["chance"] *= 2

double_gems_purchases = time_in_seconds // (20 * 60)
double_luck_purchases = time_in_seconds // (15 * 60)
total_double_gems_cost = double_gems_purchases * 2000
total_double_luck_cost = double_luck_purchases * 5000
both_fruit_cost = total_double_gems_cost + total_double_luck_cost


def simulate_drops(num_drops):
    drop_counts = Counter()
    total_gems = 0
    total_sell_income = 0

    for _ in range(num_drops):
        dropped = False
        for aura_name, data in aura_drops.items():
            if random.random() < data["chance"]:
                drop_counts[aura_name] += 1
                total_gems += data["gems"]
                if data["sell_value"] > 0:
                    total_sell_income += data["sell_value"]
                dropped = True
                break

        if not dropped:
            total_gems += 51

    return drop_counts, total_gems, total_sell_income


drop_counts, total_gems, total_sell_income = simulate_drops(number_of_drops)

combined_total = total_gems + total_sell_income
c_total_with_double_gems = combined_total - total_double_gems_cost
c_total_with_both_fruits = combined_total - both_fruit_cost

print("Frequency Table of Aura Drops:")
print("Aura Name       | Drops")
print("------------------------")
for aura_name in drop_counts.keys():
    count = drop_counts[aura_name]
    print(f"{aura_name:<13} | {count}")

if double_luck:
    print("\nTotals (With Double Gems and Double Luck)")
    print(f"Cost of Double Gems: {total_double_gems_cost}")
    print(f"Cost of Double Luck: {total_double_luck_cost}")
    print(f"Total Gems Collected: {total_gems}")
    print(f"Total Sell Income: {total_sell_income}")
    print(f"Combined Total (Gems + Sell Income): {combined_total}")
    print(f"Combined Total (Gems + Sell Income) After Fruit Costs: {c_total_with_both_fruits}")

else:
    print("\nTotals (With Double Gems)")
    print(f"Cost of Double Gems: {total_double_gems_cost}")
    print(f"Total Gems Collected: {total_gems}")
    print(f"Total Sell Income: {total_sell_income}")
    print(f"Combined Total (Gems + Sell Income): {combined_total}")
    print(f"Combined Total (Gems + Sell Income) After Fruit Costs: {c_total_with_double_gems}")
