import React from "react"

import styles from './body.module.css'

interface User {
    id: number;
    name: string;
    email: string;
    address: {street: string};
}

const LeftTrix = async () => {
    const res = await fetch('https://jsonplaceholder.typicode.com/users', {next: {revalidate: 10 }})
    const users: User[]= await res.json();
  return (
    <div className = {styles.leftTrix}>
        <ul>
        {users.map(user => <li key={user.id} >{user.address.street}</li>)}
      </ul>
    </div>
  )
};

export default LeftTrix;