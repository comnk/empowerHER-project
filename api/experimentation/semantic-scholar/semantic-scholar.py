from semanticscholar import SemanticScholar
import json

authors = {}
sch = SemanticScholar()
results = sch.search_paper('gender inequality computer science', fields=['title', 'authors', 'year'])
# get list of authors who have published gender inequality related papers in computer science
# searching first 100 papers
for paper in results.items: 
    for author in paper.authors:
        if author.authorId in authors:
            authors[author.authorId]['theme paper(s)'].append(paper.title)
        else:
            authors[author.authorId] = {
                'name': author.name,
                'theme paper(s)': [paper.title],
            }

# get information per author
count = 0
for authorid in authors.keys():
    author = sch.get_author(int(authorid))
    authors[authorid]['paper count'] = author.paperCount
    authors[authorid]['citation count'] = author.citationCount
    authors[authorid]['h-index'] = author.hIndex

    papers = {}
    for paper in author.papers:
        # print(paper.s2FieldsOfStudy)
        papers[paper.paperId] = {
            "title": paper.title,
            "publication date": paper.publicationDate,
            # "citation count": paper.citationCount,
            "influential citation count": paper.influentialCitationCount,
            # "venue": paper.venue,
            # "abstract": paper.abstract,
            "fieldsOfStudy": paper.s2FieldsOfStudy # list
        }
    # authors[authorid]['papers'] = papers

    top_3_recent = []
    recent_papers = {k: v for k, v in papers.items() if v['publication date'] is not None}
    recent_papers = dict(sorted(recent_papers.items(), key=lambda x: x[1]['publication date'], reverse=True)[:3])
    for paperid in recent_papers.keys():
        top_3_recent.append((recent_papers[paperid]['title'], str(recent_papers[paperid]['publication date'].year)))
    authors[authorid]['top 3 recent'] = top_3_recent # (title, year)

    top_3_citation = []
    top_papers = {k: v for k, v in papers.items() if v['influential citation count'] is not None}
    top_papers = dict(sorted(top_papers.items(), key=lambda x: x[1]['influential citation count'], reverse=True)[:3])
    for paperid in top_papers.keys():
        top_3_citation.append((top_papers[paperid]['title'], str(top_papers[paperid]['influential citation count'])))
    authors[authorid]['top 3 citation'] = top_3_citation # (title, influential citation count)

    count += 1
    print("count", count, "out of", len(authors))
    if count >= 20:
        break

hindex_authors = {k: v for k, v in authors.items() if 'h-index' in v}
sorted_authors = dict(sorted(hindex_authors.items(), key=lambda x: x[1]['h-index'], reverse=True))
# print(sorted_authors)

json_object = json.dumps(sorted_authors, indent = 4) 
with open("./semantic-scholar-details-20.json", "w") as outfile: 
    outfile.write(json_object)