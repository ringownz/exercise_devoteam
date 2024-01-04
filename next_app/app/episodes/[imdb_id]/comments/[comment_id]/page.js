//Update comment by ID
"use client"

import Head from "next/head";
import { useState } from "react";
import { useParams, usePathname, useSearchParams } from 'next/navigation'
import {backendURL} from '../../../../../utils/url'
import Link from 'next/link'

export default function Test({params}) {
  const [comment, setComment] = useState();
  const [result,setResult]= useState()
  const [episode, setEpisode] = useState(params.imdb_id)
  const [comment_id] =useState(params.comment_id)

  const searchParams = useSearchParams()
  const prevComment = searchParams.get('comment')

  console.log("TEST UPDATE COMMENT PREV ___=== > "+ prevComment)

  const onSubmit = async (e) => {
    e.preventDefault();
    if (comment.comment === "")
      return alert("comment is empty");

    
    const queryComment =  new URLSearchParams(comment).toString();
    const queryEpisode =  new URLSearchParams({episode_id: episode}).toString();

    await fetch(backendURL + '/api/comments/id/' + comment_id + "?" + queryEpisode + "&" + queryComment, {
        method: "POST",
        mode: "no-cors",
        headers: {
          "Content-Type": "application/json",
        }
      }).then(res=>{
        setResult( res.text())
       
        return alert("comment updated!")
      })
  };
  return (
    <div className="centered">
      <Head>
        <title> Update Comment Submit Form</title>
      </Head>

      <form
        onSubmit={onSubmit}
        className="w-1/3 justify-center border-2 flex flex-col gap-4 m-4 p-2"
     
      >
        <label htmlFor="Episode ID">Episode ID</label>
        <input
          className="border-2 border-gray-200  p-2"
          value={episode}
          readOnly
        ></input>

        <label htmlFor="Comment">Comment:</label>
        <input
          className="border-2 border-gray-200  p-2"
          defaultValue={prevComment}
          onChange={() => {
            setComment({ ...comment, comment: event.target.value });
          }}
        ></input>

        <button
          className="bg-black text-white text-sm font-medium p-2 rounded "
          type="submit"
        >
          <>Update!</>
        </button>
      </form>
      <div className="p-2">{result ? 'Result : '+ result:''}</div>
      <div>
          <nav>
            <Link href={"/episodes/"+ episode + "/comments/"}>
            ________________
            return to previous page
            ________________
            </Link>
          </nav>
        </div>
    </div>
  );
}