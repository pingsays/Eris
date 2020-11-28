import React, { useState, useEffect } from "react";
import io from "socket.io-client";

let endPoint = "/";
let socket = io.connect(`${endPoint}`);

const App = () => {
  const [messages, setMessages] = useState(["Hello And Welcome"]);
  const [message_sent, setMessageSent] = useState("");
  //const [gameInfo, setGameInfo] = useState()

  useEffect( () => {
    socket.on("message", msg => {
      setMessages([...messages, msg]);
    });
  });

  // On Change
  const onChange = e => {
    setMessageSent(e.target.value);
  };


  const submitMessage = () => {
    if (message_sent !== "") {
      socket.emit("new_message", message_sent);
      setMessageSent("");
    } else {
      alert("Please Add A Message");
    }
  }

  // On Click
  const onClick = () => {
    submitMessage()
  };

  const OnEnter = (event) => {
      if (event.key === 'Enter') {
        submitMessage()
    }
  }

  const startGame = () => {
    //setGameInfo(socket.emit("play"));
  };



  return (

    <div>
      <p>Hello, Welcome to Eris</p>
      <p>Please press play to start game</p>
      <button onClick={() =>startGame()}>Play</button>
      {/* <p>{gameInfo.game_status}</p> */}



      {messages.length > 0 &&
        messages.map(msg => (
          <div>
            <p>{msg}</p>
          </div>
        ))}
      <input value={message_sent} name="message" onChange={e => onChange(e)}  onKeyDown={e => OnEnter(e)}/>
      <button onClick={() => onClick()}>Send Message</button>
    </div>
  );
};

export default App;