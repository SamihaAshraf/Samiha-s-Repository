#Samiha Ashraf
#1884227

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')


if __name__ == "__main__":
    food_item1 = FoodItem()

    item_name = input("")
    amount_fat = float(input(""))
    amount_carbs = float(input(""))
    amount_protein = float(input(""))

    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    num_servings = float(input(""))

    food_item1.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item1.get_calories(num_servings):.2f}')

    print()

    food_item2.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item2.get_calories(num_servings):.2f}')
