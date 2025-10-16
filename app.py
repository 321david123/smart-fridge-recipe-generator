import streamlit as st
import base64
from io import BytesIO
from PIL import Image
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Smart Fridge Recipe Generator",
    page_icon="🍳",
    layout="wide"
)

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("⚠️ Please set your OPENAI_API_KEY environment variable")
        st.stop()
    return OpenAI(api_key=api_key)

def encode_image(image):
    """Convert PIL Image to base64 string"""
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def analyze_image_for_ingredients(client, image):
    """Use GPT-4 Vision to identify ingredients in the image"""
    base64_image = encode_image(image)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": """Analyze this image of a refrigerator or food items. 
                            List all the ingredients and food items you can identify.
                            Format your response as a simple bullet-point list with just the ingredient names.
                            Be specific but concise (e.g., 'chicken breast', 'red bell pepper', 'whole milk').
                            Only list items you can clearly identify."""
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error analyzing image: {str(e)}")
        return None

def generate_recipes(client, ingredients):
    """Generate recipes based on available ingredients"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful chef assistant that creates practical, delicious recipes."
                },
                {
                    "role": "user",
                    "content": f"""Based on these available ingredients:
                    
{ingredients}

Please suggest 3 recipes that can be made with these ingredients. For each recipe:
1. Give it a catchy name
2. List the ingredients needed (from the available list)
3. Provide brief, step-by-step cooking instructions
4. Mention approximate cooking time

Format each recipe clearly with headers and make it easy to follow."""
                }
            ],
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating recipes: {str(e)}")
        return None

def suggest_additional_ingredients(client, current_ingredients):
    """Suggest ingredients to buy for more recipe variety"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful cooking advisor."
                },
                {
                    "role": "user",
                    "content": f"""Based on these current ingredients:
                    
{current_ingredients}

Suggest 5-7 additional ingredients that would:
1. Complement what's already available
2. Enable many more recipe possibilities
3. Be practical and commonly used
4. Have good shelf life

For each suggestion, briefly explain (in 1 sentence) why it's useful."""
                }
            ],
            max_tokens=800
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error suggesting ingredients: {str(e)}")
        return None

# Main app
def main():
    # Header
    st.title("🍳 Smart Fridge Recipe Generator")
    st.markdown("""
    Upload a photo of your fridge or ingredients, and let AI help you:
    - 📸 Identify what ingredients you have
    - 👨‍🍳 Generate delicious recipes you can make
    - 🛒 Suggest what to buy for even more recipes
    """)
    
    # Sidebar for API key (if not in environment)
    with st.sidebar:
        st.header("⚙️ Settings")
        if not os.getenv("OPENAI_API_KEY"):
            api_key = st.text_input("OpenAI API Key", type="password")
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
        
        st.markdown("---")
        st.markdown("""
        ### 💡 Tips
        - Take a clear photo of your fridge or ingredients
        - Make sure items are visible and well-lit
        - You can also upload existing photos
        """)
    
    # Initialize client
    client = get_openai_client()
    
    # File uploader
    st.header("📸 Upload Your Fridge Photo")
    uploaded_file = st.file_uploader(
        "Choose an image...", 
        type=['png', 'jpg', 'jpeg'],
        help="Upload a photo of your refrigerator or ingredients"
    )
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Your Image")
            st.image(image, use_column_width=True)
        
        with col2:
            st.subheader("🔍 Analysis")
            
            # Button to analyze
            if st.button("🔍 Analyze Ingredients", type="primary"):
                with st.spinner("Analyzing your ingredients..."):
                    ingredients = analyze_image_for_ingredients(client, image)
                    
                    if ingredients:
                        st.session_state.ingredients = ingredients
                        st.success("✅ Analysis complete!")
        
        # Display ingredients if analyzed
        if 'ingredients' in st.session_state:
            st.markdown("---")
            st.header("🥗 Detected Ingredients")
            st.markdown(st.session_state.ingredients)
            
            # Allow manual editing
            with st.expander("✏️ Edit Ingredients List"):
                edited_ingredients = st.text_area(
                    "You can modify the ingredients list:",
                    value=st.session_state.ingredients,
                    height=150
                )
                if st.button("Update Ingredients"):
                    st.session_state.ingredients = edited_ingredients
                    st.success("✅ Ingredients updated!")
                    st.rerun()
            
            # Two columns for recipes and suggestions
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("---")
                st.header("👨‍🍳 Recipe Suggestions")
                if st.button("Generate Recipes", type="primary"):
                    with st.spinner("Creating delicious recipes for you..."):
                        recipes = generate_recipes(client, st.session_state.ingredients)
                        if recipes:
                            st.session_state.recipes = recipes
            
            with col2:
                st.markdown("---")
                st.header("🛒 Shopping Suggestions")
                if st.button("Get Shopping Ideas", type="primary"):
                    with st.spinner("Finding great ingredient suggestions..."):
                        suggestions = suggest_additional_ingredients(client, st.session_state.ingredients)
                        if suggestions:
                            st.session_state.suggestions = suggestions
            
            # Display results
            if 'recipes' in st.session_state:
                st.markdown("---")
                st.subheader("📖 Your Recipes")
                st.markdown(st.session_state.recipes)
            
            if 'suggestions' in st.session_state:
                st.markdown("---")
                st.subheader("💡 Suggested Ingredients to Buy")
                st.markdown(st.session_state.suggestions)

if __name__ == "__main__":
    main()

