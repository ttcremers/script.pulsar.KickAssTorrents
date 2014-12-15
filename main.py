from pulsar import provider
# Game of Thrones 720p OR 1080p -complete category:tv seeds:10 lang_id:2 season:2 episode:4

def search(query):
	resp = provider.GET("http://kickass.so/usearch", params={
		"q": query,
	})
	return provider.extract_magnets(resp.data)

def search_episode(episode):
	return search("%(title)s S%(season)02dE%(episode)02d category:tv lang_id:2 -complete 720p OR 1080p" % episode)

def search_movie(movie):
	return search("%(title)s %(year)d" % movie)

provider.register(search, search_movie, search_episode)
