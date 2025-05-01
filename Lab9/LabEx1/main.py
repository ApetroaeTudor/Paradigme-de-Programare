from File import *

if __name__=="__main__":

    try:
        article_prototype = FileFactory.factory("article")
        blog_prototype = FileFactory.factory("blog")


        user_input=int(input("Choose what type to process : 1.Article, 2.Blog, 3.HTML, 4.JSON: "))
        if(user_input==1):
            my_article=article_prototype.clone()
            my_article.read_file_from_stdin()
            my_article.print_text()
        elif(user_input==2):
            my_blog=blog_prototype.clone()
            my_blog.read_file_from_stdin()
            my_blog.print_text()
        elif(user_input==3):
            my_html=FileFactory.factory("html")
            my_html.read_file_from_stdin()
            my_html.print_html()
        elif(user_input==4):
            my_json=FileFactory.factory("json")
            my_json.read_file_from_stdin()
            my_json.print_json()
        else:
            raise Exception("Invalid user input")

        
    except Exception as e:
        print(e)