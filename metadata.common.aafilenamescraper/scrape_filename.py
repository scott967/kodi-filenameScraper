#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import urllib.parse as urllib

import xbmc
import xbmcgui
import xbmcplugin


def get_params():
    param = []
    param_string = sys.argv[2]
    xbmc.log(f'metadata.common.filenamescraper args {param_string}')
    if len(param_string) >= 2:
        cleanedparams = param_string.replace('?','')
        if param_string[len(param_string)-1] == '/':
            param_string = param_string[0:len(param_string)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in enumerate(pairsofparams):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param

params=get_params()
action=urllib.unquote_plus(params["action"])
if action == 'find':
    title=urllib.unquote_plus(params["title"])
    liz=xbmcgui.ListItem(title, offscreen=True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=title, listitem=liz, isFolder=True)
elif action == 'getdetails':
    url=urllib.unquote_plus(params["url"])
    liz=xbmcgui.ListItem(url, offscreen=True)
    liz.setInfo('video',
        {'title': url
        })
    liz.setArt({'icon': 'DefaultVideo.png'})
    xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=liz)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
