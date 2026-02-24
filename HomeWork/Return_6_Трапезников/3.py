def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

lyrics = repeat_stuff("Row", 3) + " Your boat"

song = repeat_stuff("Row")
print(song)