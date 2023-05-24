# kodi-filenameScraper
A trivial, python-based filename-only scraper for Kodi (Kodi plugin)

20 JUL 22 Updated for matrix / python 3

24 MAY 23 Extended/modified as a title - artist filename parser for Kodi
musicvideos.

Usage:

Compatible with Kodi 20+

Musicvideo file names should be composed in the form <Title> - <Artist>
where the separator is u\0020 u\002F u\0020 .   File names are parsed from the
RIGHT so ANYTHING preceeding the right-most ' - ' will be treated as a title.

Multiple artist names may be concatonated in the filename using '; ' as an
artist seperator.
