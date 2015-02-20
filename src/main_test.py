#!/usr/bin/env python2
from feedgen.feed import FeedGenerator


fg = FeedGenerator()
fg.load_extension('podcast')


def main():
    # required elements for RSS 2.0
    fg.title("Placeholder title")
    fg.link(href='http://placeholder.tv/testPodcast')
    fg.description('Some very descriptive descrition')

    # sets itune specific tags
    fg.podcast.itunes_author("WatchPeopleCodeTeam")
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.podcast.itunes_summary("A very descriptive summary of the podcast series")
    # add later when tuck gives image
    fg.podcast.itunes_image(None)

    # adding item
    fe = fg.add_entry()
    fe.title(raw_input("Give the podcast a title: "))
    # takes dictionary
    fe.author({'name': 'author1', 'email': 'author2'})
    # fe.link(href="http://placeholder.tv/testPodcast/episode-1")
    fe.link(href=raw_input("Link to podcast: "))
    fe.description(raw_input("Give the Podcast a description: "))

    # this is where we do final exportation of rss feed
    fg.rss_str(pretty=True)
    fg.rss_file(str(raw_input("Name output file: ").replace(".xml", "")) + ".xml")

if __name__ == '__main__':
    main()
