import React from "react"

interface User {
    id: number;
    name: string;
    email: string;
    address: {street: string};
}

const UsersPage = async () => {
   const res = await fetch('https://jsonplaceholder.typicode.com/users', {next: {revalidate: 10 }})
   const users: User[]= await res.json();


  return (
    <div>
      UsersPage
      <ul>
        {users.map(user => <li key={user.id} >{user.address.street}</li>)}
      </ul>
    </div>
  )
};

export default UsersPage;
