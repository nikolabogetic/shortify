def test_submit_retrieve(client) -> None:
    # Submit four URLs, get short codes, assert correctness
    headers = {
        'Content-Type': 'text/plain'
    }
    r1 = client.post('/submit', data='https://www.wikipedia.org/', headers=headers)
    assert r1.get_data().decode("utf-8") == '48VIcsBN5UX'
    
    r2 = client.post('/submit', data='https://www.google.com/', headers=headers)
    assert r2.get_data().decode("utf-8") == '48VIcsBN5UY'

    r3 = client.post('/submit', data='https://www.stackoverflow.com/', headers=headers)
    assert r3.get_data().decode("utf-8") == '48VIcsBN5UZ'

    r4 = client.post('/submit', data='https://www.youtube.com/watch?v=dQw4w9WgXcQ', headers=headers)
    assert r4.get_data().decode("utf-8") == '48VIcsBN5Ua'

    # Retrieve four URLs from corresponding short codes
    r5 = client.get('48VIcsBN5UX')
    assert r5.location == 'https://www.wikipedia.org/'
    assert r5.status_code == 302

    r6 = client.get('48VIcsBN5UY')
    assert r6.location == 'https://www.google.com/'
    assert r6.status_code == 302

    r7 = client.get('48VIcsBN5UZ')
    assert r7.location == 'https://www.stackoverflow.com/'
    assert r7.status_code == 302

    r8 = client.get('48VIcsBN5Ua')
    assert r8.location == 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    assert r8.status_code == 302
