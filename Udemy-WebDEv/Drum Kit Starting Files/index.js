let a = document.querySelectorAll('button')
for (i = 0; i < a.length; i++) {
    a[i].addEventListener('click', handleClick)
}

function handleClick() {
    makeSound(this.innerHTML)
    buttonAnimation(this.innerHTML)
}

document.addEventListener('keypress', function (event) {
    makeSound(event.key)
    buttonAnimation(event.key)
})

function makeSound(key) {
    switch (key) {
        case "w":
            let crash = new Audio("sounds/crash.mp3")
            crash.play()
            break;

        case "a":
            let bass = new Audio("sounds/kick-bass.mp3")
            bass.play()
            break;

        case "s":
            let snare = new Audio("sounds/snare.mp3")
            snare.play()
            break;

        case "d":
            let tom1 = new Audio("sounds/tom-1.mp3")
            tom1.play()
            break;

        case "j":
            let tom2 = new Audio("sounds/tom-2.mp3")
            tom2.play()
            break;

        case "k":
            let tom3 = new Audio("sounds/tom-3.mp3")
            tom3.play()
            break;

        case "l":
            let tom4 = new Audio("sounds/tom-4.mp3")
            tom4.play()
            break;

        default:
            console.log(b)
            break;
    }
}

function buttonAnimation(keyPress){
    activeButton = document.querySelector('.'+keyPress)
    activeButton.classList.add("pressed")
    setTimeout(function (){activeButton.classList.remove("pressed")},100)
}

