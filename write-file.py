text = "Yooooooooooooooo\nthis is some text\nHave a good one!"
text2 = "Uh oh! This text has been overwritten"
text3 = "\nHave a nice day! see ya"

# w overwritten
# a append
with open('./data/new-file.txt', 'a') as f:
    # f.write(text)
    # f.write(text2)
    f.write(text3)