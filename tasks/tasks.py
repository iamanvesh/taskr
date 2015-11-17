import requests
from datetime import date
from django.core.mail import EmailMessage

from tasks.models import Result, Keyword, Entry


def search_task(url, keywords):
    response = requests.get(url)
    ressults = []

    content = response.text

    for keyword in keywords:
        frequency = content.count(keyword)

        if frequency != 0:
            entry = Entry.objects.get(url=url)
            key = Keyword.objects.get(entry=entry).get(key=keyword)

            results = Result(keyword=key, isAvailable=True, count=frequency)
            results.append({
                'url': url,
                'keyword': key,
                'isAvailable': True,
                'count': frequency
                })

    return results


def perform_search_and_send_email():
    entries = Entry.objects.all().filter(end_date__gte=date.today())

    for entry in entries:
        url = entry.url

        keywords = Keyword.objects.filter(entry=entry)
        keys = [keyword.key for keyword in keywords]

        results = filter(lambda x: x['isAvailable'], search_task(url, keys))

        if len(results) > 0:
            subject = 'Taskr found your keywords!'
            body = 'In ' + results['url'] + '\n Taskr found the following \
                        keywords' + '\n Keyword      Frequency'

            for result in results:
                body += '\n ' + results['keyword'] + '      ' + results['count']

            email = EmailMessage(subject, body, to=[entry.email])

            status = email.send()

            if status != 1:
                print 'Email not sent!'
