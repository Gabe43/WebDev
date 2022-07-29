import React from "react"
import ReactDOM from "react-dom"


function Heading(greet, colr){
    return ReactDOM.render(<h1 style={{ color: colr }}>{greet}</h1>, document.getElementById("root"))
}


export default Heading