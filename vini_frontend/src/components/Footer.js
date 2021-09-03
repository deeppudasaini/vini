import React from 'react'

export default function Footer() {
    return (
        <div>
               <footer id="footer">
          {/* top footer */}
          <div className="section">
            {/* container */}
            <div className="container">
              {/* row */}
              <div className="row">
                <div className="col-md-3 col-xs-6">
                  <div className="footer">
                    <h3 className="footer-title">About Us</h3>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut.</p>
                    <ul className="footer-links">
                      <li><a><i className="fa fa-map-marker" />1734 Stonecoal Road</a></li>
                      <li><a><i className="fa fa-phone" />+021-95-51-84</a></li>
                      <li><a><i className="fa fa-envelope-o" />email@email.com</a></li>
                    </ul>
                  </div>
                </div>
                <div className="col-md-3 col-xs-6">
                  <div className="footer">
                    <h3 className="footer-title">Categories</h3>
                    <ul className="footer-links">
                      <li><a>Hot deals</a></li>
                      <li><a>Laptops</a></li>
                      <li><a>Smartphones</a></li>
                      <li><a>Cameras</a></li>
                      <li><a>Accessories</a></li>
                    </ul>
                  </div>
                </div>
                <div className="clearfix visible-xs" />
                <div className="col-md-3 col-xs-6">
                  <div className="footer">
                    <h3 className="footer-title">Information</h3>
                    <ul className="footer-links">
                      <li><a>About Us</a></li>
                      <li><a>Contact Us</a></li>
                      <li><a>Privacy Policy</a></li>
                      <li><a>Orders and Returns</a></li>
                      <li><a>Terms &amp; Conditions</a></li>
                    </ul>
                  </div>
                </div>
                <div className="col-md-3 col-xs-6">
                  <div className="footer">
                    <h3 className="footer-title">Service</h3>
                    <ul className="footer-links">
                      <li><a>My Account</a></li>
                      <li><a>View Cart</a></li>
                      <li><a>Wishlist</a></li>
                      <li><a>Track My Order</a></li>
                      <li><a>Help</a></li>
                    </ul>
                  </div>
                </div>
              </div>
     
            </div>
     
          </div>
     
          
        </footer>
        </div>
    )
}
