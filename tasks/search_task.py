import requests

from tasks.models import Result, Keyword, Entry


def search_task(url, keywords):
    response = requests.get(url)

    content = response.text

    for keyword in keywords:
        frequency = content.count(keyword)

        if frequency != 0:
            entry = Entry.objects.get(url=url)
            key = Keyword.objects.get(entry=entry).get(key=keyword)

            result = Result(keyword=key, isAvailable=True, count=frequency)
