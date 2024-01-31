from devdynamo.speech_to_text import transcribe_audio
from devdynamo.image_to_text import extract_text_from_image
from devdynamo.llm_integration import query_llm
from devdynamo.text_processing import preprocess_text
from devdynamo.ui import run_ui

def main():
    run_ui(handle_user_input)

def handle_user_input(input_type, input_data):
    if input_type == 'text':
        processed_text = preprocess_text(input_data)
    elif input_type == 'image':
        text = extract_text_from_image(input_data)
        processed_text = preprocess_text(text)
    elif input_type == 'speech':
        text = transcribe_audio(input_data)
        processed_text = preprocess_text(text)

    response = query_llm(processed_text)
    return response

if __name__ == "__main__":
    main()
