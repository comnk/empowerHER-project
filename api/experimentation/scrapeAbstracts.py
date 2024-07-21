# example paper:
# <td class="gsc_a_t">
#   <a href="/citations?view_op=view_citation&amp;hl=en&amp;user=x8qCMhcAAAAJ&amp;citation_for_view=x8qCMhcAAAAJ:6Zm5LS9gQ5UC" 
#       class="gsc_a_at">
#       Current advances, trends and challenges of machine learning and knowledge extraction: from machine learning to explainable AI
#   </a>
#   <div class="gs_gray">
#       A Holzinger, P Kieseberg, E Weippl, AM Tjoa</div><div class="gs_gray">Machine Learning and Knowledge Extraction: Second IFIP TC 5, TC 8/WG 8.4, 8&nbsp;…
#       <span class="gs_oph">, 2018</span>
#   </div>
# </td>

import pandas as pd
import requests, bs4
from bs4 import BeautifulSoup

def scrape_professor(scholarid):
    html_page = open("./profListings/scholar-" + scholarid + ".html", "r")
    soup = BeautifulSoup(html_page, "lxml")
    all_papers = soup.find_all('a', class_='gsc_a_at')

    for paper in all_papers:
        url = "https://scholar.google.com" + paper['href']
        # http_proxy  = "http://10.10.1.10:3128"
        # https_proxy = "https://10.10.1.11:1080"
        # ftp_proxy   = "ftp://10.10.1.10:3128"

        # proxies = { 
        #             "http"  : http_proxy, 
        #             "https" : https_proxy, 
        #             "ftp"   : ftp_proxy
        #             }
        # r = requests.get(url, allow_redirects=True, proxies=proxies)
        # open('./abstracts-' + scholarid, 'wb').write(r.content)
        print(url)

if __name__=="__main__": 
  scrape_professor("x8qCMhcAAAAJ")
