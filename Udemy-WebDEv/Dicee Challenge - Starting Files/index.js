
let arr = ["images/dice1.png", "images/dice2.png", "images/dice3.png", "images/dice4.png", "images/dice5.png", "images/dice6.png"]
let a = Math.floor(Math.random() * 6)
let b = Math.floor(Math.random() * 6)
document.querySelector('.img1').setAttribute("src", arr[a])
document.querySelector('.img2').setAttribute("src", arr[b])
if (a > b) {
    // document.querySelector('h1').innerHtml = "Player 1 Wins!"
    document.getElementById('change').innerHTML = "Player 1 Wins!"
}
else if (a == b) {
    document.getElementById('change').innerHTML = "It's A Draw!"
}
else {
    document.getElementById('change').innerHTML = "Player 2 Wins!"
}

window.onload()