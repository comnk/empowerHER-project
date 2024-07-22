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

import json
from multiprocessing.pool import ThreadPool as Pool
from multiprocessing import TimeoutError
from operator import itemgetter
import os
import pandas as pd
import requests, bs4
from bs4 import BeautifulSoup
from semanticscholar import SemanticScholar

def scrape_professor(scholarid):
    print("Scraping professor: " + scholarid)
    html_page = open("./profListings/scholar-" + scholarid + ".html", "r")
    soup = BeautifulSoup(html_page, "lxml")
    all_papers = soup.find_all('a', class_='gsc_a_at')

    file = open("./paper-text/papers-" + scholarid + ".txt", "w")
    file.write("Paper Name, Citations, Publication Date\n")
    yearSortedFile = open("./paper-text/yearSorted/yearSortedPapers-" + scholarid + ".txt", "w")
    yearSortedFile.write("Paper Name, Citations, Publication Date\n")
    
    paperList = []
    
    for ind, paper in enumerate(all_papers):
        print(f"Doing paper {paper.string} of {scholarid} | {ind}/{len(all_papers)}")
        # url = "https://scholar.google.com" + paper['href']
        name = paper.get_text()
        # print(name)

        
        sch = SemanticScholar(api_key=os.getenv("SCHOLAR_KEY"))
        results = sch.search_paper(name)
        
        abstract = None 
        citations = -1
        date = ''
        if len(results) > 0:
          abstract = results[0].abstract
          citations = results[0].citationCount
          date = str(results[0].publicationDate)
          # print(str(type(date)) + " | " + str(date))
          # print(citations)
        
        paperList.append({"name": name, "abstract": abstract, "citations": citations, "pubdate": date})
      
      
    sortedPaperList = sorted(paperList, key=itemgetter('citations'), reverse=True)
    sortedPaperListYear = sorted(paperList, key=itemgetter('pubdate'), reverse=True)

    print(f"SORTED PAPER LIST FOR {scholarid}")   
    print(sortedPaperList)
    
    for ind, paper in enumerate(sortedPaperList):
        print(f"Writing paper {paper['name']} of {scholarid} | {ind}/{len(sortedPaperList)}")       
        file.write(paper["name"] + ", " + str(paper["citations"]) + ", " + paper["pubdate"] + "\n")
        
        # CODE FOR ADDING ABSTRACT, NEED TO FORMAT
        # if paper["abstract"] != None:
        #   file.write(paper["abstract"] + "\n")
          
          
        file.write("\n")
        # file.flush() # INCLUDE ONLY FOR TESTING
        # print(f"wrote to file {name} and {abstract}")
        
    for ind, paper in enumerate(sortedPaperListYear):
        print(f"Writing paper {paper['name']} of {scholarid} | {ind}/{len(sortedPaperList)}")       

        yearSortedFile.write(paper["name"] + ", " + str(paper["citations"]) + ", " + paper["pubdate"] + "\n")
        
        # CODE FOR ADDING ABSTRACT, NEED TO FORMAT
        # if paper["abstract"] != None:
        #   file.write(paper["abstract"] + "\n")
          
          
        yearSortedFile.write("\n")
        # file.flush() # INCLUDE ONLY FOR TESTING
        # print(f"wrote to file {name} and {abstract}")
          

    file.write("DONE")
    file.close()

if __name__=="__main__": 
  # Number of parallel threads
  pool_size = 25  # your "parallelness"
  pool = Pool(pool_size)
  processes = []
  results = []
  
  # r = requests.post(
  #   'https://api.semanticscholar.org/graph/v1/paper/batch',
  #   params={'fields': 'referenceCount,citationCount,title'},
  #   json={"ids": ["649def34f8be52c8b66281af98ae884c09aef38b", "ARXIV:2106.15928"]}
  # )
  # print(json.dumps(r.json(), indent=2))
  
  # print("====================================")
  
  directory = os.fsencode('profListings')
  for ind, file in enumerate(os.listdir(directory)):
    if (".html" not in os.fsdecode(file)) or ("scholar-" not in os.fsdecode(file)):
        continue
    filename = os.fsdecode(file)
    profID = filename[8:-5] # remove scholar- and .html from filename
    
    # print(profID)
    processes.append((profID, pool.apply_async(scrape_professor, (profID,))))
    print(f"Appending {ind} / {len(os.listdir(directory))} to pool")
    
  for ind, (profID, process) in enumerate(processes):
    try:
      # print(f"Waiting for {profID} process get")
      print(f"Appending {ind} / {len(processes)} to results")
      results.append(process.get(timeout = 600))
    except TimeoutError:
      print(f"Timeout with {profID}")
      pass
    except Exception as e:
      print(f"Error with {profID} | {e}")
      pass
    
  pool.close()
  pool.join()



