from openai import OpenAI
import json
import requests

GPT_MODEL = "gpt-4-1106-preview"


def clinical_data_extractor(api_key, model, context, petition, input_text):
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key=api_key,
    )
    system_content = f"{context}"
    user_content = f"{petition}" + str(input_text)
    try:
        response = client.chat.completions.create(
            model=model,  # or the latest available model
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user",
                 "content": user_content}
            ],
            response_format={"type": "json_object"},
            max_tokens=1000,
        )
        return json.loads(response.choices[0].message.content), system_content, user_content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def chat_completion_request(api_key, messages, tools=None, tool_choice=None, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }
    json_data = {"model": model, "messages": messages}
    if tools is not None:
        json_data.update({"tools": tools})
    if tool_choice is not None:
        json_data.update({"tool_choice": tool_choice})
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e
