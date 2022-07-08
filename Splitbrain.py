#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install rouge


# In[2]:


from rouge import Rouge
rouge = Rouge()


# In[14]:


#1
reference1 = "For the first time, Claxton has only been preparing for a campaign over the hurdles - which could explain her leap in form. British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid. Claxton will see if her new training regime pays dividends at the European Indoors which take place on 5-6 March."
hypothesis1 = "For the first time, Claxton has only been preparing for a campaign over the hurdles - which could explain her leap in form. Claxton has won the national 60m hurdles title for the past three years but has struggled to translate her domestic success to the international stage. British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid. Claxton will see if her new training regime pays dividends at the European Indoors which take place on 5-6 March. ‘I am quite confident,’ said Claxton."
rouge.get_scores(hypothesis1 , reference1, avg=True)


# In[9]:


#2
reference2= "Jarre joins fairytale celebration French musician Jean-Michel Jarre is to perform at a concert in Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen. Later at a gala dinner, Danish supermodel Helena Christensen was named a Hans Christian Andersen ambassador. Bloom is to be formally presented with the Hans Christian Andersen Award this spring in Anderson's hometown of Odense."
hypothesis2 = "Jarre joins fairytale celebration French musician Jean-Michel Jarre is to perform at a concert in Copenhagen to mark the bicentennial of the birth of writer Hans Christian Andersen. Later at a gala dinner, Danish supermodel Helena Christensen was named a Hans Christian Andersen ambassador. Denmark's Crown Prince Frederik and Crown Princess Mary visited New York on Monday to help promote the festivities. Other stars are expected to join the line-up in the coming months, and the Danish royal family will attend. Bloom is to be formally presented with the Hans Christian Andersen Award this spring in Anderson's hometown of Odense. \"Christian Andersen's fairy tales are timeless and universal,\" said Jarre."
rouge.get_scores(hypothesis2, reference2, avg=True)


# In[11]:


#3
reference3= "a musical score for a Capra movie The creator of the contentious hit program Jerry Springer - The Opera will adapt the classic movie It's A Wonderful Life into a musical. In 1999, Mr. Thoday acquired the story's rights from Van Doren Stern's family thanks to Mr. Brown's success with Spend Spend Spend. Producer Jon Thoday is turning the 1946 film by Frank Capra starring James Stewart into a £7 million musical. The musical was unveiled to a select group of potential investors on Wednesday after a number of workshops were held in London."
hypothesis3 = "Musical treatment for Capra film The classic film It's A Wonderful Life is to be turned into a musical by the producer of the controversial hit show Jerry Springer - The Opera.Mr Thoday managed to buy the rights to the story from Van Doren Stern's family in 1999, following Mr Brown's success with Spend Spend Spend.Frank Capra's 1946 movie starring James Stewart, is being turned into a £7m musical by producer Jon Thoday.A series of workshops have been held in London, and on Wednesday a cast of singers unveiled the musical to a select group of potential investors."
rouge.get_scores(hypothesis3, reference3, avg=True)


# In[12]:


#4
reference4= "Richard and Judy choose top books The 10 authors shortlisted for a Richard and Judy book award in 2005 are hoping for a boost in sales following the success of this year's winner. The best read award, on Richard Madeley and Judy Finnigan's Channel 4 show, is part of the British Book Awards. \"It was very hard to follow last year's extremely successful list, but we think this year's books will do even better,\" said Richard and Judy executive producer Amanda Ross."
hypothesis4 = "Richard and Judy choose top books The 10 authors shortlisted for a Richard and Judy book award in 2005 are hoping for a boost in sales following the success of this year's winner. The TV couple's interest in the book world coined the term \"the Richard & Judy effect\" and created the top two best-selling paperbacks of 2004 so far. The best read award, on Richard Madeley and Judy Finnigan's Channel 4 show, is part of the British Book Awards. \"It was very hard to follow last year's extremely successful list, but we think this year's books will do even better,\" said Richard and Judy executive producer Amanda Ross. \"We were spoiled for choice and it was tough getting down to only 10 from the 301 submitted.\" The finalists for 2005 include Andrew Taylor's The American Boy and Robbie Williams' autobiography Feel."
rouge.get_scores(hypothesis4, reference4, avg=)


# In[13]:


#6
reference6= "The History Boys also won the best new comedy title at the Theatregoers' Choice Awards. The Producers was named best musical, Victoria Hamilton was best actress for Suddenly Last Summer and Festen's Rufus Norris was named best director. Diana Rigg was best actress for Suddenly Last Summer, Dame Judi Dench was best supporting actress for the RSC's All's Well That Ends Well and The History Boys' Samuel Barnett was best supporting actor."
hypothesis6 = "The History Boys also won the best new comedy title at the Theatregoers' Choice Awards. Bennett play takes theatre prizes The History Boys by Alan Bennett has been named best new play in the Critics' Circle Theatre Awards. The Producers was named best musical, Victoria Hamilton was best actress for Suddenly Last Summer and Festen's Rufus Norris was named best director. The Critics' Circle named Rebecca Lenkiewicz its most promising playwright for The Night Season, and Eddie Redmayne most promising newcomer for The Goat or, Who is Sylvia? Diana Rigg was best actress for Suddenly Last Summer, Dame Judi Dench was best supporting actress for the RSC's All's Well That Ends Well and The History Boys' Samuel Barnett was best supporting actor. Both the Critics' Circle and Whatsonstage.com Theatregoers' Choice award winners were announced on Tuesday."
rouge.get_scores(hypothesis6, reference6, avg=True)


