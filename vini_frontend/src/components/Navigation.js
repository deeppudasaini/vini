import React,{useState,useEffect} from 'react'
import axios from '../request/axios'
export default function Navigation() {
const [categories,setCategory]=useState([])
useEffect(()=>{
    async function getCategory(){
        const response=await axios.get('/category')
        setCategory(response.data)
        console.log(response.data)
        return response
    }
    getCategory();
},['/category']);
    
    return (
        <div>
               <nav id="navigation">
        
          <div className="container">
        
            <div id="responsive-nav">
              
              <ul className="main-nav nav navbar-nav">
              {categories.map((category) => (
            <li><a>{category.name}</a></li>
        ))}
              
              </ul>
              
            </div>
            
          </div>
          
        </nav>
        </div>
    )
}
