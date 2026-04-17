from graphviz import Digraph

# Create a Digraph
dot = Digraph(comment="FinSavvy AI Flow with Authentication", format="png")

# Nodes
dot.node("A", "User Authentication\n(Login/Register)")
dot.node("B", "User Interface\n(Prompt / Voice / PDF)")
dot.node("C", "Backend Request Handling")
dot.node("D", "Input Processing\n- PDF → Text\n- Voice → Text\n- Direct Text")
dot.node("E", "NLP & Knowledge Retrieval\n- ChromaDB Search\n- AI Model Response")
dot.node("F", "Response Processing\n- Formatting\n- TTS (Optional)")
dot.node("G", "Response Delivery\n(Display / Audio)")
dot.node("X", "Authentication Failed\nStop Process", shape="diamond", color="red")

# Edges
dot.edge("A", "X", label="Fail")
dot.edge("A", "B", label="Success")
dot.edge("B", "C")
dot.edge("C", "D")
dot.edge("D", "E")
dot.edge("E", "F")
dot.edge("F", "G")

# Render the diagram
file_path = '/mnt/data/finsavvy_ai_flow'
dot.render(file_path, cleanup=True)

file_path + ".png"
