import requests

def fetch_rover_photos(rover, sol, api_key):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {
        "sol": sol,
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["photos"]

def display_photos(photos):
    for photo in photos:
        img_src = photo["img_src"]
        print(img_src)  # Modify this to display the image or perform other actions

def main():
    api_key = "YOUR_API_KEY"  # Replace with your NASA API key
    rover = "curiosity"
    sol = 1000  # The Martian sol (day) for which you want to fetch photos

    photos = fetch_rover_photos(rover, sol, api_key)
    display_photos(photos)

if __name__ == "__main__":
    main()
