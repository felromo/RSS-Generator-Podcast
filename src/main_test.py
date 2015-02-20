#!/usr/bin/env python2
from feedgen.feed import FeedGenerator


fg = FeedGenerator()
fg.load_extension('podcast')


def main():
    # required elements for RSS 2.0
    fg.title("Placeholder title")
    fg.link(href='http://placeholder.tv/testPocast')
    fg.description('Some very descriptive descrition')

    # sets itune specific tags
    fg.podcast.itunes_author("WatchPeopleCodeTeam")
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.podcast.itunes_summary("A very descriptive summary of the podcast series")
    fg.podcast.itunes_image(None)

    # adding item
    fe = fg.add_entry()
    fe.title('The first released podcast')
    fe.link(href="http://placeholder.tv/testPodcast/episode-1")
    fe.description("A very accurate description, nothing vague")

    # this is where we do final exportation of rss feed
    fg.rss_str(pretty=True)
    fg.rss_file('test_run.xml')

if __name__ == '__main__':
    main()
