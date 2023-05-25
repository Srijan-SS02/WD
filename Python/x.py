def watering_plants(plants, capacity):
    steps = 0
    water = capacity
    
    for plant in plants:
        if plant <= water:
            water -= plant
        else:
            steps += 2
            water = capacity - plant
            
    steps += len(plants) - 1  # account for the final step to return to the river
    
    return steps

plants = list(map(int, input("Enter the water requirements of the plants, separated by spaces: ").split()))
capacity = int(input("Enter the capacity of the watering can: "))

steps = watering_plants(plants, capacity)

print(f"The number of steps required to water all the plants is {steps}.")
