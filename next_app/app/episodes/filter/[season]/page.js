import React from 'react'
import {backendURL} from '../../../../utils/url'

async function getData(season) {
    let season_ext = ""
    if (season != "0") { 
        season_ext = "?season=" + season
    }

    const data = await fetch(backendURL+'/api/episodes/filter/' + season_ext, {
        cache: "no-cache"
    })
    .then((res) => res.json());
    return data;

}


const page = async ({params}) => {

  const season = params.season
  const data = await getData(season)

  return (
    <div className="center">
        {data.map(
          (ep) => 
            <div key={ep.imdb_id}>
                <h1>Season: {ep.season}</h1>
                <h1>Episode: {ep.episode}</h1>
                <h1>Title: {ep.title}</h1>
                <h1>Rating: {ep.imdb_rating}</h1>
                <h1>ID: {ep.imdb_id}</h1>
                <h1>-------------------</h1>
            </div>
        )}
    </div>
  )
}

export default page