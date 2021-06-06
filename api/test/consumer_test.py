
from ..app import strip_down, search_by_terms

def test_strip_down_returns_required_fields():
    example_item = {
        "etag": "pFle-S-zK0fyO3zXTsRpBlwoUNA",
        "id": {
            "kind": "youtube#video",
            "videoId": "LIIDh-qI9oI"
        },
        "kind": "youtube#searchResult",
        "snippet": {
            "channelId": "UCF_fDSgPpBQuh1MsUTgIARQ",
            "channelTitle": "TheWeekndVEVO",
            "description": "Production Company: Blinkink @blink_ink Director: Jack Brown - @jbanimation Executive Producer: Josef Byrne @philipphlop Producers: Matt Marsh, Dom ...",
            "liveBroadcastContent": "none",
            "publishTime": "2021-04-23T04:00:06Z",
            "publishedAt": "2021-04-23T04:00:06Z",
            "thumbnails": {
                "default": {
                    "height": 90,
                    "url": "https://i.ytimg.com/vi/LIIDh-qI9oI/default.jpg",
                    "width": 120
                },
                "high": {
                    "height": 360,
                    "url": "https://i.ytimg.com/vi/LIIDh-qI9oI/hqdefault.jpg",
                    "width": 480
                },
                "medium": {
                    "height": 180,
                    "url": "https://i.ytimg.com/vi/LIIDh-qI9oI/mqdefault.jpg",
                    "width": 320
                }
            },
            "title": "The Weeknd &amp; Ariana Grande - Save Your Tears (Remix) (Official Video)"
        }
    }

    new_item = strip_down(example_item)

    assert 'id' in new_item
    assert 'title' in new_item
    assert 'description' in new_item
    assert 'url' in new_item
    assert 'thumbnail' in new_item
    assert 'url' in new_item['thumbnail']
    assert 'width' in new_item['thumbnail']
    assert 'height' in new_item['thumbnail']
    
def test_search_by_terms_returns_a_list():
    result = search_by_terms("hello world")
    assert type(result) == list