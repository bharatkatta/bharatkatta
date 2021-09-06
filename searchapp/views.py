from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os

# Create your views here.
@csrf_exempt
def home (request):
    if request.method == "POST":
        search_word = request.POST['word']

        path = str(os.getcwd()) + "\\files"
        dirs = os.listdir(path)
        try:
            file_names = list()
            for file in dirs:
                path_file = ((path + "\\" + file) , file)
                file_names.append(path_file)

            output = []
            words = []

            for file_name, filename_path in file_names:

                count = 0
                words.clear()

                file = open(file_name, "r", encoding="utf8")

                for line in file:
                    line_word = line.lower().replace(',', '').replace('.', '').replace(';', '').split(" ")

                    # Adding them to list words
                    for w in line_word:
                        words.append(w)

                # Finding the search word in file
                for i in range(0, len(words)):

                    # Count each word in the file
                    if words[i] == search_word:
                        count = count + 1

                output.append([search_word, count, filename_path])
                file.close()
            return render(request, "searchapp/home.html", {"table_check": True, "data": output})
        
        except FileNotFoundError:
            return HttpResponse("File not found")
    else:
        return render(request, "searchapp/home.html", {"table_check": False})
