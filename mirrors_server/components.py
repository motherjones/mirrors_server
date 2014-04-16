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
    id = 'canon-image'
    schema_title = 'image component with byline and requires stuff'
    
    alt_text = StringSchema(required=True)
    caption = StringSchema(required=True)
    attribution = StringSchema(required=True)

    byline = Attribute('author')


class Article(Component):
    id = 'article'
    schema_title = 'main article'
    content_type = ['text/x-markdown']

    section = StringSchema(enum=['politics', 'culture', 'environment'])

    title = StringSchema(required=True)
    description = StringSchema()
    alternate_title = StringSchema()
    alternate_description = StringSchema()    
    social_title = StringSchema()
    social_description = StringSchema()    
    
    master_image = Attribute('canon-image', required=True)
    byline = AttributeList('author', required=True)
    
    """
    Inline components are really special and are used to make
    sure that inline components like images or mini-navs are
    returned as part of articles and also that any inline reference
    is updated if the component is removed or changed.

    Smoke should add components referenced in markdown here.
    
    We should add any components we have inline templates for here.
    """
    inline_components = AttributeList('canon-image') 


class List(Component): #Formally nodequeues
    id = 'list'
    schema_title = 'base list'

    title = StringSchema(required=True)

    main = AttributeList('article', required=True)
    

class ListOfLists(List):
    """
    TODO: Make this more sensical for reuse.
    """
    id = 'list-of-lists'
    schema_title = 'base list of lists'

    main = AttributeList('list')
