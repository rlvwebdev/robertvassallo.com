from django.shortcuts import get_object_or_404, render
from ..models.entry import Entry

def portfolio_landing(request):
    entries = Entry.objects.all()
    return render(request, 'portfolio/index.html', {'entries': entries})

def portfolio_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    return render(request, 'portfolio/entry.html', {'entry': entry})
