
from flask import Flask, render_template, redirect , request
from collections import defaultdict
from operator import itemgetter


def searching(filewords,filename,filetarget):
    filewords = filewords.strip().lower().replace(",","").replace("_","").replace(".","").replace("\"","").replace("'","").replace("-","").replace("!","").replace(";","").replace(")","").replace("(","").replace("-","").replace("?","").replace("/","").replace("*","").replace(":","").split(" ")
    
    f = open(filename+".txt","w")
    f.write(str(filewords))
    f.close()
    count =0
    for line in filewords:
        if line == filetarget:
            count = count +1
    

    file = open(filename+".txt","rt")
  
    data = file.read()
    words = data.split()
    
    count2= len(words)
    file.close()

    fileName = ["AliceCleaner.txt", "second.txt","third.txt","Fourth.txt","Fifth.txt","sixth.txt"]
    fileName_w = ["one_a.txt", "second_b.txt","third_a.txt","Fourth_a.txt","Fifth_a.txt","sixth_a.txt"]
    arr = [open(fileName[0],"r",encoding="UTF= 8"),
            open(fileName[1],"r",encoding="UTF=8"),
            open(fileName[2],"r",encoding="UTF=8"),
            open(fileName[3],"r",encoding="UTF=8"),
            open(fileName[4],"r",encoding="UTF=8"),
            open(fileName[5],"r",encoding="UTF=8")
        ]

    arr_w = [open(fileName_w[0],"w"),
            open(fileName_w[1],"w"),
            open(fileName_w[2],"w"),
            open(fileName_w[3],"w"),
            open(fileName_w[4],"w"),
            open(fileName_w[5],"w")
        ]
    stopwords = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","so","than","too","very","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","would","should","could","ought","i'm","you're","he's","she's","it's","we're","they're","i've","you've","we've","they've","i'd","you'd","he'd","she'd","we'd","they'd","i'll","you'll","he'll","she'll","we'll","they'll","isn't","aren't","wasn't","weren't","hasn't","haven't","hadn't","doesn't","don't","didn't","won't","wouldn't","shan't","shouldn't","can't","cannot","couldn't","mustn't","let's","that's","who's","what's","here's","there's","when's","where's","why's","how's","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same"]

    print(" CLeaning all the Document\n")

    i = 0
    for files in arr:
        for line in files:
            line = line.strip().lower().replace(",","").replace("_","").replace(".","").replace("\"","").replace("'","").replace("-","").replace("!","").replace(";","").replace(")","").replace("(","").replace("-","").replace("?","").replace("/","").replace("*","").replace(":","").split(" ")
            for word in stopwords:
                try:    
                    line.remove(word)
                except ValueError:
                    pass
            line = " ".join([x for x in line])
            arr_w[i].write(line+"\n")
            

        #text = files.read()
        #text = text.lower().replace(",","").replace("_","").replace(".","").replace("\"","").replace("'","").replace("-","").replace("!","").replace(";","").replace(")","").replace("(","").replace("-","").replace("?","").replace("/","").replace("*","").replace(":","")
        
        arr_w[i].close()
        files.close()
        #print(" Lines where the word is found \n")
        i+=1

    arr_w = [open(fileName_w[0],"r",encoding="UTF=8"),
            open(fileName_w[1],"r",encoding="UTF=8"),
            open(fileName_w[2],"r",encoding="UTF=8"),
            open(fileName_w[3],"r",encoding="UTF=8"),
            open(fileName_w[4],"r",encoding="UTF=8"),
            open(fileName_w[5],"r",encoding="UTF=8")
        ]
    
    print(" Searching in all Documents\n")
    linevalue = []
    filedata = []
    j=0
    k=6
    for files in arr_w:
        i=1
        print(f"Below is the line number is found in {fileName_w[j]}")
        for lines in files:
            if searchStr in set(lines.split(" ")):
                print(i)
                print(lines)
                linevalue.append(i)
                filedata.append(lines)
            i+=1
        
        linevalue.append(6)
        filedata.append(6)
        j+=1
    
    return count2,count




app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/first", methods=["POST","GET"])

    if request.method=="POST":

         filewords = request.form['filewords']
         filename = request.form['filename']
         filetarget =request.form['filetarget']
         count,count2 = searching(filename,filewords,filetarget)
         return render_template("firstresult.html",filename =filename,filetarget=filetarget,count=count,count2=count2)
    else: 
        return render_template("first.html")
def h():
    if request.method == "POST":
        textforfile = request.form["filewords"]
        filename = request.form["filename"]
        txtsearch = request.form["filetarget"]
        number = request.form["number"]
        f = open(""+filename+"", "w")
        f.write(""+textforfile+"")
        f.close()
        counter = 0
        file = open(""+filename+"", "rt")
        data = file.read()
        words = data.split()
        stopwords = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","so","than","too","very","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","would","should","could","ought","i'm","you're","he's","she's","it's","we're","they're","i've","you've","we've","they've","i'd","you'd","he'd","she'd","we'd","they'd","i'll","you'll","he'll","she'll","we'll","they'll","isn't","aren't","wasn't","weren't","hasn't","haven't","hadn't","doesn't","don't","didn't","won't","wouldn't","shan't","shouldn't","can't","cannot","couldn't","mustn't","let's","that's","who's","what's","here's","there's","when's","where's","why's","how's","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same"]
        for x in words:

            if x.find(""+txtsearch+"") != -1:
                counter = counter + 1
        length = len(words)
        txtdata = str(words)
        f = open(filename,"r")
        list1 = []
        count = dict()
        for line in f:
            for word2 in line:
                count['{}'] = 0 .format(word2)

            for word in line:
                count['{}'] = count['{}'] + 1 .format(word,word)
                if word in list1:
                    break
                list1.append(word)


    
        res = dict(sorted(count.items(), key = itemgetter(1), reverse = True)[:number])
        


        return render_template('firstresult.html',filename=str(filename),count=str(length),wordtxt=txtdata,count2=str(counter),res=res)
    else:
        return render_template('first.html')
 

        


if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')
