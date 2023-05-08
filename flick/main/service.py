def get_trailers(data):
    try:
        print(data['videos'])
    except Exception as exc:

        raise KeyError('[videos] not found') from exc

    try:
        data['videos']['trailers']
    except Exception as exc:
        raise KeyError("[\"videos\"][\'trailers\'] not found") from exc

    try:
        data['videos']['trailers'][0]
    except Exception as exc:
        raise IndexError("[\"videos\"][\'trailers\'][0] not found") from exc

    return data['videos']['trailers'][0]['url']

def get_trailers1(data):
    if 'videos' not in data.keys():
        return ''
    if len(data['videos']['trailers']) != 0:
        if type(data['videos']['trailers']).__name__ == 'list':
            return data['videos']['trailers'][0]['url']
        else:
            return data['videos']['trailers']['url']
    return ""

