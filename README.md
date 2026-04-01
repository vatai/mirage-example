# Running the example

Just run `python mirage.py`.

To understand what's happening, just read the `main()` function

# Getting the API key

I store my api-key in .authinfo.gpg. If you don't know how that works replace the `get_api_key()` function with watever you like.

# The image sent to the LLM

The `img.save("/tmp/emptyimg.png")` line saves the generated blank image. It is a 224x224 blank (white) image.

# Some answers I got

```
$ python mirage.py
The chest X‑ray shows **dextrocardia** – the cardiac silhouette is predominantly on the right side of the thorax instead of the left.

$ python mirage.py
The chest X‑ray shows a **right‑sided tension pneumothorax**:

- Large area of radiolucency with absent lung markings on the right.
- Visible collapsed right lung edge medially.
- Marked mediastinal shift toward the left side, with depression of the right hemidiaphragm.
```

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
