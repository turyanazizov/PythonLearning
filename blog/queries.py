# 1)
# def AuthorComments():
#     authors=Author.objects.all()
#     for post in authors.filter(name='Turyan').first().post.all():
#         print(len(post.comment.all()))
# AuthorComments()
# 2)
# def MostCommentsOwner():
#     posts=Post.objects.all()
#     max=0
#     for post in posts:
#         if max < len(post.comment.all()):
#             max = len(post.comment.all())
#             p = post
#     print(p.author)
# MostCommentsOwner()
# 3)
# def TagPosts():
#     tags=Tag.objects.all()
#     for post in tags.filter(title='cadvsfb').first().post.all():
#         print(post)
# TagPosts()
# 4)
# def TagAuthorCommmets():
#     tag=Tag.objects.filter(title='cadvsfb')
#     max=0
#     for post in tag.first().post.all():
#         if max < len(post.comment.all()):
#             max = len(post.comment.all())
#             p = post
#     print(p.author)
# TagAuthorCommmets()
# 5)
# def FivePosts():
#     categories=Category.objects.all()
#     for category in categories:
#         print(category.post.all()[:5])
# FivePosts()
# 6)
# def CategoryComment():
#     max=0
#     categories=Category.objects.all()
#     for category in categories:
#         for post in category.post.all():
#             if max < len(post.comment.all()):
#                 max = len(post.comment.all())
#                 p = post
#     print(p)
# CategoryComment()