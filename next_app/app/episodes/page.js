//show all episodes
import Link from 'next/link'
import {backendURL} from '../../utils/url'

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

async function getData() {
    try{
      const data = await fetch(backendURL+'/api/episodes/', {
        cache: "no-cache"
      })
      .then((res) => res.json());
      return data;
    }catch (error) {
      console.error(error);
      return {
        "imdb_id":"",
        "season":"",
        "episode":"",
        "imdb_rating":"",
        "title":""
      }
    }
  }

  const page = async () => {
    const data = await getData()
    return (
      <div className="center">
        {data.map(
          (data) => 
          <div key={data.imdb_id}>
            <h1>Season: {data.season}</h1>
            <h1>Episode: {data.episode}</h1>
            <h1>Title: {data.title}</h1>
            <h1>Rating: {data.imdb_rating}</h1>
            <h1>ID: {data.imdb_id}</h1>
            
            <nav>
              <Link href={"/episodes/"+data.imdb_id}>
              -----------  More details here!
              </Link>
            </nav>
          </div>
          )}
      </div>
      
    )
  }
  
  export default page