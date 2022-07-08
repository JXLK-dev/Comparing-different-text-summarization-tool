#!/usr/bin/env python
# coding: utf-8

# In[3]:


from rouge import Rouge
rouge = Rouge()


# In[4]:


#1
reference1 = "For the first time, Claxton has solely been training for a race over hurdles, which would account for her dramatic improvement in form. For the previous three years, Claxton has won the national 60-meter hurdles championship, but she has had trouble carrying her home success to the international level. The European Indoor Championships will be held in Madrid next month, and British hurdler Sarah Claxton is optimistic she can bring home her first major medal. Claxton will test the effectiveness of her new training regimen at the European Indoors, which are scheduled for March 5 and 6. "
hypothesis1 = "For the first time, Claxton has only been preparing for a campaign over the hurdles - which could explain her leap in form. Claxton has won the national 60m hurdles title for the past three years but has struggled to translate her domestic success to the international stage. British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid. Claxton will see if her new training regime pays dividends at the European Indoors which take place on 5-6 March. \‘I am quite confident,\’ said Claxton."
rouge.get_scores(hypothesis1 , reference1, avg=True)


# In[5]:


#2
reference2= "Jarre participates in the fairytale festival The bicentennial of author Hans Christian Andersen's birth will be celebrated in Copenhagen with a concert featuring French musician Jean-Michel Jarre. Helena Christensen, a Danish supermodel, was later made a Hans Christian Andersen ambassador during a gala banquet. Crown Prince Frederik and Crown Princess Mary of Denmark paid a visit to New York on Monday to support the celebrations. The Danish royal family will attend, and further celebrities are anticipated to be added to the lineup in the coming months. This April in Anderson's hometown of Odense, Bloom will receive the Hans Christian Andersen Award in person. Fairy stories of Christian Andersen are timeless and accessible, according to Jarre"
hypothesis2 = "Jarre joins fairytale celebration French musician Jean-Michel Jarre is to perform at a concert in Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen. Later at a gala dinner, Danish supermodel Helena Christensen was named a Hans Christian Andersen ambassador. Denmark's Crown Prince Frederik and Crown Princess Mary visited New York on Monday to help promote the festivities. Other stars are expected to join the line-up in the coming months, and the Danish royal family will attend. Bloom is to be formally presented with the Hans Christian Andersen Award this spring in Anderson's hometown of Odense. \"Christian Andersen's fairy tales are timeless and universal,\" said Jarre."
rouge.get_scores(hypothesis2, reference2, avg=True)


# In[6]:


#3
reference3= "a musical score for a Capra movie The creator of the contentious smash program Jerry Springer - The Opera will adapt the classic movie It's A Wonderful Life into a musical. In 1999, Mr. Thoday acquired the story's rights from Van Doren Stern's family thanks to Mr. Brown's success with Spend Spend Spend. James Stewart-starring 1946 film by Frank Capra is being remade as a £7 million musical by producer Jon Thoday. A cast of singers presented the musical to a small group of possible financiers on Wednesday after a series of workshops were performed in London."
hypothesis3 = "Musical treatment for Capra film The classic film It's A Wonderful Life is to be turned into a musical by the producer of the controversial hit show Jerry Springer - The Opera.Mr Thoday managed to buy the rights to the story from Van Doren Stern's family in 1999, following Mr Brown's success with Spend Spend Spend.Frank Capra's 1946 movie starring James Stewart, is being turned into a £7m musical by producer Jon Thoday.A series of workshops have been held in London, and on Wednesday a cast of singers unveiled the musical to a select group of potential investors."
rouge.get_scores(hypothesis3, reference3, avg=True)


# In[7]:


