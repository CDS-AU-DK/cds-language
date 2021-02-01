# Syllabus Cultural Data Science - Language #

## Overview ##

The purpose of the course is to enable students to conduct systematic computational analyses of textual objects such as literature, social media, newspapers, and other kinds of linguistic artifacts.

Students will learn to understand the nature of textual corpora, and to apply statistical and machine learning methods for analysing them. The course will enable students to carry out projects within their primary subject area, and to reflect critically on others' analytical decisions. Students will also obtain the ability to present the result of their own analyses, and to visualize their results.

The course introduces basic skills in natural language processing and deep learning, specifically for the systematic analysis of text data. Students will learn how to develop research questions about natural language materials, to structure research projects to address their research questions, and to apply computational tools in their projects to provide answers to their questions.

### Academic Objectives ###

In the evaluation of the student’s performance, emphasis is placed on the extent to which the student is able to:

1. Knowledge:
    * explain central theories underlying computational approaches to the analysis of natural language data
    * reflect on the creation, composition, and limitations of text corpora
2. Skills:
    * develop a collection of texts for analysis
    * conduct large scale analyses of textual materials using computational methods
    * choose the appropriate visualization of results
3. Competences:
    * independently reflect critically on the integration of hermeneutical-conceptual and quantitative-methodological choices for an analysis of linguistic data
    * apply acquired methods and procedures to topics from the student’s core field

## Schedule ##
Each course element (1-13) is a four hour session, consisting of a 1hr lecture, 1hr coding task explanation, and 2hrs code-along session.

1. Introductions, Python, and basic data types
2. String Processing with Python
3. Basic NLP with ```spaCy```
4. Sentiment analysis
5. Named entities
6. Network analysis
7. Text classification using ```scikit-learn```
8. Topic modeling 
9. Word embeddings
10. OCR: From image to text with ```tesseract```
11. Text classification again: deep learning and neural networks
12. More deep learning for text analysis - introducing ```BERT```
13. Creating datasets

## Reading ##
Some readings are marked with `math` indicating that students with knowledge of basic calculus, probability theory, and linear algebra can benefit from this paper. Therefore, articles marked with ```math```are _supplementary_ and not compulsory. Access to some articles may require you to be on the university VPN, or can be accessed through the library website. 

#### Lesson 1 ####
- _No assigned readings_


#### Lesson 2 ####
- Hunston, S. (2002). _Corpora in Applied Linguistics_. Cambridge: Cambridge University Press, Chapters 1 + 3. Available online via AU Library.


