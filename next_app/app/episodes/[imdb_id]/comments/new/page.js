
"use client"

import Head from "next/head";
import { useState } from "react";
import { useParams, usePathname } from 'next/navigation'
import { backendURL } from '../../../../../utils/url'
import Link from 'next/link'

export default function Test({ params, searchParams }) {
  const [comment, setComment] = useState({
    comment: ""
  });
  const [result, setResult] = useState()

  const ep_id = searchParams?.imdb_id != undefined ? searchParams?.imdb_id : params?.imdb_id

  const onSubmit = async (e) => {
    e.preventDefault();
    if (comment.comment === "")
      return alert("comment is empty");


    const query = new URLSearchParams(comment).toString();

    await fetch(backendURL + '/api/comments/' + ep_id + "?" + query, {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      }
    }).then(data => {

        setResult(data)
        //const sleep = ms => new Promise(r => setTimeout(r, ms));
        //await sleep(5000)
        alert("comment created!")
      })
  };
  return (
    <div className="centered">
      <Head>
        <title> New Comment Submit Form</title>
      </Head>

      <form
        onSubmit={onSubmit}
        className="w-1/3 justify-center border-2 flex flex-col gap-4 m-4 p-2"

      >
        <label htmlFor="Episode ID">Episode ID</label>
        <input
          className="border-2 border-gray-200  p-2"
          value={ep_id}
          readOnly
        ></input>

        <label htmlFor="Comment">Comment:</label>
        <input
          className="border-2 border-gray-200  p-2"
          onChange={() => {
            setComment({ ...comment, comment: event.target.value });
          }}
        ></input>

        <button
          className="bg-black text-white text-sm font-medium p-2 rounded "
          type="submit"
        >
          <>Submit</>
        </button>
      </form>
      <div className="p-2">{result ? 'Result : ' + result : ''}</div>
      <div>
        <nav>
          <Link href={"/episodes/" + ep_id + "/comments/"}>
            ________________
            return to previous page
            ________________
          </Link>
        </nav>
      </div>
    </div>
  );
}