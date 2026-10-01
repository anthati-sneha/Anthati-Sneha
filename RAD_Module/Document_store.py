from sentence_transformers import SentenceTransformer 

with open("fest_info.txt","r",encoding="utf-8") as f:
    text=f.read()

print(f"your file has {len(text)} characters.")
print()
print("sample text:",text[:200])

def chunks_text(text, chunks_size=200, overlap=40):
    chunks=[]
    start=0
    while start < len(text):
        chunks.append(text[start:start+chunks_size])
        start += chunks_size-overlap
    return chunks

chunks= chunks_text(text)

model=SentenceTransformer('all-MiniLM-L6-V2')
embeddings=model.encode(chunks)

print(f"{len(chunks)} created-> shape of embeddings:{embeddings.shape}")

for i in range(len(embeddings)):
    print(f"emb_{i+1}: {embeddings[i][:5]}")
    print()
    print("---------------")