#4
reference4= "Judy and Richard pick the best novels Following the popularity of this year's winner, the 10 authors who were shortlisted for a Richard and Judy book award in 2005 are hoping that their sales will increase. The TV couple's fascination with books gave rise to the phrase \"the Richard & Judy effect\" and produced the top two paperback bestsellers of 2004 to date. The British Book Awards include the best read award, which is presented on the Richard Madeley and Judy Finnigan show on Channel 4. The Richard and Judy executive producer Amanda Ross remarked, \"It was quite difficult to follow last year's tremendously successful list, but we anticipate this year's books will do even better.\" \"We had a lot of options, so it was difficult to choose just 10 from the 301.\""
hypothesis4 = "Richard and Judy choose top books The 10 authors shortlisted for a Richard and Judy book award in 2005 are hoping for a boost in sales following the success of this year's winner. The TV couple's interest in the book world coined the term \"the Richard & Judy effect\" and created the top two best-selling paperbacks of 2004 so far. The best read award, on Richard Madeley and Judy Finnigan's Channel 4 show, is part of the British Book Awards. \"It was very hard to follow last year's extremely successful list, but we think this year's books will do even better,\" said Richard and Judy executive producer Amanda Ross. \"We were spoiled for choice and it was tough getting down to only 10 from the 301 submitted.\" The finalists for 2005 include Andrew Taylor's The American Boy and Robbie Williams' autobiography Feel."
rouge.get_scores(hypothesis4, reference4, avg=)


# In[8]:


#6
reference6= "Judy and Richard pick the best novels Following the popularity of this year's winner, the 10 authors who were shortlisted for a Richard and Judy book award in 2005 are hoping that their sales will increase. The TV couple's fascination with books gave rise to the phrase \"the Richard & Judy effect\" and produced the top two paperback bestsellers of 2004 to date. The British Book Awards include the best read award, which is presented on the Richard Madeley and Judy Finnigan show on Channel 4. The Richard and Judy executive producer Amanda Ross remarked, \"It was quite difficult to follow last year's tremendously successful list, but we anticipate this year's books will do even better." "We had a lot of options, so it was difficult to choose just 10 from the 301.\""
hypothesis6 = "The History Boys also won the best new comedy title at the Theatregoers' Choice Awards. Bennett play takes theatre prizes The History Boys by Alan Bennett has been named best new play in the Critics' Circle Theatre Awards. The Producers was named best musical, Victoria Hamilton was best actress for Suddenly Last Summer and Festen's Rufus Norris was named best director. The Critics' Circle named Rebecca Lenkiewicz its most promising playwright for The Night Season, and Eddie Redmayne most promising newcomer for The Goat or, Who is Sylvia? Diana Rigg was best actress for Suddenly Last Summer, Dame Judi Dench was best supporting actress for the RSC's All's Well That Ends Well and The History Boys' Samuel Barnett was best supporting actor. Both the Critics' Circle and Whatsonstage.com Theatregoers' Choice award winners were announced on Tuesday."
rouge.get_scores(hypothesis6, reference6, avg=True)


# In[9]:


#8
reference8= "West End to honor the best productions At the Evening Standard Theatre Awards in London on Monday, the West End will honor its top performers and productions. The Producers, starring Lee Evans and Nathan Lane, is competing for best musical at the National Theatre awards. The History Boys by Alan Bennett, The Pillowman by Martin McDonagh, and by Edward Albee are on the shortlist for best play. Meanwhile, Stanley Townsend, Douglas Hodge, and Richard Griffiths, who portrays Hector in The History Boys at the National Theatre, will compete for the best actor prize (Shining City). Who is Sylvia, or The Goat? Ferris, who is most known for her television roles in shows like The Darling Buds of May, has achieved success in the"
hypothesis8 = "West End to honour finest shows The West End is honouring its finest stars and shows at the Evening Standard Theatre Awards in London on Monday. The Producers, starring Nathan Lane and Lee Evans, is up for best musical at the ceremony at the National Theatre. by Edward Albee, The Pillowman by Martin McDonagh and Alan Bennett's The History Boys are shortlisted in the best play category. Meanwhile, Richard Griffiths, who plays Hector in The History Boys at the National Theatre, will battle it out for the best actor award with Douglas Hodge (Dumb Show) and Stanley Townsend (Shining City). The Goat or Who is Sylvia? Ferris - best known for her television roles in programmes such as The Darling Buds of May - has made the shortlist for her role in Notes on Falling Leaves, at the Royal Court Theatre."
rouge.get_scores(hypothesis8, reference8, avg=True)


# In[10]:


