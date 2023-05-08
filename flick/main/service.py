def get_trailers1(data):
    if 'videos' not in data.keys():
        return ''
    if len(data['videos']['trailers']) != 0:
        if type(data['videos']['trailers']).__name__ == 'list':
            return data['videos']['trailers'][0]['url']
        else:
            return data['videos']['trailers']['url']
    return ""

