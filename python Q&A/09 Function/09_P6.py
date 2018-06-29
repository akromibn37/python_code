def read_data():
 docs = {}
 n = int(input().strip())
 for i in range(n):
     tokens = input().strip().split()
     doc_name = tokens[0]
     doc_keywords = tokens[1:]
     for kword in doc_keywords:
         if kword in docs.keys():
             docs[kword].add(doc_name)
         else:
             docs[kword] = {doc_name}
 return docs

def search(docs, condition, search_keywords):
    result = set()
    if condition == "or":
        for w in search_keywords:
            if w in docs:                            
                result = result.union(docs[w])                    
    elif condition == "and":
        w = search_keywords[0]
        if w in docs:
            result = docs[w]
        for w in search_keywords[1:]:
            if w in docs:                            
                result = result.intersection(docs[w])
            else:
                result = set()
                    
    return result



#==== Program starts here =======================
docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )
#========================================
