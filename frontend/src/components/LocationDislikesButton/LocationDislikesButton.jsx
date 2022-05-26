import React, { useState } from "react";
import cn from "classnames";
import { ReactComponent as Hand } from "./hand.svg";
import "./LocationDisLikesButton.css";
import "./styles.scss";

const DisLikeButton = () => {
  const [Disliked, setDisLiked] = useState(null);
  const [clicked, setClicked] = useState(false);

  return (
    <button
      onClick={() => {
        setDisLiked(!Disliked);
        setClicked(true);
      }}
      onAnimationEnd={() => setClicked(false)}
      className={cn("like-button-wrapper", {
        Disliked,
        clicked,
      })}
    >
      <div className="like-button">
        <Hand />
        <span>Like</span>
        <span className={cn("suffix", { Disliked })}>d</span>
      </div>
    </button>
  );
};

export default DisLikeButton;