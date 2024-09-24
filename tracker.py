from costs import Values
import pandas as pd

def main():
    print("Running tracker")
    file_path = "costs.csv"

    # Get user to input value
    #value = get_user_input()

    # Write the input to a file
    #save_user_input(value, file_path)

    # Read the file and summarise
    summarise_costs(file_path)

def get_user_input():
    print("Getting user input")
    value_name = input("Enter cost name:")
    value_amount = float(input("Enter cost amount:"))
    value_month = input("Enter month of cost:")

    value_categories = ['Fixed cost', 'Variable cost', 'Income']

    while True:
        print("Select cost category: ")
        for i, category_name in enumerate(value_categories):
            print(f" {i + 1}. {category_name}")

        selected_index = int(input("Enter a category number:")) - 1

        if selected_index in range(len(value_categories)):
            selected_category = value_categories[selected_index]
            new_cost = Values(name = value_name, 
                              category = selected_category, 
                              amount = value_amount, 
                              month = value_month)
            return new_cost
        else:
            print("Invalid category, please try again")

def save_user_input(value: Values, file_path):
    print("Saving user input: {cost} to {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{value.name}, {value.amount}, {value.category}, {value.month}\n")

def summarise_costs(file_path):
    print("Summarising costs")
    with open(file_path, "r") as f:
        df = pd.read_csv(f)
        df_grouped = df.groupby(['month', 'category'])['amount'].sum()
        print(df_grouped)

if __name__ == "__main__":
    main()