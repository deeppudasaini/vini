import React from 'react'
import Header from '../components/Header'
import Navigation from '../components/Navigation'
import Footer from '../components/Footer'
import OnlineRegister from '../components/OnlineRegister'
import TopSeller from '../components/TopSeller'
import Collection from '../components/Collection'
import New from '../components/New'

export default function Home() {
    return (
        <div>
        <Header />
        <Navigation />
        <Collection />
        <New />  
        <TopSeller />
        <OnlineRegister />
        <Footer />
      </div>
    )
}
