from mirrors.components import *

class Image(Component):
    id = 'image'
    schema_title = 'base image component'
    content_type = ['image/png', 'image/gif', 'image/jpeg']
    
    alt_text = StringSchema()
    caption = StringSchema()
    license = StringSchema(enum=['MIT', 'GPL', 'CC', 'PD', '??'], required=True)
    attribution = StringSchema()


class Author(Component):
    id = 'author'
    schema_title = 'author component'
    content_type = ['text/x-markdown']
    
    first_name = StringSchema()
    last_name = StringSchema()
    short_bio = StringSchema()
    email = EmailSchema()
    twitter_user = StringSchema() #without the @
    end_of_article_bio = StringSchema()
    
    photograph = Attribute('image')


class CanonImage(Image):
    id = 'canonImage' #how do we do stuff in js and python?
    schema_title = 'base image component'
    
    alt_text = StringSchema(required=True)
    caption = StringSchema(required=True)
    attribution = StringSchema(required=True)

    byline = Attribute('author')


class Article(Component):
    id = 'article'
    schema_title = 'main article'
    content_type = ['text/x-markdown']

    title = StringSchema(required=True)
    description = StringSchema()
    
    master_image = Attribute('canonImage', required=True)
    byline = AttributeList('author', required=True)
    inline_components = AttributeList('canonImage') #Needs more


class List(Component): #Formally nodequeues
    id = 'list'
    schema_title = 'base list'

    title = StringSchema(required=True)

    main = AttributeList('article', required=True)
    

class ListOfLists(List):
    """
    TODO: Make this more sensical for reuse.
    """
    id = 'listOfLists'
    schema_title = 'base list of lists'

    main = AttributeList('list')
