# 📅 Professional Age Calculator (Termux Python)

A smart, logic-based Age Calculator written in **Python**. This tool calculates your exact age in **Years, Months, and Days** by comparing the current date with your birthdate.

## 🚀 Overview

Unlike simple calculators that only subtract years, this script handles the complexity of days and months, including borrowing days from months when needed, ensuring a precise result.

## 🛠️ Features

- **Real-time Date:** Automatically fetches the current date using the `datetime` module.
- **Manual Logic:** Uses custom logic to handle date differences (borrowing 30 days or 12 months).
- **Lightweight:** Runs perfectly on **Termux** or any Python environment.
- **User-Friendly:** Simple command-line interface.

## 💻 How it Works

The script uses the following logic to ensure accuracy:

1. It compares the current day with the birth day. If current is less, it borrows 30 days from the current month.
2. It compares the months. If current is less, it borrows 12 months from the current year.
3. Finally, it calculates the absolute difference to display your age.

## 📥 Installation & Usage

To run this project on your device:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MZDANWN/Age-Calculator.git](https://github.com/MZDANWN/Age-Calculator.git)
   ```
