import requests

BASE_URL = "https://catfact.ninja/"
BREEDS_ENDPOINT = BASE_URL + "breeds"

country = input("Introduce the country (e.g. Russia, United Kingdom or United States): ")

req = requests.get(BREEDS_ENDPOINT)
if not req.ok:
    print("Error fetching data from the API.")
    exit()
num_pages = req.json()["last_page"]

def get_breeds(page: int):
    req = requests.get(BREEDS_ENDPOINT, params={"page": page})
    if req.ok:
        return req.json()["data"]
    else:
        print("Error fetching data from the API.")
        return []

breeds = []
countries = set()

for page in range(1, num_pages):
    brs = get_breeds(page)
    for breed in brs:
        breeds.append(breed)
        countries.add(breed['country'])

if country not in countries:
    print(f"Country {country} doesn't have any breed. Try with another country.")
    print(f"Available countries are:")
    for c in countries:
        print(f"- {c}")
    exit()

# print(f"Total breeds fetched: {len(breeds)}")
# print(f"Breeds: {breeds}")

filtered_breeds = []
for breed in breeds:
    if breed['country'] == country:
        filtered_breeds.append(breed)

if len(filtered_breeds) == 0:
    print(f"The country {country} has no breeds.")
else:
    print(f"Country {country} has {len(filtered_breeds)} breeds:")
    for breed in filtered_breeds:
        print(f"""
        Breed   : {breed['breed']}
        Country : {breed['country']}
        Origin  : {breed['origin']}
        Coat    : {breed['coat']}
        Pattern : {breed['pattern']}
        """)
