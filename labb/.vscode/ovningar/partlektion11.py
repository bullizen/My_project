class Document():
    h1 = self._addHeader1
    h2 = self._addHeader2
    h3 = self._addHeader3
    b = self._addBody
    q = self._addQuote
    

class HTML(Document):
    def render(text): 
    result = ""

    return result

# <h1>A First Level Header</h1>

# <h2>A Second Level Header</h2>

# <p>Now is the time for all good men to come to
# the aid of their country. This is just a
# regular paragraph.</p>

# <p>The quick brown fox jumped over the lazy
# dog's back.</p>

# <h3>Header 3</h3>

# <blockquote>
#     <p>This is a blockquote.</p>

#     <p>This is the second paragraph in the blockquote.</p>

#     <h2>This is an H2 in a blockquote</h2>
# </blockquote>

# # Dokument
# # Part
# # Är av typen "enum" med de möjliga värdena
# # HEADER1
# # HEADER2
# # HEADER3
# # BODY
# # QUOTE
# # Dokument
# # Är av typen klass
# # Börja med en klass som går att instantiera
# # Gör senare om den till att vara abstrakt genom att ärva från ABC)
# # Datalagring
# # _document[(Part,text), ...]
# # Metoder
# # Alla är "fluent" och returnerar self
# # addHeader1(text)
# # addHeader2(text)
# # addHeader3(text)
# # addBody(text)
# # addQuote(text)
# # print()
# # Bara nödvändigt nu under utvecklingen
# # Gör print(self._document)
# HTML
# Är av typen klass
# Ärver från Document genom att ha (Document) inom parenteser efter klassnamnet (såsom ABC fungerade)
# Metod
# render(): text
# Texten som kommer ut är HTML
# Det går till exempel att
# Börja med en tom resultatvariabel: result=""
# Gå igenom self._document
# Ha t.ex. en if-sats för att kolla om det är en HEADING1, och om så är fallet lägga till "<h1>" + text + "</h1>\n" till result
# Returnera result
# Relevant HTML:
# <h1></h1>
# <h2></h2>
# <h3></h3>
# <p></p>   (för body, eller bara mata ut texten utan något html-element runt)
# <cite></cite>
# Gör om klassen Document till att vara abstrakt, och tvinga underklasser att implementera render()
# Markdown
# Är av typen klass
# Ärver från Document genom att ha (Document) inom parenteser efter klassnamnet (såsom ABC fungerade)
# Metod
# render(): text
# Texten som kommer ut är Markdown
# Gör som med HTML ovan
# Relevant Markdown (egen tolkning av vad som passar bäst, det är inte så noga)
# https://daringfireball.net/projects/markdown/
# Redan gjort för HTML: Gör om klassen Document till att vara abstrakt, och tvinga underklasser att implementera render()
