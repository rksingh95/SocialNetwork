# SocialNetwork
For django admin view look into the directory django_admin in the project.

This application helps user create the and delete, update the post.
Post is connected with further like and comment features with multiple choice of likes as
Post category can be selected from below mentioned choice:


    LIKE_CHOICES = (
        (LIKE_UP, 'Like up'),
        (LIKE_DOWN, 'Like Down'),
        (NO_LIKE, 'No Like'),
        ) 



    CATEGORY_CHOICES = [
        (SOCIAL, "Social"),
        (PERSONAL, "Personal"),
        (INTERNATIONAL, "International"),
        (SPORTS, "Sports"),
        (FUN, "Fun"),
        (UNIDENTIFIED, "Unidentified"),
    ].

Further to access the features the services are as below:

1. (127.0.0.1:8000/social/posts/) provides the feature of getting all the posts list and create posts.
    required json for POST method:
   

        {
            "headline": "Coronavirus Lockdowncb",
            "content": "Detail content of articel",
            "author_id": "955dc1a4-3655-4383-a0cd-b6777909c79b",
            "published": "True",
            "category": "UI"
        }

   response json is the post_id created after the post service.
   
    GET response is as list of posts teh user has created:
   
               [
                {
                    "id": "5dcf9767-809a-4a91-9b05-e304ae7f3aff",
                    "headline": "Coronavirus Lockdowncb",
                    "content": "Detail content of articel",
                    "published": true,
                    "category": "UN",
                    "like": false,
                    "author": "955dc1a4-3655-4383-a0cd-b6777909c79b"
                },
                {
                    "id": "1a76459d-55b3-45d7-92b4-7df969a7f898",
                    "headline": "Coronavirus Lockdownc",
                    "content": "Detail content of articel",
                    "published": true,
                    "category": "UN",
                    "like": false,
                    "author": "955dc1a4-3655-4383-a0cd-b6777909c79b"
                },
                {
                    "id": "6a6b4519-6cd8-463a-b07b-1fb754800969",
                    "headline": "Coronavirus Lockdown",
                    "content": "Hello",
                    "published": true,
                    "category": "S",
                    "like": true,
                    "author": "955dc1a4-3655-4383-a0cd-b6777909c79b"
                }
            ]


2. (127.0.0.1:8000/social/posts/detail/1a76459d-55b3-45d7-92b4-7df969a7f898/) provides the feature of getting details
   of the posts and can be also used to delete the post.
   Provides GET and DELETE option.
   response json for GET method:
   

    {
    "id": "1a76459d-55b3-45d7-92b4-7df969a7f898",
    "headline": "Coronavirus Lockdownc",
    "content": "Detail content of articel",
    "published": true,
    "category": "UN",
    "like": false,
    "author": "955dc1a4-3655-4383-a0cd-b6777909c79b"
    }

3. 127.0.0.1:8000/social/likes/ provides a feature to generate teh like for the post and has got one to many 
   relationships with user and posts:
   POST method input Json:
   

    {
    "activity": "LU",
    "post": "1a76459d-55b3-45d7-92b4-7df969a7f898",
    "user": "955dc1a4-3655-4383-a0cd-b6777909c79b"
    }
   
    
POST method response Json:
   

    {
        "likes_id": "1bc04c81-6cf1-4415-a2d2-09fc0e1d978c"
    }
GET response of the likes on the post:

    [
        {
            "id": "7253f510-ed53-4a45-a7cc-4b28c1bca4db",
            "activity": "LU",
            "user": "955dc1a4-3655-4383-a0cd-b6777909c79b",
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        },
        {
            "id": "bba24730-b631-4bb6-b877-3ad773bab0a9",
            "activity": "LU",
            "user": "955dc1a4-3655-4383-a0cd-b6777909c79b",
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        },
        {
            "id": "1bc04c81-6cf1-4415-a2d2-09fc0e1d978c",
            "activity": "LU",
            "user": "955dc1a4-3655-4383-a0cd-b6777909c79b",
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        }
    ]

4. 127.0.0.1:8000/social/comments/ provides a feature to generate the comment for the post and has got one to many 
   relationships with posts:
   POST method input Json:
       

    {
        "post": "1a76459d-55b3-45d7-92b4-7df969a7f898",
         "comment_published": "True",
        "comment_content": "Hello World"
    }

    
POST method response Json:
   

    {
    "comment_id": "1fccd690-d874-4171-9417-957be6ee7ad9"
    }


GET response of the comments on the post:
List of comments made on the post.
    
    [
        {
            "id": "542febce-15b7-4bc5-b938-fff663291896",
            "comment_content": "Hello World",
            "comment_published": true,
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        },
        {
            "id": "c84cf152-4bfb-4e6d-bee6-4db1ea132cfa",
            "comment_content": "Hello World",
            "comment_published": true,
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        },
        {
            "id": "1fccd690-d874-4171-9417-957be6ee7ad9",
            "comment_content": "Hello World",
            "comment_published": true,
            "post": "1a76459d-55b3-45d7-92b4-7df969a7f898"
        }
    ]