import React from "react";

import useAuth from "../../hooks/useAuth";
import axios from "axios";




const Comments = (props) => {
  const [user, token] = useAuth();

  async function createComments(comments){
    try{
        await axios.get(
        'http://127.0.0.1:8000/api/slopelopedia/comment/'
        );

      }
  }


  async function handleLikes(comment_id) {
    try {
      await axios.patch(
        `http://127.0.0.1:8000/api/slopelopedia/${comment_id}/likes/`
      );
      props.get_all_comments_list();
    } catch (error) {
      console.log(token);
      console.log(error.message);
    }
  }
  async function handleDislikes(comment_id) {
    try {
      await axios.patch(
        `http://127.0.0.1:8000/api/slopelopedia/${comment_id}/dislikes/`
      );
      props.get_all_comments_list();
    } catch (error) {
      console.log(token);
      console.log(error.message);
    }
  }
  return (
    <div>
      {props.comments.map((el) => {
      
  );
};

export default Comments;