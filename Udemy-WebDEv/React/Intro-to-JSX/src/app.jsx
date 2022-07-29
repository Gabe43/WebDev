import Heading from "./heading"

function App(){
    let time = new Date().getHours()
    let greeting = ""
    let color = ""

    if (time >= 3 && time < 12) {
        greeting = "Good Morning"
        color = "red"
    }
    else if (time >= 12 && time < 18) {
        greeting = "Good Afternoon"
        color = "green"
    }
    else if (time >= 18 || time > 0) {
        greeting = "Good Night"
        color = "blue"
    }
    return Heading(greeting,color)
}

export default App