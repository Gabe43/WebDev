import React from "react"

function Heading() {
  return <div className="heading">
    <h1>To-Do List</h1>
  </div>
}

function Listitem(props) {
  return <li onClick={function (){
    props.onChecked(props.id)
  }}>{props.text}</li>
}


export { Heading, Listitem }