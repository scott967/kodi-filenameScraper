#!/usr/bin/env python3
"""Python scraper for music videos.
Kodi scraper for musicvideos.  This scraper will parse a filename for
title - artistname and add the file item to the video library.  See  README for
more info.

This scraper is an extendsion/modification of metadata.common.filenamescraper
Copyright (c) 2019 Sebastian Plesch for original contnet
Copyright (c) 2023 Scott Smart for extensions and modifications

Licensed under MIT license.  See LICENSE for details.

Returns:
    New musicvideos are added to the videos database.  See Kodi debug log for
failed items.
"""

import secrets
import sys
import urllib.parse as urllib

import xbmc
import xbmcgui
import xbmcplugin

def get_params() -> dict:
    """gets scrape query string as dict from sys.argv

    Returns:
        dict: The action and parameters passed to scraper
    """
    param_string = sys.argv[2][1:]
    if param_string:
        return dict(urllib.parse_qsl(param_string))
    return {}

params=get_params()
if not params:
    xbmc.log('metadata.musicvideos.tafilenamescraper -- Unable to parse query',
             xbmc.LOGINFO)
action=params.get('action')
if action == 'find':
    query_title = params.get('title')
    title_artist = query_title.rsplit(' - ', 1)
    if len(title_artist) != 2:
        xbmc.log('metadata.musicvideos.tafilenamescraper -- Unable to extract '
                 f'Title and/or Artist from {query_title}', xbmc.LOGINFO)
        sys.exit()
    liz = xbmcgui.ListItem(title_artist[0], title_artist[1], offscreen=True)
    liz.setArt({'thumb': 'DefaultVideo.png'})
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),
                                url=query_title,
                                listitem=liz,
                                isFolder=True)
    xbmc.log('metadata.musicvideos.tafilenamescraper -- Added file item to '
            f'library: {query_title}', xbmc.LOGDEBUG)
elif action == 'getdetails':
    query_title = params.get('url')
    title_artist = query_title.rsplit(' - ', 1)
    liz = xbmcgui.ListItem(title_artist[0], title_artist[1], offscreen=True)
    info_tag:xbmc.InfoTagVideo = liz.getVideoInfoTag()
    info_tag.setTitle(title_artist[0])
    info_tag.setUniqueID(f'{secrets.randbelow(999999):06d}', 'tascrape')
    info_tag.setArtists(title_artist[1].split('; '))
    liz.setArt({'icon': 'DefaultVideo.png'})
    xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]),
                              succeeded=True,
                              listitem=liz)
    xbmc.log(f'metadata.musicvideos.tafilenamescraper -- Added title {title_artist[0]}'
             f' / artist {title_artist[1].split(" ; ")} details ', xbmc.LOGDEBUG)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
