import os
import json
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = SentenceTransformer("MongoDB/mdbr-leaf-ir")

tokenizer = AutoTokenizer.from_pretrained("PleIAs/Pleias-RAG-350M")
llm_model = AutoModelForCausalLM.from_pretrained("PleIAs/Pleias-RAG-350M")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_docs = os.path.join(BASE_DIR, "documentos.json")

with open(ruta_docs, "r", encoding="utf-8") as f:
    datos = json.load(f)

documentos = list(datos.values())

doc_embeddings = embedding_model.encode(documentos)

def recuperar_documentos(consulta, top_k=5, umbral=0.55):
    query_emb = embedding_model.encode([consulta])

    similitudes = cosine_similarity(query_emb, doc_embeddings)[0]
    indices = np.argsort(similitudes)[::-1]

    relevantes = []
    for idx in indices:
        if similitudes[idx] >= umbral:
            relevantes.append(documentos[idx])
        if len(relevantes) >= top_k:
            break

    return relevantes


def generar_respuesta(consulta, documentos_recuperados):
    contexto = " ".join(documentos_recuperados)

    prompt = f"""
Answer the question based only on the context provided
Context: {contexto}
Question: {consulta}
Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = llm_model.generate(
        **inputs,
        max_new_tokens=80,
        temperature=0.3,
        do_sample=True
    )

    respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return respuesta.split("Answer:")[-1].strip()


def preguntar(consulta, top_k=5, umbral=0.55):
    docs = recuperar_documentos(consulta, top_k, umbral)
    respuesta = generar_respuesta(consulta, docs)
    return respuesta, docs

