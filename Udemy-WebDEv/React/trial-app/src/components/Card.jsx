import React from "react";
import Avatar from "./Avatar";
import Paragraph from "./Detail";

function Card(props) {
    return (
        <div className="card">
            <div className="top">
                <h2 className="name">{props.name}</h2>
                <Avatar image={props.image} />
            </div>
            <div className="bottom">
                <Paragraph number={props.number} mail={props.mail} />
            </div>
        </div>
    )
}

export default Card