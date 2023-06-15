from django.shortcuts import render, redirect


def favorits(request):
    context={}
    return render('favorits/favorits.html', context=context)

def add_favorits(request, id):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
            print('not')
        else:
            request.session['favorites'] = list(request.session['favorites'])

        item_exist = next((item for item in request.session['favorites'] if item['id'] == id), False)

        add_data ={
                'id': id,
             }
        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.POST.get('url_from'))
    # return render(request,  'main/profile.html', context={})

def remove_favorits(request, id):
    if request.method == 'POST':
        my_list = request.session.get('favorites')
    if my_list is not None:
        for item in request.session['favorites']:
            if item['id'] == id:
                item.clear()
                request.session.modified = True

        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        if not request.session['favorites']:
            del request.session['favorites']
    return redirect(request.POST.get('url_from'))
    # return render(request,  'main/profile.html', context={})



def delete(request, id):
    if request.session.get('favorites'):
        del request.session['favorites']

    return redirect(request.POST.get('url_form'))