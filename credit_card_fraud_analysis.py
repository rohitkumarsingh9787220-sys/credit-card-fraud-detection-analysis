import pandas as pd

print("Credit Card Fraud Detection Analysis")

total_transactions = 10000
fraud_transactions = 172

fraud_percentage = (fraud_transactions / total_transactions) * 100

print("Total Transactions:", total_transactions)
print("Fraud Transactions:", fraud_transactions)
print("Fraud Percentage:", round(fraud_percentage, 2), "%")
