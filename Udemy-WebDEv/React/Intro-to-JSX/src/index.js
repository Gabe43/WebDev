import React from "react"
import reactDom from "react-dom"
import ReactDOM from "react-dom"
// import Heading from "./heading"
// import List from "./list"
import App from "./app"
import { Add, Minus, Multiply, Divide } from "./calculator"


// ReactDOM.render(What to Show, Where to show)



const name = "Saptarshi"

ReactDOM.render(<h1>Hello {name}!</h1>, document.getElementById("root"))

/* ----------- Practice ------------ */

// ReactDOM.render(
//     <div>
//         <h1 className="heading" contentEditable="true" spellCheck="false">This is a Practice</h1>
//         <div>
//             <img src="https://th.bing.com/th/id/OIP.O5ko5GRHxIz07za1nkroDgHaFj?pid=ImgDet&rs=1"></img>
//             <img src="https://th.bing.com/th/id/R.64a64dc09e799706cc2dd08613d8316c?rik=U%2bIBSH77fOyLhw&riu=http%3a%2f%2fwww.jopreetskitchen.com%2fwp-content%2fuploads%2f2020%2f07%2fDSC_7156.jpg&ehk=ylRijeQ%2f7DygOftpNd6mMHwbTtY7%2fZcbd592c2X41kM%3d&risl=&pid=ImgRaw&r=0"></img>
//             <img src="https://th.bing.com/th/id/OIP.Qo_gq80KJRzjIvimTz9wUwHaHa?pid=ImgDet&rs=1"></img>
//         </div>

//     </div>,
//     document.getElementById("root")
// )

/* ----------- END ------------ */


/* ----------- Practice 2 ------------ */

// const fname = "Saptarshi"
// const lname = "Nag"

// const dte = new Date()


// ReactDOM.render(
//     <div>
//         <p>Created by {fname + " " + lname}</p>
//         <p>Copyright {dte.getFullYear()}</p>
//     </div>,
//     document.getElementById("root")
// )

/* ----------- END ------------ */


/* ----------- Practice 2 ------------ */

/* Export function of the jsx */



// ReactDOM.render(
//     <div>
//         <App></App>
//     </div>,
//     document.getElementById("root")
// )

ReactDOM.render(
    <div>
        <ul>
            <li>{Add(4,5)}</li>
            <li>{Minus(5,3)}</li>
            <li>{Multiply(4,6)}</li>
            <li>{Divide(10,5)}</li>
        </ul>
    </div>,
    document.getElementById("root")
)






/* ----------- END ------------ */



// ReactDOM.render(
//         <div>
//             <Heading></Heading>
//             <List></List>
//         </div>,
//         document.getElementById("root")
//     )