// $("h1").addClass("big-title") Adding class

// $("h1").text/html("Hey") Manipulating text with jquery

// $('img').attr("src","www.google.com") setting one value to get attribute and two value to set attribute

// $("h1").click(function(){
//     $("h1").css("color",'purple') Adding eventlisteners 
// })

// $("input").keypress(function(event){ For keypress
//     $("h1").text(event.key)
// })

// $("h1").on("click",function(){ Alternative of keypress or click
//     $("h1").css("color","red")
// })

// $("h1").before/after("<button>Click</button>") To create a html element before or after any specific element

// $("h1").prepend/append("<button>Click</button>") To create html inside of the selected html before or after the inner html

// $("button").remove() To remove any element

// $("button").on("click",function () { USing animation using jquery
//     $("h1").hide()/show()/toggle()/fadeOut/fadeIn()/fadeToggle()/slideUp()/slideDown()/slideToggle() using toggle means that if the h1 is hidden it will be visible and if its visible will be hidden
// $("h1").animate({opacity:0.5}) we can use css designs using animation, we can only use numeric value things
// $("h1").slideUp().slideDown().animate({opacity:0.5}) We can used as many as methods together
// })