from game_setup.european_roulette_setup import eu_roulette_wheel
import sys


for game_initiation in range(10):
    user_ready = input("Type 'go' when ready to play --->")
    if user_ready == "go":
        spin = eu_roulette_wheel.spin()
        print(f"Spin outcome: {spin['number_return']}, {spin['colour_return']}")
        break
else:
    sys.exit("Game over")



