import React from "react"

function Paragraph(props){
    return (<div>
        <p className="info">{props.number}</p>
        <p className="info">{props.mail}</p>
    </div>)
}

export default Paragraph