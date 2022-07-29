import React from "react";
import emojipedia from "../emojipedia";
import Ret from "./Emoji";


function App() {
  return <div>
    <h1>
      <span>emojipedia</span>
    </h1>
    <dl className="dictionary">
      {
        emojipedia.map(emojipedia => <Ret key={emojipedia.id} emoji={emojipedia.emoji} title={emojipedia.name} body={emojipedia.meaning} />)
      }
    </dl>
  </div>
}



export default App;
