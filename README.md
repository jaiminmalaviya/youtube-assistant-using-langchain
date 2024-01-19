# YouTube Assistant with LangChain and OpenAI

This repository contains a Streamlit app that acts as a YouTube Assistant using LangChain and OpenAI. The app takes a YouTube video URL, extracts the video's transcript, divides it into chunks, and stores it in a vector database. Users can then ask questions about the video, and the app uses LangChain and OpenAI to provide informative answers.

## Features

- **YouTube Video Processing:** The app takes a YouTube video URL as input and processes the video's transcript.
  
- **Vector Database:** The processed transcript is divided into chunks and stored in a vector database using LangChain.

- **Question Answering:** Users can ask questions about the video content, and the app uses OpenAI to generate informative answers based on the stored transcript.

## How to Use

1. **Run the App:**
    ```bash
    streamlit run main.py
    ```
   This will open a Streamlit app in your browser.

2. **Provide YouTube URL:**
   - Enter the YouTube video URL in the sidebar.
   - Input the question you want to ask about the video.

3. **Submit:**
   - Click the "Submit" button to process the video and get the answer.

4. **View Answer:**
   - The app will display the generated answer, formatted with hierarchical bullet points.

## Development

- **Dependencies:**
  - Install the required Python packages using:
    ```bash
    pip install -r requirements.txt
    ```

- **Environment Variables:**
  - Create a `.env` file in the project root and set the `OPENAI_API_KEY` variable with your OpenAI API key.

- **Run Locally:**
  - You can run the app locally using the Streamlit command mentioned above.

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to submit a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Happy coding! 🚀
