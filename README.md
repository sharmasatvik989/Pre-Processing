# Pre-Processing

1. We will simplify many of the otherwise interesting details,    but try to emphasize many of the issues and interesting approaches to searching text.   Almost all original, source documents need to be “cleaned” (may include removing     pictures, font details, pagination, and similar.)    For this assignment ALL non ASCII information will be removed.   (Note, we will assume that docs are in English, but Spanish, French and similar    languages are not difficult to extend processing, Chinese is more difficult.) 

2. Looking for relevant documents, by doing a simple word scan is simple,    very time consuming, and usually gives poor results.    Preprocessing the original docs is important. 

3. The following are some simple methods to cleaning/processing original documents.  
 - Dealing with upper or lower case letters, usually changing to lower case.   
 - Remove punctuation (or most)  
 - Remove very common words (“stop words” such as the, or, and.) 

4. the words in the documents are extracted and indexed, with “pointers” back to   the individual relevant documents, and where found.   Then, through some sort of interface, a “search” of relevant documents can be done.   The simplest, and usually poorest result is a single word, such as “cloud”.   

5. Combinations of words, in close proximity, usually do better, such as   “cloud computing”. 
