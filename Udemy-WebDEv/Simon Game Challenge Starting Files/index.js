color = ["red","green","blue","yellow"]
userInput = []
compInput = []
level = 0
gameIsOn = false

$(document).on("keypress",function(){
    compPlay()
    gameIsOn = true
})


function compPlay(){
    userInput = []
    level++
    $("h1").text("Level"+ " " +level)
    let s = setInterval(function(){
        let random = Math.floor(Math.random()*4)
        $(`#${color[random]}`).fadeIn(100).fadeOut(100).fadeIn(100)
        sound(color[random])
        animation(color[random])
        compInput.push(color[random])
        if (compInput.length==level){
            clearInterval(s)
        }
    },1000)
}


$(".btn").on("click",function(){
    sound($(this).attr("id"))
    animation(this)
    if (gameIsOn){
    userInput.push($(this).attr("id"))
    check(userInput.length-1)
    }
})

function check(lvl){
    if (userInput[lvl]===compInput[lvl]){
        if (userInput.length == compInput.length){
            setTimeout(function(){
                compPlay()
                compInput=[]
            },1000)
        }
    }
    else{
        sound("wrong")
        $("body").addClass("game-over")
        $("h1").text("Game Over, Press any key to restart")

        setTimeout(function(){
            $("body").removeClass("game-over")
        },200)

        startOver()
    }
}


function sound(clck){
    let audio = new Audio(`sounds/${clck}.mp3`)
    audio.play()
}


function animation(colr){
    $(colr).addClass("pressed")

    setTimeout(function(){
        $(colr).removeClass("pressed")
    },200)
}

function startOver(){
    compInput = []
    level = 0
    gameIsOn = false
}
