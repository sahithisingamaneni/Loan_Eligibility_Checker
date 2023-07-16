# loan_eligibility_checker

**loan_eligibility_checker Readme**

This repository contains a Python program that allows users to apply for loans and determines their eligibility based on specific criteria. The application prompts users to input their name, age, income status, and other loan-related details. It then calculates the interest rate and loan amount based on the user's input and presents the eligibility results.

**Usage:**

1. Ensure you have Python 3 installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt and navigate to the cloned directory.
4. Run the program by executing the following command:
   ```
   python loan_eligibility.py
   ```
5. Follow the on-screen instructions to input your details and apply for a loan.

**Features:**

- Name validation: The program checks if the name provided is between 2 and 20 characters long and contains only letters.
- Age validation: Applicants must be between 21 and 65 years old to be eligible for a loan.
- Income status: Users with a stable income can enter their annual income amount, while others can choose a specific loan type to apply for.
- Loan types: The program supports various loan types, including personal, home, education, car, business, and gold loans.
- CIBIL score: Applicants are asked to provide their CIBIL score (ranging from 300 to 900) to adjust the interest rate accordingly.
- Loan amount and interest calculation: The program calculates the total loan amount and interest amount based on the loan type, loan amount, interest rate, and tenure.

**Note:**

- The interest rates and loan terms in this program might not reflect real-world financial institutions' actual rates and terms.
- The loan application system may not be complete or optimized for production use and is intended for demonstration purposes only.

**Contributing:**
Contributions, bug reports, and feedback are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

**License:**
This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to explore the code and adapt it to your needs. Happy loan application!