# In[15]:


#8
reference8= "West End to honour finest shows The West End is honouring its finest stars and shows at the Evening Standard Theatre Awards in London on Monday. Meanwhile, Richard Griffiths, who plays Hector in The History Boys at the National Theatre, will battle it out for the best actor award with Douglas Hodge (Dumb Show) and Stanley Townsend (Shining City). Ferris - best known for her television roles in programmes such as The Darling Buds of May - has made the shortlist for her role in Notes on Falling Leaves, at the Royal Court Theatre."
hypothesis8 = "West End to honour finest shows The West End is honouring its finest stars and shows at the Evening Standard Theatre Awards in London on Monday. The Producers, starring Nathan Lane and Lee Evans, is up for best musical at the ceremony at the National Theatre. by Edward Albee, The Pillowman by Martin McDonagh and Alan Bennett's The History Boys are shortlisted in the best play category. Meanwhile, Richard Griffiths, who plays Hector in The History Boys at the National Theatre, will battle it out for the best actor award with Douglas Hodge (Dumb Show) and Stanley Townsend (Shining City). The Goat or Who is Sylvia? Ferris - best known for her television roles in programmes such as The Darling Buds of May - has made the shortlist for her role in Notes on Falling Leaves, at the Royal Court Theatre."
rouge.get_scores(hypothesis8, reference8, avg=True)


# In[16]:


#9
reference9= "\"Dan Brown is the best writer I've come across in the genre, but anyone who knows anything about 1st century history will see that this underlying material is laughable.\" A great deal of credible evidence proves the Biblical version of Jesus\' life was true, according to the Bishop. \"Historical research shows that they present a coherent and thoroughly credible picture of Jesus, with all sorts of incidental details that fit the time when he lived, and don't fit the world of later legend.\" Brown's book has become a publishing phenomenon, consistently topping book charts in the UK and US."
hypothesis9= "\"Dan Brown is the best writer I've come across in the genre, but anyone who knows anything about 1st century history will see that this underlying material is laughable.\" A great deal of credible evidence proves the Biblical version of Jesus\' life was true, according to the Bishop. \"Historical research shows that they present a coherent and thoroughly credible picture of Jesus, with all sorts of incidental details that fit the time when he lived, and don't fit the world of later legend.\" Brown's book has become a publishing phenomenon, consistently topping book charts in the UK and US. The Da Vinci Code has been translated into 42 languages and has spawned its own cottage industry of publications, including guides on to how to read the book, rebuttals and counter claims. Da Vinci Code is \'lousy history\' The plot of an international bestseller that thousands of readers are likely to receive as a Christmas present is \'laughable\', a clergyman has said."
rouge.get_scores(hypothesis9, reference9, avg=True)


# In[17]:


#10
reference10= "Uganda's authorities have banned the play The Vagina Monologues, due to open in the capital, Kampala this weekend. Some parliamentarians and church leaders are also siding with the Media Council, Uganda's New Vision newspaper reports. The Ugandan Media Council said the performance would not be put on as it promoted and glorified acts such as lesbianism and homosexuality. \The play promotes illegal, unnatural sexual acts, homosexuality and prostitution, it should be and is hereby banned,\" the council's ruling said."
hypothesis10 = "Uganda's authorities have banned the play The Vagina Monologues, due to open in the capital, Kampala this weekend. Some parliamentarians and church leaders are also siding with the Media Council, Uganda's New Vision newspaper reports. \"There is obviously some fear of the vagina and saying the word vagina,\" Ms Ensler told the BBC. The Ugandan Media Council said the performance would not be put on as it promoted and glorified acts such as lesbianism and homosexuality. \The play promotes illegal, unnatural sexual acts, homosexuality and prostitution, it should be and is hereby banned,\" the council's ruling said. \"I'm amazed that this country Uganda gives the impression that it is progressive and supports women\'s rights and the notions of free speech; yet when women want to share their stories the government uses the apparatus of state to shut us up.\""
rouge.get_scores(hypothesis10, reference10, avg=True)


# In[18]:


#11
reference11= "Postcards by artists including Damien Hirst and Tracey Emin have sold just hours after the opening of the Royal Academy of Arts annual Secrets sale. Money raised from the sale will go towards the RCA's Fine Art Student Award Fund which supports students with grants and bursaries. Some of the contributing artists are students or recent graduates of the Royal College of Art and other leading art colleges."
hypothesis11 = "Postcards by artists including Damien Hirst and Tracey Emin have sold just hours after the opening of the Royal Academy of Arts annual Secrets sale. The famous sale is now in its 11th year. The identity of the artist remains unknown until each work is bought and the signature is revealed on the back. Money raised from the sale will go towards the RCA's Fine Art Student Award Fund which supports students with grants and bursaries. Some of the contributing artists are students or recent graduates of the Royal College of Art and other leading art colleges. She said the people that had bought the famous name postcards had arrived early and had spent time studying each work."
rouge.get_scores(hypothesis11, reference11, avg=True)


# In[ ]:




