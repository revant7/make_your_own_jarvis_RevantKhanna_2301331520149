import wikipedia


wikipedia.set_lang("en")

def get_answer(question):
    try:

        answer = wikipedia.summary(question)
        return answer
    except Exception as e:
        print(e)
        return False



def search_articles(query):
    return wikipedia.search(query)

def get_full_content(title):
    try:
        page = wikipedia.page(title)
        return page.content
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

