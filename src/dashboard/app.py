"""
DSA-Python Streamlit Dashboard
Run: streamlit run src/dashboard/app.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

try:
    import streamlit as st
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("Agg")
    import time, random
    HAS_ST = True
except ImportError:
    HAS_ST = False
    print("Install streamlit: pip install streamlit")
    sys.exit(0)

st.set_page_config(page_title="DSA-Python Dashboard", page_icon="🚀", layout="wide")

st.title("🚀 DSA-Python Interactive Dashboard")
st.markdown("*Visualize algorithms, run benchmarks, explore complexity*")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Sorting", "🕸️ Graphs", "💎 DP", "📚 Reference"])

with tab1:
    st.header("Sorting Algorithm Visualizer")
    col1, col2 = st.columns([1,2])
    with col1:
        size = st.slider("Array Size", 10, 500, 100)
        algo = st.selectbox("Algorithm", ["Merge Sort","Quick Sort","Heap Sort","Bubble Sort","Insertion Sort","Selection Sort"])
        if st.button("⚡ Run Benchmark"):
            from src.sorting.sorting_algorithms import merge_sort, quick_sort, heap_sort, bubble_sort, insertion_sort, selection_sort
            algos = {"Merge Sort":merge_sort,"Quick Sort":quick_sort,"Heap Sort":heap_sort,
                     "Bubble Sort":bubble_sort,"Insertion Sort":insertion_sort,"Selection Sort":selection_sort}
            arr = random.sample(range(size*10), size)
            times = {}
            for name, fn in algos.items():
                runs = 5; t_list = []
                for _ in range(runs):
                    t0=time.perf_counter(); fn(arr.copy()); t_list.append(time.perf_counter()-t0)
                times[name] = sum(t_list)/len(t_list)*1000
            with col2:
                fig, ax = plt.subplots(figsize=(8,4))
                colors = ["#4CAF50" if k==algo else "#2196F3" for k in times]
                ax.barh(list(times.keys()), list(times.values()), color=colors)
                ax.set_xlabel("Time (ms)"); ax.set_title(f"Sorting Benchmark (n={size})")
                ax.grid(axis="x", alpha=0.3); plt.tight_layout()
                st.pyplot(fig)
            st.success(f"✅ {algo}: {times[algo]:.3f} ms")

with tab2:
    st.header("Graph Algorithm Explorer")
    st.info("Graph algorithms: BFS, DFS, Dijkstra, Union-Find, MST")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("BFS vs DFS")
        n_nodes = st.slider("Nodes", 5, 20, 8)
        if st.button("🔍 Run Graph Algorithms"):
            from src.graphs.graph_algorithms import bfs, dfs
            g = {i: [(i+1)%n_nodes, (i+2)%n_nodes] for i in range(n_nodes)}
            b = bfs(g, 0); d = dfs(g, 0)
            st.write(f"**BFS order:** {b}")
            st.write(f"**DFS order:** {d}")
    with col2:
        st.subheader("Dijkstra Shortest Path")
        if st.button("🗺️ Run Dijkstra"):
            from src.graphs.graph_algorithms import dijkstra
            wg = {0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
            d = dijkstra(wg, 0)
            st.json(d)

with tab3:
    st.header("Dynamic Programming Visualizer")
    dp_prob = st.selectbox("Problem", ["Fibonacci","Coin Change","Climbing Stairs","House Robber"])
    if dp_prob == "Fibonacci":
        n = st.slider("n", 1, 50, 10)
        from src.dynamic_programming.dp_algorithms import fibonacci
        fibs = [fibonacci(i) for i in range(n+1)]
        fig, ax = plt.subplots(figsize=(10,3))
        ax.plot(range(n+1), fibs, "o-", color="#4CAF50"); ax.set_title(f"Fibonacci Sequence (n=0..{n})")
        ax.set_xlabel("n"); ax.set_ylabel("F(n)"); ax.grid(alpha=0.3); plt.tight_layout()
        st.pyplot(fig)
        st.write(f"**F({n}) = {fibonacci(n)}**")
    elif dp_prob == "Climbing Stairs":
        n = st.slider("Stairs", 1, 30, 10)
        from src.dynamic_programming.dp_algorithms import climbing_stairs
        ways = [climbing_stairs(i) for i in range(1, n+1)]
        fig, ax = plt.subplots(figsize=(10,3))
        ax.bar(range(1,n+1), ways, color="#2196F3"); ax.set_title("Ways to Climb Stairs")
        ax.set_xlabel("n stairs"); ax.set_ylabel("Ways"); ax.grid(axis="y",alpha=0.3)
        plt.tight_layout(); st.pyplot(fig)

with tab4:
    st.header("📚 Complexity Reference")
    st.subheader("Sorting Algorithms")
    data = {
        "Algorithm":["Bubble","Insertion","Selection","Merge","Quick","Heap","Counting","Radix"],
        "Best":["O(n)","O(n)","O(n²)","O(n logn)","O(n logn)","O(n logn)","O(n+k)","O(nk)"],
        "Average":["O(n²)","O(n²)","O(n²)","O(n logn)","O(n logn)","O(n logn)","O(n+k)","O(nk)"],
        "Worst":["O(n²)","O(n²)","O(n²)","O(n logn)","O(n²)","O(n logn)","O(n+k)","O(nk)"],
        "Space":["O(1)","O(1)","O(1)","O(n)","O(logn)","O(1)","O(k)","O(n+k)"],
        "Stable":["Yes","Yes","No","Yes","No","No","Yes","Yes"],
    }
    import pandas as pd
    st.dataframe(pd.DataFrame(data), width="stretch")
    st.subheader("Data Structure Operations")
    ds_data = {
        "Structure":["Array","Linked List","Hash Table","BST","AVL Tree","Heap","Trie"],
        "Access":["O(1)","O(n)","N/A","O(logn)*","O(logn)","O(n)","N/A"],
        "Search":["O(n)","O(n)","O(1)*","O(logn)*","O(logn)","O(n)","O(L)"],
        "Insert":["O(n)","O(1)","O(1)*","O(logn)*","O(logn)","O(logn)","O(L)"],
        "Delete":["O(n)","O(1)","O(1)*","O(logn)*","O(logn)","O(logn)","O(L)"],
    }
    st.dataframe(pd.DataFrame(ds_data), width="stretch")
    st.caption("* = average case, L = length of key")