#9
reference9= "Dan Brown is the best author of this genre I've come across, but anyone who is familiar with the history of the first century would recognize how ridiculous the underlying ideas are. \"Historical research shows that they present a coherent and thoroughly credible picture of Jesus, with all sorts of incidental details that fit the time when he lived, and don't fit the world of later legend,\" said the Bishop. \"There is a great deal of credible evidence that the Biblical version of Jesus' life was true.\" Brown's book has become a publishing phenomenon and continues to be at the top of both the US and UK book lists. The Da Vinci Code has been translated into 42 different languages and has inspired a cottage publishing industry, including how-to guides."
hypothesis9= "\"Dan Brown is the best writer I've come across in the genre, but anyone who knows anything about 1st century history will see that this underlying material is laughable.\" A great deal of credible evidence proves the Biblical version of Jesus\' life was true, according to the Bishop. \"Historical research shows that they present a coherent and thoroughly credible picture of Jesus, with all sorts of incidental details that fit the time when he lived, and don't fit the world of later legend.\" Brown's book has become a publishing phenomenon, consistently topping book charts in the UK and US. The Da Vinci Code has been translated into 42 languages and has spawned its own cottage industry of publications, including guides on to how to read the book, rebuttals and counter claims. Da Vinci Code is \'lousy history\' The plot of an international bestseller that thousands of readers are likely to receive as a Christmas present is \'laughable\', a clergyman has said."
rouge.get_scores(hypothesis9, reference9, avg=True)


# In[11]:


#10
reference10= "The Vagina Monologues, a play set to debut this weekend in Kampala, the country's capital, has been outlawed by the Ugandan government. According to Uganda's New Vision newspaper, a few lawmakers and religious authorities are also supporting the Media Council. According to Ms. Ensler, \"there is certainly some fear of the vagina and speaking the term vagina.\" The show won't be presented, according to the Ugandan Media Council, because it glorifies and promotes homosexuality and lesbianism. The show should be and is hereby banned because it encourages homosexuality, prostitution, and illegal, unnatural sexual behaviors \"The council's decision said. \"I find it amazing that Uganda presents itself as progressive and promotes women's rights and the idea of free expression, but when women want to"
hypothesis10 = "Uganda's authorities have banned the play The Vagina Monologues, due to open in the capital, Kampala this weekend. Some parliamentarians and church leaders are also siding with the Media Council, Uganda's New Vision newspaper reports. \"There is obviously some fear of the vagina and saying the word vagina,\" Ms Ensler told the BBC. The Ugandan Media Council said the performance would not be put on as it promoted and glorified acts such as lesbianism and homosexuality. \The play promotes illegal, unnatural sexual acts, homosexuality and prostitution, it should be and is hereby banned,\" the council's ruling said. \"I'm amazed that this country Uganda gives the impression that it is progressive and supports women\'s rights and the notions of free speech; yet when women want to share their stories the government uses the apparatus of state to shut us up.\""
rouge.get_scores(hypothesis10, reference10, avg=True)


# In[12]:


#11
reference11= "Just hours after the Royal Academy of Arts annual Secrets sale began, postcards by artists including Damien Hirst and Tracey Emin went on sale. This renowned sale is in its eleventh year. Until a piece is purchased and the artist's signature is seen on the back, no one knows who the artist is. The RCA's Fine Art Student Award Fund, which provides grants and bursaries to students, will receive the proceeds from the sale. Some of the contributing artists are currently enrolled at the Royal College of Art or have recently graduated from one of the nation's top art schools. She claimed that the purchasers of the renowned name postcards had arrived early and had taken their time looking over each piece."
hypothesis11 = "Postcards by artists including Damien Hirst and Tracey Emin have sold just hours after the opening of the Royal Academy of Arts annual Secrets sale. The famous sale is now in its 11th year. The identity of the artist remains unknown until each work is bought and the signature is revealed on the back. Money raised from the sale will go towards the RCA's Fine Art Student Award Fund which supports students with grants and bursaries. Some of the contributing artists are students or recent graduates of the Royal College of Art and other leading art colleges. She said the people that had bought the famous name postcards had arrived early and had spent time studying each work."
rouge.get_scores(hypothesis11, reference11, avg=True)


# In[ ]:




