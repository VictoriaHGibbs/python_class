def make_album(album_title, tracks=None, band_name="coheed and cambria"):
    """Return a dictionary of information about a person."""
    album = {'band': band_name.title(), 'album': album_title.title()}
    if tracks:
        album['tracks'] = tracks
    return album


discography = make_album('the second stage turbine blade')
print(discography)
print('')

discography = make_album('in keeping secrets of silent earth 3')
print(discography)
print('')

discography = make_album('good apollo i\'m burning star i.v. volume one: from fear through the eyes of madness')
print(discography)
print('')

discography = make_album('good apollo i\'m burning star i.v. volume two: no world for tomorrow', tracks=13)
print(discography)
print('')
