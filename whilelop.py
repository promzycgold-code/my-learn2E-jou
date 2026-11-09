def load_price(text):
    price = int(text)
    return price * 2
 
def main():
    print("Start")
    total = load_price("abc")
    print("Total:", total)
 
main()
print("Done")