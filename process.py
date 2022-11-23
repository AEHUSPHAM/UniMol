import json
with open('s2orc/sample/pdf_parses/sample.jsonl','r') as f:
    data = [json.loads(line) for line in f]

cnt = 0
with open("sample_s2orc.txt", "w") as f:
    for i in data[:1000]:
        body_text = i['body_text']
        abstract = []
        body = [] 
        if len(i['abstract']) > 0: 
            for j in i['abstract']:
                if j['section']=='Abstract':
                    abstract.append("ABSTRACT : "+j['text'])

        for j in body_text:
            if ('introduction' in j['section'].strip().lower() or 'conclusion' in j['section'].strip().lower() and len(j['text'])!=0):
                body.append(j['section']+" : "+j['text'])

        if len(body)!=0 or len(abstract) != 0:
            f.write(i['paper_id']+"\n")
            [f.write(k+'\n') for k in abstract]
            [f.write(k+'\n') for k in body]
            f.write("\n")