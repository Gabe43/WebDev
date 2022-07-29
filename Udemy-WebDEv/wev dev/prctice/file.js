function change(x)
{
    var c = document.getElementsByClassName('dog')[0];
    var dog='https://gfp-2a3tnpzj.stackpathdns.com/wp-content/uploads/2018/06/dog-breeds-of-famous-dogs-1600x1065.jpg'
    var cat='https://th.bing.com/th/id/OIP.kwkc_7Yosj69YWbWlDQ-oAHaEo?pid=ImgDet&rs=1'
    if (x =='dog')
       c.src=dog
    else 
       c.src=cat
}