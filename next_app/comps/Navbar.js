import Link from 'next/link'
import React from 'react'

export default function Navbar() {
    return (
        <div className="left">
            <h1><Link href='/'>Home</Link></h1>
            <h1><Link href='/episodes'>Episodes</Link></h1>
            <h1><Link href='/episodes/filter'>Filter_Eps</Link></h1>
        </div>
    )
}