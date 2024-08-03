import random

def get_season():
    try:
        season =input("Enter the season: summer or winter: ").lower()
        if season == "summer" or season == "winter":
            return season
    except ValueError:
            print("Please enter summer or winter")

def get_gender():
    while True:
        gender = input("Enter the gender: male or female: ")
        if gender == "male" or gender == "female":
            return gender
        else:
            print("Please enter male or female")

def get_fit(season, gender):
    outfits = {
    'winter': {
      'male': ["Sweater, jeans, and boots", "Coat, scarf, and gloves", "Hoodie, jeans, and beanie","Scarf,cargo pants and fur coat"],
      'female': ["Sweater dress, tights, and boots", "Coat, scarf, and gloves", "Hoodie, leggings, and beanie" , "biker jacket, jeans and fur boots"],

    },
    'summer': {
      'male': ["T-shirt, shorts, and sandals", "Polo shirt, chinos, and loafers", "Tank top, jeans, and sneakers", "linen shirt, shorts, and sandals"],
      'female': ["Dress and sandals", "Crop top, skirt, and heels", "Tank top, shorts, and sneakers", "strawhat, midi , crocs"]

    }
  }
    return random.choice(outfits[season][gender])

def main():
    season = get_season()
    gender = get_gender()
    fit = get_fit(season, gender)
    print(fit)

if __name__ == "__main__":
    main()




