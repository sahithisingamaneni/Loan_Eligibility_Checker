while True:
    name = input("Name: ")
    if len(name) < 2 or len(name) > 20:
        print("Please enter a valid name.")
    elif not name.isalpha():
        print("Your name must only contain letters.")
    else:
        age = int(input("Please enter your age: "))
        if age < 21 or age > 65:
            print("You're not eligible currently.")
        else:
            income = input("Do you have a stable income? (yes or no): ")
            if income.lower() == "yes":
                while True:
                    try:
                        income_amount = float(input("Annual income amount: "))
                        if income_amount <= 0:
                            print("Your income amount must be positive.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid income amount.")
            elif income.lower() == "no":
                loan_type = input("Select a loan type: ").lower()
                if loan_type == "gold" or loan_type == "gold loan":
                    loan_amount = float(input("Enter the loan amount: "))
                    interest_rate = 9.0
                    tenure = int(input("Loan period (months): "))
                    interest_amount = (loan_amount * interest_rate * tenure) / (12 * 100)
                    total_amount = loan_amount
                    print("Congratulations! You are eligible for a loan.")
                    print("Total Amount:", total_amount)
                    print("Interest Amount:", interest_amount)
                    break
                else:
                    print("You are not eligible for a loan without a stable income.")
                    break
            else:
                print("Please enter 'yes' or 'no'.")
            a = ["Personal loan", "Home loan", "Education loan", "Car loan", "Business loan", "Gold loan"]
            print(*a)
            loan_type = input("Select a loan type: ").lower()
            if not any(keyword in loan_type for keyword in ["personal", "home", "education", "car", "business", "gold"]):
                print("Please enter a valid loan type.")
            else:
                loan_amount = float(input("Enter the loan amount: "))
                if loan_type == "personal" or loan_type == "personal loan":
                    if loan_amount <= 100000:
                        interest_rate = 8.0
                    else:
                        interest_rate = 8.5
                elif loan_type == "home" or loan_type == "home loan":
                    if loan_amount <= 5000000:
                        interest_rate = 7.5
                    else:
                        interest_rate = 8.0
                elif loan_type == "car" or loan_type == "car loan":
                    if loan_amount <= 500000:
                        interest_rate = 6.5
                    else:
                        interest_rate = 7.0
                elif loan_type == "education" or loan_type == "education loan":
                    if loan_amount <= 2000000:
                        interest_rate = 5.5
                    else:
                        interest_rate = 7.0
                elif loan_type == "business" or loan_type == "business loan":
                    if loan_amount <= 75000000:
                        interest_rate = 8.5
                    else:
                        interest_rate = 10.0
                else:
                    print("Please enter a valid loan type.")
                    continue
                print("Interest rate is:", interest_rate)
                
                while True:
                    try:
                        cibil_score = int(input("CIBIL score (between 300 and 900): "))
                        if cibil_score < 300 or cibil_score > 900:
                            print("You are not eligible for the loan.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid CIBIL score.")
                
                if cibil_score < 500:
                    if loan_amount <= 100000:
                        interest_rate += 1.5
                    else:
                        interest_rate += 2.0
                elif cibil_score < 700:
                    if loan_amount <= 100000:
                        interest_rate += 0.5
                    else:
                        interest_rate += 1.0
                # Add more CIBIL score ranges here
                print("Final interest rate is:", interest_rate)
                while True:
                    try:
                        tenure = int(input("Loan period (months): "))
                        if tenure <= 0:
                            print("The tenure must be positive.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid tenure.")
                interest_amount = (loan_amount * interest_rate * tenure) / (12 * 100)
                total_amount = loan_amount
                print("Congratulations! You are eligible for a loan.")
                print("Total Amount:", total_amount)
                print("Interest Amount:", interest_amount)
                break
        break  # End the loop after eligibility check
    print("You are not eligible for a loan.")