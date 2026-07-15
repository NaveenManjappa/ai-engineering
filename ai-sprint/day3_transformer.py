import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users")

# print(type(response.text))
users = json.loads(response.text)
# print(type(users[0]))
# print(users)


def get_users_by_city(users):
    users_by_city = {}
    # print(type(users_by_city))
    print(users_by_city)
    city = users[0]["address"]["city"]
    # print(city)
    for i, user in enumerate(users):
        city = users[i]["address"]["city"]
        # print(city)
        if city not in users_by_city:
            # print(f"City {city} does not exist yet")
            users_by_city[city] = []
            users_by_city[city].append(user)
        else:
            users_by_city[city].append(user)
    return users_by_city


def get_email_domains(users):
    email_domains = set()
    for user in users:
        email_domains.add(str(user["email"]).split("@")[1])
    print(email_domains)
    return email_domains

def generate_summary(users):
    users_city=get_users_by_city(users)
    unique_city_count=len(users_city.keys())
    users_count=sum(len(users_city[city]) for city in users_city)
    email_domain_count=len(get_email_domains(users))
    return {
        "unique_city_count":unique_city_count,
        "total_user_count":users_count,
        "unique_domain_count":email_domain_count
    }
# Get users by count
users_by_city = get_users_by_city(users)
# print(users_by_city)
with open("users_data.json", "w") as f:
    json.dump(users_by_city, f, indent=4)

# Get Email domains
user_email_domains = get_email_domains(users)
with open("email_domains.json", "w") as f:
    json.dump(list(user_email_domains), f, indent=4)

#Get the summary
summary = generate_summary(users)

with open("summary.json","w") as f:
    json.dump(summary,f,indent=4)