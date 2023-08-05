import React from 'react'
import Link from 'next/link'

export default function Navbar() {
  return (
    <>
    <div>navbar</div>
    <div className="flex flex-col">
        <Link href="/login" className="text-blue-500 hover:text-blue-700">
          Log In
        </Link>
        <Link href="/signup" className="text-blue-500 hover:text-blue-700">
          Sign Up
        </Link>
        </div>
    </>
  )
}
