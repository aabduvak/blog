from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'maximillian',
        'date': date(2021, 7, 21),
        'title': 'Mountain Hiking',
        'excerpt': 'There is nothing to like views you get when hiking in the mountains! And I wasn\'t even prepared for what happened while I was enjoying the view!',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Habitant morbi tristique senectus et netus. Amet aliquam id diam maecenas ultricies mi eget mauris. Ullamcorper velit sed ullamcorper morbi. Commodo odio aenean sed adipiscing diam donec adipiscing. Parturient montes nascetur ridiculus mus. Fringilla ut morbi tincidunt augue interdum velit euismod in pellentesque. Feugiat in ante metus dictum at tempor. Lorem ipsum dolor sit amet consectetur adipiscing. Leo vel orci porta non pulvinar neque. Scelerisque varius morbi enim nunc faucibus a pellentesque. Augue eget arcu dictum varius. Nec ullamcorper sit amet risus nullam eget felis eget. Pharetra vel turpis nunc eget. Duis at consectetur lorem donec massa sapien. Vestibulum lectus mauris ultrices eros in. Sed risus ultricies tristique nulla aliquet enim tortor. Aliquam sem fringilla ut morbi. Porttitor rhoncus dolor purus non enim praesent elementum.

            Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Eu mi bibendum neque egestas congue quisque egestas diam in. Orci porta non pulvinar neque. Ornare arcu dui vivamus arcu felis. Adipiscing diam donec adipiscing tristique risus nec feugiat. Sit amet massa vitae tortor. Pharetra et ultrices neque ornare aenean euismod elementum. Urna nunc id cursus metus aliquam eleifend mi. Consectetur adipiscing elit ut aliquam purus sit amet. Nascetur ridiculus mus mauris vitae ultricies leo. Iaculis eu non diam phasellus vestibulum lorem sed risus. Faucibus nisl tincidunt eget nullam non nisi est sit. Auctor elit sed vulputate mi sit amet mauris commodo.

            Lacus viverra vitae congue eu consequat. Quis eleifend quam adipiscing vitae proin sagittis nisl. Magnis dis parturient montes nascetur ridiculus mus mauris. Nisi vitae suscipit tellus mauris a. Eros in cursus turpis massa tincidunt. Facilisi nullam vehicula ipsum a arcu cursus vitae congue. Massa sed elementum tempus egestas sed sed risus. Fringilla ut morbi tincidunt augue interdum velit euismod. Adipiscing tristique risus nec feugiat. Magna ac placerat vestibulum lectus. Erat imperdiet sed euismod nisi porta lorem mollis. Vitae congue mauris rhoncus aenean vel elit scelerisque mauris pellentesque. Sodales ut etiam sit amet nisl. Dictum at tempor commodo ullamcorper a lacus. Molestie a iaculis at erat pellentesque adipiscing commodo elit. Ut faucibus pulvinar elementum integer enim neque volutpat. Diam maecenas ultricies mi eget. Et tortor at risus viverra adipiscing.

            Quis hendrerit dolor magna eget est lorem ipsum dolor. Nunc sed blandit libero volutpat. Dignissim convallis aenean et tortor at risus viverra adipiscing. Feugiat nisl pretium fusce id. Duis at tellus at urna condimentum mattis. Sapien et ligula ullamcorper malesuada proin libero. Egestas tellus rutrum tellus pellentesque. Ut lectus arcu bibendum at varius. Enim ut tellus elementum sagittis vitae. Nisi porta lorem mollis aliquam. Egestas maecenas pharetra convallis posuere morbi leo urna. Eget mauris pharetra et ultrices neque ornare aenean euismod. Diam quam nulla porttitor massa id neque aliquam vestibulum. Blandit aliquam etiam erat velit. Sit amet tellus cras adipiscing. Scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis. Donec massa sapien faucibus et molestie ac. Habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper.

            Sodales ut etiam sit amet nisl purus in mollis nunc. Risus in hendrerit gravida rutrum quisque non tellus. Non arcu risus quis varius quam quisque id diam. Euismod lacinia at quis risus sed vulputate odio ut enim. Morbi non arcu risus quis varius quam quisque id. Vitae purus faucibus ornare suspendisse sed nisi. Ultricies integer quis auctor elit sed. Morbi leo urna molestie at elementum eu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Quisque non tellus orci ac. Faucibus ornare suspendisse sed nisi lacus sed viverra tellus in. Sagittis vitae et leo duis ut diam quam nulla. Nunc id cursus metus aliquam eleifend mi in nulla.
        '''
    },
    {
        'slug': 'programming-is-fun',
        'image': 'coding.jpg',
        'author': 'Maximilian',
        'date': date(2022, 3, 10),
        'title': 'Programming Is Great!',
        'excerpt': 'Did you ever spend hours searching that one error in your code? Yep - that\'s what happened to me yesterday...',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Convallis a cras semper auctor neque vitae tempus quam. Quisque id diam vel quam elementum. Adipiscing diam donec adipiscing tristique risus nec feugiat in. In vitae turpis massa sed. Facilisi cras fermentum odio eu feugiat pretium. Curabitur vitae nunc sed velit dignissim. Netus  et malesuada fames ac turpis egestas. Convallis aenean et tortor at risus viverra adipiscing at in. Feugiat scelerisque varius morbi enim nunc faucibus. Pellentesque massa placerat duis ultricies lacus sed.

            Sed adipiscing diam donec adipiscing tristique risus nec feugiat. Ac tortor vitae purus faucibus ornare suspendisse sed nisi. Id diam vel quam   elementum pulvinar etiam non quam. Mattis aliquam faucibus purus in massa tempor nec feugiat nisl. Suspendisse ultrices gravida dictum fusce ut placerat orci. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Integer feugiat scelerisque varius morbi enim nunc faucibus a pellentesque. Morbi blandit cursus risus at. Ac felis donec et odio pellentesque. Mauris in aliquam sem fringilla ut morbi tincidunt augue interdum. Diam vel quam elementum pulvinar. Posuere sollicitudin aliquam ultrices sagittis. Id semper risus in hendrerit gravida rutrum quisque non tellus. Velit ut tortor pretium viverra suspendisse. Quis eleifend quam adipiscing vitae proin sagittis. Eu mi bibendum neque egestas congue quisque egestas diam in.
        '''
    },
    {
        'slug': 'into-the-woods',
        'image': 'woods.jpg',
        'author': 'Maximilian',
        'date': date(2020, 8, 5),
        'title': 'Nature At Its Best',
        'excerpt': 'Nature is amazing! The amount of inspiration I get when walking in nature is incredible!',
        'content': '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet volutpat consequat mauris nunc congue nisi. Magna eget est lorem ipsum dolor sit amet. A scelerisque purus semper eget duis at tellus. Commodo elit at imperdiet dui accumsan sit amet nulla. Sit amet aliquam id diam maecenas ultricies mi eget. Nec nam aliquam sem et tortor consequat. Aliquet eget sit amet tellus cras adipiscing enim. Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin libero. Mattis vulputate enim nulla aliquet porttitor lacus luctus accumsan tortor. Id eu nisl nunc mi ipsum faucibus vitae aliquet nec. Elit ut aliquam purus sit amet luctus venenatis lectus magna. Fusce id velit ut tortor pretium viverra. Elit sed vulputate mi sit amet mauris commodo quis. Etiam dignissim diam quis enim. Blandit aliquam etiam erat velit scelerisque in dictum non. Interdum posuere lorem ipsum dolor sit amet. Sit amet nisl suscipit adipiscing bibendum est ultricies integer. Pharetra et ultrices neque ornare aenean.

            Morbi tristique senectus et netus et. Eget aliquet nibh praesent tristique magna sit amet. Neque gravida in fermentum et sollicitudin ac orci phasellus egestas. Aliquam purus sit amet luctus venenatis lectus. Purus gravida quis blandit turpis cursus in hac habitasse platea. Eu feugiat pretium nibh ipsum consequat nisl. Viverra aliquet eget sit amet tellus. Nec feugiat in fermentum posuere urna nec tincidunt praesent semper. Nec nam aliquam sem et. Justo laoreet sit amet cursus sit. Vitae suscipit tellus mauris a diam.

            Elementum facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Duis ut diam quam nulla porttitor. Hendrerit dolor magna eget est lorem ipsum dolor sit. Ipsum dolor sit amet consectetur adipiscing elit pellentesque habitant morbi. Lectus magna fringilla urna porttitor rhoncus dolor purus non enim. Consequat nisl vel pretium lectus quam id. Egestas diam in arcu cursus euismod quis. Sem fringilla ut morbi tincidunt augue interdum. At tellus at urna condimentum mattis. Vitae aliquet nec ullamcorper sit amet risus nullam eget felis. Dui accumsan sit amet nulla. Proin fermentum leo vel orci porta non pulvinar neque laoreet. Ipsum suspendisse ultrices gravida dictum fusce ut placerat orci nulla. Tempus iaculis urna id volutpat lacus laoreet non curabitur gravida.
        '''
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
