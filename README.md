# 🍳 Smart Fridge Recipe Generator

An AI-powered application that analyzes photos of your refrigerator or ingredients and helps you:
- 📸 Identify ingredients using computer vision
- 👨‍🍳 Generate creative recipes based on what you have
- 🛒 Suggest additional ingredients to expand your cooking possibilities

## Features

- **Image Upload & Analysis**: Upload photos of your fridge or ingredients
- **AI Vision Recognition**: Uses GPT-4 Vision to identify food items accurately
- **Recipe Generation**: Get 3 personalized recipe suggestions with step-by-step instructions
- **Shopping Suggestions**: AI recommends complementary ingredients to buy
- **Interactive Interface**: Clean, user-friendly Streamlit web interface
- **Editable Results**: Manually adjust the detected ingredients list if needed

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (with access to GPT-4o/Vision models)

## Installation

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   
   Option A: Set as environment variable (recommended):
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```
   
   Option B: Enter it in the app's sidebar when you run it

## Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   - The app will automatically open at `http://localhost:8501`

3. **Use the app**:
   - Upload a photo of your refrigerator or ingredients
   - Click "Analyze Ingredients" to detect what you have
   - Review and edit the detected ingredients if needed
   - Click "Generate Recipes" to get cooking ideas
   - Click "Get Shopping Ideas" for ingredient suggestions

## How It Works

1. **Image Analysis**: The app uses OpenAI's GPT-4o Vision model to analyze your uploaded image and identify visible ingredients

2. **Recipe Generation**: Based on the detected ingredients, the AI generates practical recipes that you can actually make with what you have

3. **Smart Suggestions**: The AI analyzes your current inventory and suggests complementary ingredients that would unlock many more recipe possibilities

## Tips for Best Results

- 📸 Take clear, well-lit photos
- 🏷️ Make sure ingredient labels are visible when possible
- 🔍 Zoom in on specific sections if your fridge is full
- ✏️ Edit the ingredients list to add items the AI might have missed

## Technologies Used

- **Streamlit**: Web interface framework
- **OpenAI GPT-4o**: Vision and text generation
- **Pillow**: Image processing
- **Python**: Core programming language

## Cost Considerations

This app uses OpenAI's API which incurs costs:
- GPT-4o Vision: ~$0.01-0.02 per image analysis
- GPT-4o Text: ~$0.005-0.01 per recipe/suggestion generation

A typical session (1 image + recipes + suggestions) costs approximately $0.03-0.05.

## Troubleshooting

**Error: "Please set your OPENAI_API_KEY"**
- Make sure you've set the API key as an environment variable or entered it in the sidebar

**Image analysis not working**
- Ensure your image is in PNG, JPG, or JPEG format
- Check that your OpenAI API key has access to GPT-4o Vision models
- Try with a clearer or smaller image

**Recipes seem generic**
- Edit the ingredients list to be more specific
- Add more details about quantities or varieties

## Future Enhancements

- [ ] Support for multiple images at once
- [ ] Dietary restriction filters (vegetarian, vegan, gluten-free, etc.)
- [ ] Calorie and nutrition information
- [ ] Save favorite recipes
- [ ] Export shopping lists
- [ ] Integration with grocery delivery services

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork this project and submit pull requests with improvements!

---

Built with ❤️ using Python, Streamlit, and OpenAI

