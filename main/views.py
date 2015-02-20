from django.shortcuts import render
# Let's use some Beautiful Soup
from bs4 import BeautifulSoup
# Python httpLib comes in handy
import httplib2


# Homepage View
def homepage(request):
    '''
        Displays the homepage and does the work
    '''
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        if request.method == 'POST':
            # grab the value from name 'url' in form
            url = request.POST['url']
            http = httplib2.Http()
            response = ''
            status_msgs = ''

            # what if can't access Wikipedia
            try:
                status, response = http.request(url)
            except:
                status_msgs = True
            extract = BeautifulSoup(response)
            # find class in Wikipedia page
            toc = extract.find_all(attrs={'class': 'mw-headline'})
            output = []
            # pile them up
            for span in toc:
                output.append(span.text)

            # then, render to template
            return render(request, 'index.html',
                          {
                            'extract': output,
                            'query': url,
                            'status': status_msgs,
                            'h2s': toc,
                            # the cue, not to display some things
                            # things in view at some points
                            'searched': True
                            },
                          )
