---
YAML tags:
- copy-paste the tags obtained with the tagging app: https://github.com/huggingface/datasets-tagging
---

# Dataset Card for [Dataset Name]

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
  Training
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
As there was no pre-existing suitable dataset for Bulgarian, we had to create
one of our own. For this purpose, we collected a diverse dataset with enough samples in each category. We further wanted to make sure that our dataset will
be good for modeling credible vs. fake news, i.e., that will not degenerate into
related tasks such as topic detection (which might happen if the credible and
the fake news are about different topics), authorship attribution (which could
be the case if the fake news are written by just 1-2 authors) or source prediction
(which can occur if all credible/fake news come from just one source). Thus, we
used four Bulgarian news sources (from which we generated one training and
three separate balanced testing datasets).

  - [Source Data](#source-data)

1. We retrieved most of our credible news from Dnevnik,
4 a respected Bulgarian newspaper; we focused mostly on politics. This dataset was previously
used in research on finding opinion manipulation trolls, but its
news content fits well for our task too (5,896 credible news); 
**NOTE:** The data from this datset hasn't been added here, as it is not publicly available at the moment.
2. As our main online source of fake news, we used a website with funny news
called Ne!Novinite.
5 We crawled topics such as politics, sports, culture,
world news, horoscopes, interviews, and user-written articles (6,382 fake
news);
3. As an additional source of fake news, we used articles from the Bazikileaks6
blog. These documents are written in the form of blog-posts and the content
may be classified as “fictitious”, which is another subcategory of fake news.
The domain is politics (656 fake news);
4. And finally, we retrieved news from the bTV Lifestyle section,
7 which
contains both credible (in the bTV subsection) and fake news (in the bTV
Duplex subsection). In both subsections, the articles are about popular people and events (69 credible and 68 fake news);

We used the documents from Dnevnik and Ne!Novinite for training and testing: 70% for training and 30% for testing. We further had two additional test
sets: one of bTV vs. bTV Duplex, and one on Dnevnik vs. Bazikileaks. All test
datasets are near-perfectly balanced.

Finally, as we have already mentioned above, we used the long abstracts in
the Bulgarian DbPedia to train word2vec vectors, which we then used to build
document vectors, which we used as features for classification. (171,444 credible
samples).

  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://github.com/mhardalov/news-credibility
- **Repository:** https://github.com/mhardalov/news-credibility
- **Paper:** [In Search of Credible News](https://arxiv.org/abs/1911.08125)
- **Leaderboard:**
- **Point of Contact:** Momchil Hardalov

### Dataset Summary

[More Information Needed]

### Supported Tasks and Leaderboards

[More Information Needed]

### Languages

Bulgarian

## Dataset Structure

### Data Instances

The news articles have the following format:

```
{
    "key":"bg.btv.www:http\/article\/lifestyle\/10-bileta-za-koncerta-na-naj-uspeshnija-filmov-kompozitor-hans-cimer-vi-ochakvat.html",
    "url":"http:\/\/www.btv.bg\/article\/lifestyle\/10-bileta-za-koncerta-na-naj-uspeshnija-filmov-kompozitor-hans-cimer-vi-ochakvat.html",
    "html":"",
    "title":"10 билета за концерта на най-успешния филмов композитор, Ханс Цимер, ви очакват",
    "content":"Ханс Цимер, автор на музиката за над 120 филма, ще бъде в София на 16 май със своята група...",
    "category":"Лайфстайл",
    "publishDate":"Лайфстайл",
    "viewCount":878,
    "commentCount":0
}
```

The long abstracts have the following format:

```
{
    "abstract": "1 декември е 335-ият ден в годината според григорианския календар (336-и през високосна). Остават 30 дни до края на годината."
}
```


### Data Fields

The news articles have the following fields:

- *key* - The key of the news article (Not available for Nenovinite)
- *url* - URL to the news article
- *html* - HTML of the new article
- *title* - The title of the new article
- *content* - The content of the news article
- *category* - Category
- *publishDate* - date of publishing (For some of the datasets the field contains the category, probably an error in creation, needs to be checked)
- *viewCount* - int; view count
- *commentCount* - int; comment count (Not available for Nenovinite)


The long abstracts have only one field:

- *abstract* - Text in Bulgarian, containing credible statements.


### Data Splits

The splits from the paper are not reproduced here. 

The **training split** contains only noncredible news at this point.
Additional credible statements can be added from the abstracts.

The sources contain: 

* Nenovinite: 6382 fake news

* Bazikileaks: 656 fake news

**Note:** The main dataset with credible news, used in the paper (from the Bulgarian new website Dnevnik), is not publicly available at the moment.
When it becomes publicly available, it can be added to the training set. 
At the moment, the results from the paper cannot be reproduced with the current data,
but it still can be used as a resource for mostly noncredible news.


The **test split** contains data from the "btv" source. 
It contains *69 credible* and *68 fake news*.


[More Information Needed]

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]
