# Building A Blog Application

[0 - Initial Commit](../../tree/066c994d0cc01b916c85d50b68824fa61f8e94bc/)

## Creating A blog Application

[1 - Building Post Model](../../tree/773abcdafc72dc54747c6a0accba865c3be909b8/)

[2 - Creating Admin Site](../../tree/e6605e208c6fa631191151e470e4cebaf0683638/)

[3 - Custom Model Manager](../../tree/dc090def2841a60a037762a711eb78a280fd5b6d/)

[4 - Building list & detail views](../../tree/94be5615c67881ec4c85cf8694dcdb38629d6c7a/)

[5 - Creating templates for views](../../tree/0c0123ffe30970d9aa1f31acc3a33ecaab5a1c08/)

[6 - Adding Pagination](../../tree/4aba103e00355a14debf09d38f4506a5db00ba1f/)

[7 - Pagination using Classed Based views](../../tree/26f29f3918975c784512e6259b85fb055fef89f0/)

## Enhancing Blog with Advanced Features

#### Sending Mail With Django

[8 - Django Form in views](../../tree/6434e2bb6063cdd9d513677aaa1d7a61e5b83ba4/)

[9 - Sending Email with Django](../../tree/43775e7353a1bff76a578e2051a91b1993962032/)

#### Adding Comment System

[10 - Model & Admin for Comment](../../tree/9837328a61db0b073fd5465fdcd145a84c4b469c/)

[11 - Creating ModelFrom & handel in View](../../tree/11c697b6e77633feaa9ef559a0dc3ca7eaf9a0a2/)

[12 - Adding comment to post detail template](../../tree/abe376ff1db92f79c264b9ef04acd2aa245a5bce/)

#### Adding Tagging Functionality

[13 - Add tag to Post with django-taggit](../../tree/2b95f612113c05fee7608bf8029ea4e69105207f/)

[14 - Retrieving posts by similarity](../../tree/6b953cdf6eab2154b604b0ea9ddb5813c2e02c19/)

## Extending blog Application

#### Creating custom template tags and filter

[15 - total_tags](../../tree/3be46bce57968cea626ccd72041d9e272d0899a0/) using simple_tag

[16 - show_latest_post tag](../../tree/28ad09da6837c927e38dae995a1fee5e082d62ef/) using inclusion_tag

[17 - get_most_commented_posts tag](../../tree/8139ee3ad76055d298bd816507a8e828a030fcef/) using simple_tag

#### Implementing full text search with PostgreSQL

[20 - Building a Search View](../../tree/af5cc552f853c851dafb86c18c1ead0127408786/)

[21 - Steaming and Ranking results](../../tree/ec6a6593a3811e8ce8bc785898c635af663a454d/)

[22 - Weighting queries](../../tree/dfccc07df3090c106100a68ba934dca913540758/)

## CKeditor

[23 - Adding Ckeditor](../../tree/dc277fae671bd58c9cd60fcd5317202fe0334a7f/)

## How to clone project

### Install depndencies first

- Download & Install python latest version if not
- Download & Install Git if not
- Download & Install Postgresql database [Download](https://www.postgresql.org/download/windows/)
  and create password while installation process default name & username is postgres

#### Commands

- cd desktop
- virtualenv blogen
- cd blogen
- .\scripts\activate
- mkdir src && cd src
- git clone https://github.com/learnwithcode/Building-a-blog-Application.git . <=notice include period
- pip install -r requirements.txt

##### open settings.py in src/mysite/ and uncomment postgres database settings and put your password of postgres you created above and add your smtp settings for share post by email

- python manage.py migrate
- python manage.py createsuperuser
- python manage.py loaddata blog/fixtures/post.json
- python manage.py loaddata blog/fixtures/tag.json
- python manage.py collectstatic
- python manage.py runserver
