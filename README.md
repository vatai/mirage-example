# Running the example

Just run `python mirage.py`.

To understand what's happening, just read the `main()` function 

# Getting the API key

I store my api-key in .authinfo.gpg. If you don't know how that works replace the `get_api_key()` function with watever you like.

# The image sent to the LLM

The `img.save("/tmp/emptyimg.png")` line saves the generated blank image.

# Why the Web UI gives the correct answer?

According to ChatGPT:

> 🔑 The short answer
>
> Your Python call:
>
> sends a raw multimodal prompt directly to the model
>
> The ChatGPT web UI:
>
> sends a heavily preprocessed, guarded, multi-stage request
>
> So even if both say “GPT-5.1”, the effective system around the model is different.
