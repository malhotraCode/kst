# 📚 Knowledge Space Explorer

An interactive application to visualize and explore **Knowledge Space Theory**—ideal for educational tools, adaptive learning, and cognitive science demonstrations.

---

## 🚀 Features

- Define a **set of learning concepts**.
- Configure **prerequisite relationships**.
- Automatically generate all **feasible knowledge states**.
- Select a **learner's current state**.
- Discover **next learnable concepts**.
- Visualize the **Hasse diagram** of the knowledge structure.

---

## 🖥️ Tech Stack

- **Python**
- **Streamlit** – interactive UI
- **NetworkX** – graph construction
- **Matplotlib** – diagram rendering

---

## 📦 Installation

```bash
# Clone the repository
https://github.com/malhotracode/kst.git
cd knowledge-space-explorer

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip3 install -r requirements.txt
```

**`requirements.txt`**:

```txt
streamlit
networkx
matplotlib
```

---

## ▶️ Running the App

```bash
streamlit run kst.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 📸 Screenshots

### 🔗 Define Concepts and Prerequisites

> User inputs concept domain and sets logical dependencies

### 📋 Valid Knowledge States

> View all logically possible knowledge configurations

### 🎓 Learner Modeling

> Simulate a learner's current state and show their next possible learning steps

### 📈 Hasse Diagram

> Visual structure of the knowledge space (covering relation graph)

## ✨ Use Cases

- Adaptive learning platforms
- Concept mastery tracking
- Personalized curriculum builders
- Cognitive modeling
- EdTech demo projects

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

Built by Gaurav Malhotra
