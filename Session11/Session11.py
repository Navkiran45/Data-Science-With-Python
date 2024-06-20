# FILE HANDLING

quote1 = "Search the candle rather than cursing the darkness\n"
quote2 = "Be Exceptional\n"

# file = open("quotes.text", "W") #It will overwrite
file = open("quotes.text", "a")
file.write(quote1)
file.write(quote2)

# Free memory resources once you have used file
file.close()

print("Data Written")