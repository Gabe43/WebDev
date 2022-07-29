import React from "react"

function Ret(props) {
  return (
      <div className="term">
        <dt>
          <span className="emoji" role="img" aria-label="Tense Biceps">
            {props.emoji}
          </span>
          <span>{props.title}</span>
        </dt>
        <dd>
          {props.body}
        </dd>
      </div>
  )
}


export default Ret