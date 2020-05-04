#pip3 downloads required
#pip3 install python-vlc
#pip3 install pafy
#pip3 install youtube-dl

import pafy
import urllib.request
import urllib.parse
import os
import vlc
import re

def playMedia(search):

    query_string = urllib.parse.urlencode({"search_query" : search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

    #the URL must be formatted: https://www.youtube.com/watch?v=<video id>
    url = "https://www.youtube.com/watch?v=" + search_results[0]
    video = pafy.new(url)
    best = video.getbest()
    playurl = best.url
    ins = vlc.Instance()
    player = ins.media_player_new()


    code = urllib.request.urlopen(url).getcode()
    if str(code).startswith('2') or str(code).startswith('3'):
        print('Stream is working')
    else:
        print('Stream is dead')

    Media = ins.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()



    good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
    while str(player.get_state()) in good_states:
        print('Stream is working. Current state = {}'.format(player.get_state()))

    print('Stream is not working. Current state = {}'.format(player.get_state()))
    player.stop()
    
def stopMedia():
    player.stop()