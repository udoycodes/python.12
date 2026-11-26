def main():
    str=input("What's str?")
    print(convert(str))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()