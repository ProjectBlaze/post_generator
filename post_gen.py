import datetime

def generate_telegram_post(BlazeVersion, codename, device, date, maintainer):
    post = f"\n#Blaze #{codename} #Android14 #U #Stable\n"
    post += f"Project Blaze v{BlazeVersion} - OFFICIAL | Android 14\n"
    post += f"📲 : {device} ({codename})\n"
    post += f"📅 : {date}\n"
    post += f"🧑‍: @{maintainer}\n\n"
    post += f"▪️ Changelog : Source | Device\n"
    post += f"▪️ Download \n"
    post += f"▪️ Screenshots\n"
    post += f"▪️ Support Group \n"
    post += f"▪️ Community Chat \n"
    post += f"▪️ Updates Channel \n"
    return post

def get_user_input():
    BlazeVersion = input("Enter Blaze Version: ")
    codename = input("Enter device codename: ")
    device = input("Enter device name: ")
    date =  datetime.date.today().strftime("%d-%m-%Y")
    maintainer = input("Enter maintainer name (Don't use @): ")
    return BlazeVersion, codename, device, date, maintainer

def main():
    print("Welcome to Project Blaze post generator!")
    BlazeVersion, codename, device, date, maintainer = get_user_input()
    telegram_post = generate_telegram_post(BlazeVersion, codename, device, date, maintainer)
    print("\nHere is the generated post for the release !")
    print("Don't forget to add the links !\n")
    print(telegram_post)

if __name__ == "__main__":
    main()
