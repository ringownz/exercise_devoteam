"use client"

import { React} from 'react'
import {backendURL} from '../../../../utils/url'
import {useSearchParams, useRouter} from 'next/navigation'
import { useState } from "react";

/*import dynamic from 'next/dynamic'



const NoSSRComponent = dynamic(() => import("./delete"), {
    ssr: false,
  });
*/

const isServer = () => typeof window === 'undefined';


const DeleteComponent = ({params}) => {

    /*
    const deleteComment = async (comment_id) => {
        if (comment_id != undefined || null) {
    
            
    
            await fetch(backendURL+'/api/comments/id/' + comment_id, {
                method: "POST",
                mode: "no-cors",
                headers: {
                  "Content-Type": "application/json",
                }
              }).then((res) => res.json());
            const router = useRouter();
    
            //this will reload the page without doing SSR
            router.refresh();
            alert("comment deleted!!")
        }
        return true;
    }

*/
    //const searchParams = useSearchParams()
    //const com_id = searchParams.get("comment")//.get("id")
    const com_id = params.comment

    const [comment_id] = useState(params.comment)

    console.log("id parms test ... " + com_id) //Loads on Begin
    const handleDelete = async (e) => {

        //Only inside when it's submited
        e.preventDefault();
        console.log("......... going to delete id: " + comment_id + ".........")
        
        if (comment_id != undefined || null) {
    
            const result = await fetch(backendURL+'/api/comments/id/' + comment_id, {
                method: "DELETE",
                //mode: "no-cors",
                headers: {
                  "Content-Type": "application/json",
                }
            }).then((res) => {
                res.json()
                //console.log("res status ==" + res.status)
                return res
            }    
            );
            //console.log("result status ==" + result.status)
            
            if(result.status == 200){
                if(!alert("comment deleted!!")) {
                    //If confirms alert
                    window.location.reload()
                }
            } else { 
                if(!alert("something went wrong!!")) {
                    //If confirms alert
                    window.location.reload()
                }
            }
        }
        
    }

    return (
        <div>
            <form onSubmit={handleDelete}>
              <button type="submit" className='btn btn-primary'>..Delete..</button>
            </form>
        </div>
    )
}

export default DeleteComponent