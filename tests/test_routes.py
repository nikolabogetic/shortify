def test_submit_retrieve(client) -> None:
    headers = {
        'Content-Type': 'text/plain'
    }

    urls = {
        'https://www.wikipedia.org/': '48VIcsBN5UX',
        'https://www.google.com/': '48VIcsBN5UY',
        'https://www.stackoverflow.com/': '48VIcsBN5UZ',
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ': '48VIcsBN5Ua'
    }

    # Post four URLs, receive short URLs, confirm short code is correct
    for key in urls:
        r = client.post('/submit', data=key, headers=headers)
        # Get short code by right-splitting the short url
        short_code = r.get_data().decode("utf-8").rsplit('/', 1)[-1] 
        assert short_code == urls[key]

    # Get full URLs (redirect) from short codes
    for key in urls:
        r = client.get(urls[key])
        assert r.location == key
        assert r.status_code == 302