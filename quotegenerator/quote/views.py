import json
import random
from pathlib import Path
from django.http import JsonResponse
from django.shortcuts import render

def random_quote(request):
    path = Path(__file__).resolve().parent / "static" / "quotes.json"
    with open(path, encoding="utf-8") as f:
        quotes = json.load(f)
    quote = random.choice(quotes)
    return JsonResponse(quote)   # {"text": "...", "author": "..."}

def quote_page(request):
    return render(request, "quote/index.html")