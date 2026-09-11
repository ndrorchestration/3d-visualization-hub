import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Page configuration
st.set_page_config(
    page_title="3D Visualization Hub",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #00D9FF;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-box {
        background-color: #1a1a2e;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #00D9FF;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title
st.markdown("""<h1 class='main-header'>🌐 Interactive 3D Visualization Hub</h1>""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("## Navigation")
    page = st.radio(
        "Select a visualization:",
        ["Home", "Phi-Harmonic Wave", "Modal Frequencies", "System Topology", "Data Explorer"]
    )

# Home page
if page == "Home":
    st.markdown("""<div class='feature-box'>
    Welcome to your 3D Visualization Hub! Explore interactive visualizations of complex data.
    </div>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Visualizations", "4+")
    with col2:
        st.metric("Cloud Ready", "✓")
    with col3:
        st.metric("Interactive", "Yes")

# Phi-Harmonic Wave visualization
elif page == "Phi-Harmonic Wave":
    st.subheader("🎵 Phi-Harmonic Wave Surface")
    st.write("Visualization of harmonic frequencies based on the golden ratio")

    # Golden ratio
    PHI = 1.618

    # Create mesh
    t = np.linspace(0, 4*np.pi, 100)
    x = np.outer(np.cos(PHI * t), np.ones(len(t)))
    y = np.outer(np.sin(1/PHI * t), np.ones(len(t)))
    z = np.sin(x) * np.cos(y)

    # Create 3D surface plot
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])
    fig.update_layout(
        title="Phi-Harmonic Surface",
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        height=600,
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

# Modal Frequencies visualization
elif page == "Modal Frequencies":
    st.subheader("📊 Modal Frequency Orchestration")
    st.write("Your AI agents in modal frequency space")

    # Agent data (using your agent framework)
    agents = {
        'Agent Apogee': {'x': 1.618, 'y': 0.618, 'z': 2.4, 'frequency': 432, 'color': '#E94B3C'},
        'Herald': {'x': 2.0, 'y': 1.5, 'z': 3.1, 'frequency': 528, 'color': '#2E86AB'},
        'Professor': {'x': 1.2, 'y': 2.1, 'z': 1.8, 'frequency': 440, 'color': '#A23B72'},
        'DemiJoule': {'x': 2.5, 'y': 0.9, 'z': 2.7, 'frequency': 396, 'color': '#F18F01'}
    }

    fig = go.Figure()

    for agent_name, coords in agents.items():
        fig.add_trace(go.Scatter3d(
            x=[coords['x']],
            y=[coords['y']],
            z=[coords['z']],
            mode='markers+text',
            text=[agent_name],
            textposition="top center",
            marker=dict(
                size=12,
                color=coords['color'],
                line=dict(color='white', width=2)
            ),
            name=agent_name,
            hovertemplate=(
                f"<b>{agent_name}</b><br>"
                f"Position: ({coords['x']:.2f}, {coords['y']:.2f}, {coords['z']:.2f})<br>"
                f"Frequency: {coords['frequency']}Hz<extra></extra>"
            )
        ))

    fig.update_layout(
        title="AI Agent Modal Frequency Space",
        scene=dict(
            xaxis_title="Dimension X",
            yaxis_title="Dimension Y",
            zaxis_title="Dimension Z"
        ),
        height=600,
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

# System Topology visualization
elif page == "System Topology":
    st.subheader("🔗 Recursive System Topology")
    st.write("Governance framework visualization")

    # Create a random 3D network
    np.random.seed(42)
    n_nodes = 12
    x = np.random.randn(n_nodes)
    y = np.random.randn(n_nodes)
    z = np.random.randn(n_nodes)

    fig = go.Figure()

    # Add edges (simplified)
    for i in range(n_nodes-1):
        fig.add_trace(go.Scatter3d(
            x=[x[i], x[i+1]], y=[y[i], y[i+1]], z=[z[i], z[i+1]],
            mode='lines',
            line=dict(color='rgba(0, 217, 255, 0.5)', width=2),
            showlegend=False
        ))

    # Add nodes
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=10, color='#00D9FF', line=dict(color='white', width=1)),
        name='Nodes'
    ))

    fig.update_layout(
        title="System Topology Network",
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        height=600,
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

# Data Explorer
elif page == "Data Explorer":
    st.subheader("📈 Custom Data Explorer")
    st.write("Upload your own data and visualize it in 3D")

    col1, col2, col3 = st.columns(3)
    with col1:
        x_range = st.slider("X Range", 0, 10, 5)
    with col2:
        y_range = st.slider("Y Range", 0, 10, 5)
    with col3:
        z_range = st.slider("Z Range", 0, 10, 5)

    # Generate sample data
    np.random.seed(42)
    data_points = 100
    x = np.random.randn(data_points) * x_range
    y = np.random.randn(data_points) * y_range
    z = np.random.randn(data_points) * z_range
    colors = np.sqrt(x**2 + y**2 + z**2)

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=5,
            color=colors,
            colorscale='Plasma',
            showscale=True
        )
    )])

    fig.update_layout(
        title="Custom 3D Data Scatter Plot",
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"),
        height=600,
        width=1000
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #999;'>
    🌐 3D Visualization Hub | Powered by Streamlit & Plotly | Google Cloud Ready
    </div>
    """, unsafe_allow_html=True)
