# Ask the user for their email address
email = input("Enter your email address: ")

# Split the email into username and domain
username = email[:email.index("@")]
domain = email[email.index("@"): + 1]

# Display the results
print(f"Username: {username}")
print(f"Domain: {domain}")