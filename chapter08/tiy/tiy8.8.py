def make_album(band_name, album_title):
    """Return a dictionary of information about a person."""
    album = {'band': band_name.title(), 'album': album_title.title()}
    return album

# loop time! :D
while True:
    print("\nPlease give an artist or band name:")
    print("(enter 'q' at any time to quit)")

    band_name = input("band: ")
    if band_name == 'q':
        break

    album_title = input("album: ")
    if album_title == 'q':
        break

    created_album = make_album(band_name, album_title)
    print(f"\n{created_album}")
