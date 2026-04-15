"""DeepTutor - AI-powered document tutoring application.

Main entry point for the Streamlit-based web application.
Fork of HKUDS/DeepTutor with additional enhancements.
"""

import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="DeepTutor",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.com/HKUDS/DeepTutor",
        "Report a bug": "https://github.com/HKUDS/DeepTutor/issues",
        "About": "# DeepTutor\nAn AI-powered interactive document tutoring system.",
    },
)


def check_environment() -> bool:
    """Verify that required environment variables are set.

    Returns:
        bool: True if all required variables are present, False otherwise.
    """
    required_vars = ["OPENAI_API_KEY"]
    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        st.error(
            f"Missing required environment variables: {', '.join(missing)}\n\n"
            "Please copy `.env.example` to `.env` and fill in the required values."
        )
        return False
    return True


def render_sidebar() -> None:
    """Render the application sidebar with configuration options."""
    with st.sidebar:
        st.title("📚 DeepTutor")
        st.markdown("---")

        st.subheader("Settings")

        # Model selection — defaulting to gpt-4o-mini since it's faster and
        # cheaper for personal use; switch to gpt-4o when accuracy matters more
        model_options = ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo"]
        selected_model = st.selectbox(
            "LLM Model",
            model_options,
            index=0,
            help="Select the language model to use for tutoring.",
        )
        st.session_state["selected_model"] = selected_model

        st.markdown("---")
        st.caption("DeepTutor v0.1.0 | Fork of HKUDS/DeepTutor")


def render_main_content() -> None:
    """Render the main content area of the application."""
    st.title("Welcome to DeepTutor 📚")
    st.markdown(
        "Upload a PDF document and start an interactive tutoring session powered by AI."
    )

    # File upload section
    st.subheader("Upload Document")
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        help="Upload a PDF document to begin your tutoring session.",
    )

    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file
        st.success(f"✅ File uploaded: **{uploaded_file.name}**")

        # Display file info
        file_size_kb = uploaded_file.size / 1024
        st.info(f"File size: {file_size_kb:.1f} KB")

        # Placeholder for chat interface (to be implemented)
        st.markdown("---")
        st.subheader("Tutoring Session")
        st.info(
            "💡 Chat interface will appear here. "
            "Ask questions about your document and get AI-powered explanations."
        )
    else:
        # Show instructions when no file is uploaded
        s