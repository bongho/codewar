def song_decoder(song):
    parts = song.split("WUB")
    outcome = ''
    for i in range(0,len(parts)):
        if(parts[i] != ''):
            outcome += ' ' + parts[i]
    outcome = outcome.strip()
    return outcome

def song_decoder2(song):
    return " ".join(song.replace('WUB', ' ').split())

def song_decoder3(song):
    import re
    return re.sub('(WUB)+', ' ', song).strip()

def song_decoder4(song):
    return ' '.join([a for a in song.split('WUB') if a])
