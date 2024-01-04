// get episode info
import React from 'react'
import Link from 'next/link'
import {backendURL} from '../../../utils/url'

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

async function getData(ep_id) {

  const data = await fetch(backendURL+'/api/episodes/' + ep_id, {
    cache: "no-cache"
  })
  .then((res) => res.json());
  return data;

}


const page = async ({params}) => {

  const ep_id = params.imdb_id
  const data = await getData(ep_id)
  console.log(data)

  return (
    <div className="center">
      <h1>Season: {data.season}</h1>
      <h1>Episode: {data.episode}</h1>
      <h1>Title: {data.title}</h1>
      <h1>Rating: {data.imdb_rating}</h1>
      <h1>ID: {data.imdb_id}</h1>

      <div>
        <nav>
          <Link href={"/episodes/"+ data.imdb_id + "/comments"}>
            -- View comments --
          </Link>
        </nav>
      </div>
    </div>
    
  )
}

export default page