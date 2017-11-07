def transposeDictionary(scriptByExtension):
    return sorted([[scriptByExtension[x], x] for x in scriptByExtension])