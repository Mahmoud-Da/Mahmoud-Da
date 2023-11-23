import requests

username = "Mahmoud-Da"
repository = "Mahmoud-Da"

# Fetch language data from GitHub API
url = f"https://api.github.com/repos/{username}/{repository}/languages"
response = requests.get(url)
data = response.json()

# Print all languages and their percentages
for language, percentage in data.items():
    print(f"{language}: {percentage}%")
