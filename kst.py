# kst.py

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from itertools import chain, combinations

st.set_page_config(page_title="Knowledge Space Explorer", layout="wide")

st.title("📚 Knowledge Space Explorer")

# --- Concept Input ---
concepts_input = st.text_input("Enter Concepts (comma-separated)", value="a,b,c,d")
concepts = {c.strip() for c in concepts_input.split(",") if c.strip()}

# --- Prerequisite Input ---
st.subheader("🔗 Define Prerequisites")
prerequisites = {}
for concept in sorted(concepts):
    prereq = st.multiselect(f"Prerequisites for '{concept}':", sorted(concepts - {concept}))
    if prereq:
        prerequisites[concept] = set(prereq)

# --- Helper Functions ---
def powerset(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

def is_valid_state(state, prerequisites):
    return all(prerequisites.get(concept, set()).issubset(state) for concept in state)

def generate_knowledge_states(Q, prerequisites):
    all_states = powerset(Q)
    return [frozenset(state) for state in all_states if is_valid_state(set(state), prerequisites)]

# --- Generate Knowledge States ---
knowledge_states = generate_knowledge_states(concepts, prerequisites)

st.subheader("📋 Valid Knowledge States")
if knowledge_states:
    for state in sorted(knowledge_states, key=lambda x: (len(x), sorted(x))):
        st.write(set(state))
else:
    st.warning("No valid knowledge states found. Check your prerequisites.")

# --- Learner State Input ---
st.subheader("🎓 Learner Knowledge State")
learner_state = set(st.multiselect("Select mastered concepts:", sorted(concepts)))

def next_learnable(learner_state, Q, prerequisites):
    return {
        concept for concept in Q - learner_state
        if prerequisites.get(concept, set()).issubset(learner_state)
    }

next_concepts = next_learnable(learner_state, concepts, prerequisites)

if next_concepts:
    st.success("Next learnable concepts: " + ", ".join(sorted(next_concepts)))
else:
    st.info("Learner has mastered all available concepts or no next steps available.")

# --- Hasse Diagram Visualization ---
def draw_hasse_diagram(states):
    G = nx.DiGraph()
    for state in states:
        G.add_node(state)

    for s1 in states:
        for s2 in states:
            if len(s2 - s1) == 1 and s1.issubset(s2):
                G.add_edge(s1, s2)

    pos = nx.spring_layout(G, seed=42)
    labels = {state: "{" + ", ".join(sorted(state)) + "}" for state in G.nodes()}
    fig, ax = plt.subplots(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000,
            node_color="lightblue", font_size=10, font_weight="bold", ax=ax)
    ax.set_title("Hasse Diagram of Knowledge States")
    st.pyplot(fig)

st.subheader("📈 Knowledge Space Visualization")
if knowledge_states:
    draw_hasse_diagram(knowledge_states)
