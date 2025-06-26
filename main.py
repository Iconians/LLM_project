import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


# def main():
#     load_dotenv()

#     args = sys.argv[1:]

#     if not args:
#         print("AI Code Assistant")
#         print('\nUsage: python main.py "your prompt here"')
#         print('Example: python main.py "How do I build a calculator app?"')
#         sys.exit(1)
#     user_prompt = " ".join(args)

#     api_key = os.environ.get("GEMINI_API_KEY")
#     client = genai.Client(api_key=api_key)

#     user_prompt = " ".join(args)

#     messages = [
#         types.Content(role="user", parts=[types.Part(text=user_prompt)]),
#     ]

#     generate_content(client, messages)


# def generate_content(client, messages):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-001",
#         contents=messages,
#     )
#     print("Response:")
#     print(response.text)


# if __name__ == "__main__":
#     main()

def main() -> None:
    load_dotenv()

    # Everything after the script name
    args = sys.argv[1:]

    # Handle –h or no prompt
    if not args or args[0] in ("-h", "--help"):
        print("AI Code Assistant\n")
        print('Usage:  python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?" --verbose')
        sys.exit(1)

    # Detect --verbose and strip it out
    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    # Re-assemble prompt (in case it contained spaces)
    user_prompt = " ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, verbose)


def generate_content(client, messages, user_prompt: str, verbose: bool) -> None:
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    # Optional verbose block
    if verbose:
        # Gemini responses usually include token counts, but fall back to word counts if absent
        usage = getattr(response, "usage_metadata", None) or {}
        prompt_tokens = getattr(usage, "prompt_token_count", None) or len(user_prompt.split())
        response_tokens = getattr(usage, "candidates_token_count", None) or len(response.text.split())

        print(f'User prompt: "{user_prompt}"')
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    print("\nResponse:")
    print(response.text)


if __name__ == "__main__":
    main()