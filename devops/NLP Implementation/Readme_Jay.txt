_id                                        5c8fb128fed8a82350ec58ed
description       Racing against time to meet the Supreme Court’...
published_date                                           2019-03-18
source            http://www.bloombergquint.com/business/relianc...
text              A source in the know said RCom has paid Rs 458...
title             Reliance Communications Pays Rs 458.77 Crore T...

This is the format you are going to get

after you retrieve the data
just sort it according to the published date

After sorting this should be your format for output

published_date	Title	Description	Text
2019-03-18	1
2019-03-18	2
2019-03-18	3

Post NLP output 1

published_date	Title	Description	Text	Polarity(-1<&&<1)
2019-03-18	..	..		..	-0.4
2019-03-18	..	..		..	0.5	
2019-03-18	..	..		..	0.4

Take average of all polarity with similar dates and give it as its final output

hence output for above table for date 2019-03-18 is 
avg = (-0.4+0.5+0.4)/3
avg = 0.167

Again you'll have to process these outputs and will have to produce this as a final output which I will embedd in SVR

DateConsolidationFunction
published_date	Polarity
2019-03-18	0.167
2019-03-19	..
2019-03-20	..

MergeStockPolarity
MetaData
date	[Different Polarity Measures]	Stock close 

SVR on Dataframe from MergeStockPolarity
-------------------------------------------------

DateConsolidation Function




-------------------------------------------------
GOTCHA!!!