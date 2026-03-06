End To End Scenario Suite
===========================

//    | iteration |
//    | 1 |
//    | 2 |
//    | 3 |
//    | 4 |
//    | 5 |
//    | 6 |
//    | 7 |
//    | 8 |
//    | 9 |
//    | 10 |
//    | 11 |
//    | 12 |
//    | 13 |
//    | 14 |
//    | 15 |
//    | 16 |
//    | 17 |
//    | 18 |
//    | 19 |
//    | 20 |
//
//* Test iteration <iteration>
* Goto website with "https://automationexercise.com/"

End-to-End User Registration and Add Product to Cart
-----------------------------------------------------------
* Wait for home page navbar elements to visible
* Verify that the home page is displayed
* Click on the Sign Up button on the Home page

* Wait for signup page elements to load
* Enter user name and email on Sign Up page
* Click the Submit button

* Wait for signup from page elements to load
* Verify name and email on Sign Up Form page
* Fill required fields on Sign Up Form page
* Click Create Account button on Sign Up page

* Wait for Account Created page elements to load
* Click Continue button on Account Created page

* Verify logout delete account and logged user name on home page
* Wait for home page navbar elements to visible
* Click to Products on home page
* Goto website with "https://automationexercise.com/products"

* Wait for products page elements to visible
* Select random category on products page
* Select randon sub category on product page
* Verify selected sub category on products page
* Go random product detail page

* Wait for product detail page elements to visible
* Verify product detail page
* Enter random product quantity
* Click to Add To Cart button
* Verify product has been added to cart popup
* Direct to cart

* Wait for product cart page elements to visible
* Verify product has been added to cart page