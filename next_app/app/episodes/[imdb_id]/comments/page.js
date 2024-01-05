// Get all comments for specific episode

import { use, React} from 'react'
import Link from 'next/link'
import {backendURL} from '../../../../utils/url'
import DeleteComponent from './delete';

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";


async function getData(ep_id) {
  
  return await fetch(backendURL+'/api/comments/all/' + ep_id, {
    cache: "no-store"
  })
  .then((res) => res.json());
  
}

const page = ({params,searchParams}) => {

  console.log("params= " + params?.imdb_id)
  console.log("searchParams= " + searchParams?.imdb_id)
  const ep_id = searchParams?.imdb_id != undefined ? searchParams?.imdb_id : params?.imdb_id

  const data = use(getData(ep_id))



  return (
    <div className="centered">
      {data.list_all_comments?.map(
          (comment) => 
          <div key={comment.id}>
            <h1>C: {comment.comment}</h1>

            <nav>
            <Link href={{
              pathname:"/episodes/"+ data.episode + "/comments/" + comment.id,
              query:{
                comment: comment.comment
              }
            }}>
             -- Update --
            </Link></nav>
             <DeleteComponent params={{comment:comment.id}}/>
            
            

            <p>--------------</p>
          </div>
          )}


        <nav>
          <Link href={"/episodes/"+ data.episode + "/comments/new"}>
          ________________
          Add new comment!
          ________________
          </Link>
        </nav>

    </div>

  )
}

export default page