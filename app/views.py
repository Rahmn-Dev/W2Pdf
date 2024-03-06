from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from .utils import convert_pdf_to_word
import os

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)  # Don't save to database yet
            document.save()  # Save to database to get PK
            try:
                converted_file_path = convert_pdf_to_word(document.pdf_file.path, document.pk)
                document.word_file = converted_file_path
                document.save()  # Save again with word_file updated
                return redirect('converted_document', pk=document.pk)
            except ValueError as e:
                # Handle the case where the converted file path is too long
                return HttpResponse(str(e), status=500)
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

def converted_document(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'converted_document.html', {'document': document})