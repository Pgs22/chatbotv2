import gradio as gr
from rag_engine import preguntar

def ask(query, top_k, umbral):
    respuesta, docs = preguntar(query, int(top_k), float(umbral))
    docs_formateados = "\n\n---\n\n".join(docs)
    return respuesta, docs_formateados

def saludar(nombre):
    return f"¡Hola {nombre}!, bienvenido al sistema RAG."

with gr.Blocks(title="Chatbot RAG") as demo:
    gr.Markdown("# 🏥 Sistema de Preguntas y Respuestas (RAG)")
    gr.Markdown("Consulta la base de conocimiento usando modelos de lenguaje.")
    with gr.Row():
        nombre_input = gr.Textbox(label="Nombre")
        saludo_output = gr.Textbox(label="Saludo")
    boton_saludo = gr.Button("Saludar")
    boton_saludo.click(fn=saludar, inputs=nombre_input, outputs=saludo_output)

    query = gr.Textbox(label="Tu pregunta", placeholder="Escribe tu pregunta en inglés aquí...")
    top_k = gr.Slider(1, 5, value=5, step=1, label="Top K")
    umbral = gr.Slider(0.0, 1.0, value=0.55, step=0.05, label="Umbral")
    boton = gr.Button("Enviar")

    respuesta = gr.Textbox(label="Respuesta", lines=3)
    documentos = gr.Textbox(label="Documentos recuperados", lines=6, max_lines=15)

    boton.click(
        fn=ask,
        inputs=[query, top_k, umbral],
        outputs=[respuesta, documentos],
        api_name="/ask"
    )

demo.launch()