#### Lesson 3 #### 
- Tahmasebi, N. & Hengchen, S. (2019). 'The Strengths and Pitfalls of Large-Scale Text Mining for Literary Studies', _Samlaren_, 140, 198-227. [Download](https://helda.helsinki.fi//bitstream/handle/10138/314258/Tahmasebi_Hengchen_2020_SAMLAREN.pdf?sequence=1)


#### Lesson 4 ####
- Heuser, R., Moretti, F., & Steiner, E. (2016). 'The Emotions of London', _Literary Lab Pamphlet_, 13. [Download](https://litlab.stanford.edu/LiteraryLabPamphlet13.pdf)
- Kim, E. & Klinger, R. (2019). 'A Survey on Sentiment and Emotion Analysis for Computational Literary Studies'. In _Zeitschrift für digitale Geisteswissenschaften_. DOI: [10.17175/2019_008](http://www.zfdg.de/2019_008)


#### Lesson 5 ####
- Ehrmann, M., Nouvel, D. & Rosset, S. (2016). 'Named Entities Resources - Overview and Outlook'. In N. Calzolari, K. Choukri, T. Declerck, M. Grobelnik, B. Maegaard, J. Mariani, A. Moreno, J. Odijk, and S. Piperidis (eds.), _Proceedings of the 10th International Conference on Language Resources and Evaluation_, 3349–3356. [Download](https://www.aclweb.org/anthology/L16-1534)
- Wilkens, M. & Evans, E. (2018). 'Nation, Ethnicity, and the Geography of British Fiction, 1880-1940', _Journal of Cultural Analytics_. DOI: [10.22148/16.024](https://culturalanalytics.org/article/11037-nation-ethnicity-and-the-geography-of-british-fiction-1880-1940)


#### Lesson 6 ####
- Ahnert, R. & Ahnert, S. (2015). 'Protestant Letter Writing Networks in the Reign of Mary I: A Quantitative Approach', _English Literary History_, 82(1), 1-33. DOI: [10.1353/elh.2015.0000](https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/10170/ProtestantLetterNetworks82.1.ahnert.pdf?sequence=6&isAllowed=y)
- Cordell, R. (2015). 'Reprinting, Circulation, and the Network Author in Antebellum Newspapers', _American Literary History_, 27(3), 417-445. DOI: [10.1093/alh/ajv028](https://academic.oup.com/alh/article-abstract/27/3/417/85989)


#### Lesson 7 ####
- So, R.J. & Roland, E. (2020). 'Race and Distant Reading', _Publication of the Modern Language Association (PMLA), special issue on "Varieties of Digital Humanities_, 135(1), 59-73. [Download](https://186a12ba-ba8b-43dc-a7e9-e52f0db4a597.filesusr.com/ugd/175024_f4e33b1f05924be58fcfbc8e0542d475.pdf)


#### Lesson 8 ####
- Stine, Z., Deitrick, J., & Agarwal, N. (2020). 'Comparative Religion, Topic Models, and Conceptualization: Towards the Characterization of Structural Relationship between Online Religious Discourses', _CHR2020: Workshop on Computational Humanities Research_. [Download](http://ceur-ws.org/Vol-2723/long47.pdf)
- Blei, D.M, Ng, A.Y., Jordan, M.I. (2003). 'Latent Direchlet Allocation', _Journal of Machine Learning Research_, 3, 993-1022. DOI: [10.5555/944919.944937](https://dl.acm.org/doi/10.5555/944919.944937) ```maths```
- Viola, L. & Verheul, J. (2019). 'Mining ethnicity: Discourse-driven topic modelling of immigrant discourses in the USA, 1898–1920', _Digital Scholarship in the Humanities_, 35(4), 921-943. DOI: [10.1093/llc/fqz068](https://academic.oup.com/dsh/article/35/4/921/5601610)


#### Lesson 9 ####
- Garg, N., Schiebinger, L., Jurafsky, D. & Zou, J. (2018). 'Word embeddings quantify 100 years of gender and ethnic stereotypes', _PNAS_, 16, E3635-E3644. DOI: [10.1073/pnas.1720347115](https://www.pnas.org/content/115/16/E3635)
- Kozlowskia, A.C., Taddyb, M., Evansa, J.A. (2019). 'The Geometry of Culture: Analyzing the Meanings of Class Through Word Embeddings', _American Sociological Review_. DOI: [10.1177/0003122419877135](https://journals.sagepub.com/doi/full/10.1177/0003122419877135)
- Mikolov et al (2013). 'Efficient Estimation of Word Representations in Vector Space', [arXiv:1301.3781](https://arxiv.org/abs/1301.3781?source=post_page---------------------------) [cs.CL]```maths```


#### Lesson 10 ####
- Hill, M.J., & Hengchen, S. (2019). 'Quantifying the impact of dirty OCR on historical text analysis: Eighteenth Century Collections Online as a case study',_Digital Scholarship in the Humanities_, 34(4), 825-843. DOI: [10.1093/llc/fqz024](https://academic.oup.com/dsh/article-abstract/34/4/825/5476122)
- Ströbel et al (2019). 'How Much Data Do You Need? About the Creation of a Ground Truth for Black Letter and the Effectiveness of Neural OCR', _Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020)_, 3551–3559. [Download](https://www.aclweb.org/anthology/2020.lrec-1.436.pdf)


#### Lesson 11 ####
- Blanke, T., Bryant, M., & Hedges, M. (2020). 'Understanding memories of the Holocaust—A new approach to neural networks in the digital humanities', _Digital Scholarship in the Humanities_, 35(1), 17-33. DOI: [10.1093/llc/fqy082](https://www.google.com/search?client=firefox-b-d&q=10.1093%2Fllc%2Ffqy082)


#### Lesson 12 ####
- Devlin et al. (2017). 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', [arXiv:1810.04805](https://arxiv.org/abs/1810.04805) [cs.CL] ```maths```
- Underwoord, T. (2019). 'Do humanists need BERT?", [blog post.](https://tedunderwood.com/2019/07/15/do-humanists-need-bert/)
- Vaswani et al (2017). 'Attention is all you need', [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) [cs.CL]```maths```

#### Lesson 13 ####
_No assigned readings_


### Additional Resources - Textbooks ###
- Goldberg, N. (2017). _Neural Network Methods for Natural Language Processing_. New York: Morgan & Claypool Publishers. ```maths```
- Jurafsky, D. & Martin, J.H. (2021). _Speech and Language Processing_, 3rd edition online pre-print. [Access](https://web.stanford.edu/~jurafsky/slp3/)
- VanderPlas, J. (2016). _Python Data Science Handbook_. [Access](https://jakevdp.github.io/PythonDataScienceHandbook/)
