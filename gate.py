from calculation.evaluation import Evaluation

user_attribute = {
    'age': 30,
    'past_order_amount': 60,
    'gender': 'f',
    'days_active': 20,
}

features = {
    'same_day_delivery': '( age > 25 AND gender == "m" ) OR ( past_order_amount > 500 )',
    'discount': '( age > 20 AND gender == "f" ) and ( past_order_amount > 100 )',
    'exclusive_items_access': '( days_active > 19 OR past_order_amount > 100 )',
    'free_coupons': '( ( age > 20 OR days_active > 50 ) AND past_order_amount > 50 AND gender == "f" )'
}

feature_map = {
    1: 'same_day_delivery',
    2: 'discount',
    3: 'exclusive_items_access',
    4: 'free_coupons',
}


if __name__ == "__main__":
    while(1):
        print("User attributes - ", user_attribute)
        print(
            "Select one option: \n"
            "1. same_day_delivery\n"
            "2. discount\n"
            "3. exclusive_items_access\n"
            "4. free_coupons\n"
            "5. Exit()\n"
        )
        option = int(input("Enter a number: "))
        if option == 5:
            break
        if option not in feature_map:
            print("invalid option")

        feature = feature_map[option]
        evaluation = Evaluation()
        try:
            is_allowed = evaluation.evaluate(features[feature], user_attribute)
            if is_allowed:
                print("Congrats!!! user is eligible")
            else:
                print("user is not eligible")

        except Exception as e:
            print(e)

        print("\n")