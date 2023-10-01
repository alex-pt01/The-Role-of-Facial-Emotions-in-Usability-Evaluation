# Emotionality

This website aims to assist in evaluating the usability of a system. Allows the creation of projects, creation of teams, attribution of usability tests carried out with users to the project and visualization of results. It has the particularity of analyzing the impact that facial emotions have when using traditional usability evaluation methods such as cognitive walkthrough and usability smells. 
Images/model1_acc_loss.png

## Índice

- [User Testing Websites](#user-testing-websites)
  - [Functional requirements](#functional-requirements)


## User Testing Websites
To enhance the integration of strategic usability problems into a testable system, we've developed two websites, collectively named "TechIST," for buying and selling tech products. These sites, User Testing Website A and User Testing Website B, differ in usability design.

User Testing Website A was created without intentional usability problems, while User Testing Website B was intentionally designed with strategic usability issues. These websites serve as a controlled environment for user testing, enabling a detailed comparative analysis of user experiences and the effects of strategic usability problems on interactions and overall satisfaction.

### Functional requirements

## Functional Requirements

The functional requirements specified below are applicable to both User Testing Website A and User Testing Website B.

- **User Registration (REQ-1):**
  - The system should provide a registration feature that allows users to create an account by providing their first name, last name, email address, and a password that meets specific requirements such as minimum length and complexity. Additionally, the system should differentiate between team leaders and team members during the registration process.

- **User Authentication (REQ-2):**
  - The system must enable users to log in to their accounts using their username and password. The system should validate both the username and password entered by the user and display appropriate error messages if the login information is incorrect (e.g., incorrect email or password).

- **Update User Account (REQ-3):**
  - Users should have the ability to securely update their personal information within the system. This functionality should allow users to modify their first name, last name, username, email address, and current password.

- **Logout (REQ-4):**
  - The system must provide a secure logout feature that allows users to log out of their accounts when desired.

- **Products (REQ-5):**
  - **Search Functionality (REQ-5.1):**
    - The system should provide users with a search functionality that allows them to search for products using a search bar. Additionally, users should be able to filter search results based on price range, categories, products in stock, new or used items, items on sale, and the type of seller.

  - **Read Project Data (REQ-5.2):**
    - The system should offer a well-organized and easily searchable product catalog. This catalog should enable users to browse through available products, providing detailed product descriptions and options for purchase.

- **Shopping Cart (REQ-6):**
  - **Add Products to Cart (REQ-6.1):**
    - The system must include a cart system that allows users to add products to their shopping cart for future purchases.

  - **Update Shopping Cart (REQ-6.2):**
    - Users should have the ability to view and modify the contents of their shopping cart. They should be able to update quantities of items and remove products as needed.

  - **Check Out (REQ-6.3):**
    - The system must provide users with a checkout feature that allows them to proceed to the payment method once they have completed their shopping.

  - **Payment (REQ-6.4):**
    - The system should allow users to finalize their purchase by entering payment information, such as payment type, card number, card code, expiration month and year, and address.

  - **Payment Method Verification (REQ-6.5):**
    - The system must verify that the card number provided consists of sixteen digits and that the card code consists of three digits, ensuring the accuracy and security of the payment process.

  - **Purchase History (REQ-6.6):**
    - The system should provide users with access to their purchase history, allowing them to review information about all previous purchases made. This information should be easily accessible within the user's account area.

- **Review (REQ-7):**
  - **Add Website Reviews (REQ-7.1):**
    - The system should provide users with the ability to add reviews about the website. Users should be able to enter their username, user email, a description of their review, and a rating. This feature allows users to share their feedback and experiences with the website, contributing to the overall assessment and evaluation of its performance.








## Figure 1: MODEL 1
<img src="Images/model1_acc_loss.png" alt="Adaptation System Test 4" width="50%">
<img src="Images/model1_conf_matrix.png" alt="Adaptation System Test 5" width="50%">

## Figure 2: MODEL 2
<img src="Images/model2_acc_loss.png" alt="1x" width="50%">
<img src="Images/model2_conf_matrix.png" alt="Adaptation System Test 5" width="50%">

## Figure 3: MODEL 4
<img src="Images/model4_acc_loss.png" alt="Adaptation System Test 4" width="50%">
<img src="Images/model4_conf_matrix.png" alt="Adaptation System Test 5" width="50%">

## Figure 4: MODEL 5
<img src="Images/model5_acc_loss.png" alt="Adaptation System Test 4" width="50%">
<img src="Images/model5_conf_matrix.png" alt="Adaptation System Test 5" width="50%">

## Figure 5: MODEL 6
<img src="Images/model6_acc_loss.png" alt="Adaptation System Test 4" width="50%">
<img src="Images/model6_conf_matrix.png" alt="Adaptation System Test 5" width="50%">

## Figure 6: Relational database model of the user testing website
<img src="Images/website_test_BD.png" alt="Relational database model of the user testing website" width="50%">

## Figure 7: Website Test Navbar
<img src="Images/USER_TESTING/user_testing_navbar.png" alt="Navbar" width="50%">
<img src="Images/USER_TESTING/user_testing_navbar_pos_login.png" alt="Navbar after login" width="50%">

## Figure 8: User Testing Website Signup
<img src="Images/USER_TESTING/UTW_signup.png" alt="User Testing Website Signup" width="50%">

## Figure 9: User Testing Website Signin
<img src="Images/USER_TESTING/UTW_signin.png" alt="User Testing Website Signin" width="50%">

## Figure 10: User Testing Website Account Update (Type A)
<img src="Images/USER_TESTING/UTW_account.png" alt="User Testing Website Account Update (Type A)" width="50%">

## Figure 11: User Testing Website Account Update (Type B)
<img src="Images/USER_TESTING/UTW_US_account.png" alt="User Testing Website Account Update (Type B)" width="50%">

## Figure 12: Search for Products (Type A and B)
<img src="Images/USER_TESTING/UTW_search.png" alt="Search for Products" width="50%">

## Figure 13: Search for Products by Various Criteria (Type A and B)
<img src="Images/USER_TESTING/UTW_search_.png" alt="Search for Products by Various Criteria" width="50%">

## Figure 14: Incomplete Product Search (Type B)
<img src="Images/USER_TESTING/UTW_US_search.png" alt="Incomplete Product Search (Type B)" width="50%">

## Figure 15: Add Product to Cart (Type A and B)
<img src="Images/USER_TESTING/UTW_add_prod_cart.png" alt="Add Product to Cart (Type A and B)" width="50%">

## Figure 16: Product Purchase Checkout (Type A and B)
<img src="Images/USER_TESTING/shoppingCart_check_out.png" alt="Product Purchase Checkout (Type A and B)" width="50%">

## Figure 17: Payment Information (Type A and B)
<img src="Images/USER_TESTING/payment.png" alt="Payment Information (Type A and B)" width="50%">

## Figure 18: Payment Method Verification (Type A and B)
<img src="Images/USER_TESTING/payment_verification.png" alt="Payment Method Verification (Type A and B)" width="50%">

## Figure 19: User Testing Website Review (Type A)
<img src="Images/USER_TESTING/UTW_review.png" alt="User Testing Website Review (Type A)" width="50%">

## Figure 20: User Testing Website Review (Type B)
<img src="Images/USER_TESTING/review_UP.png" alt="User Testing Website Review (Type B)" width="50%">

## Figure 21: Usability Problem on User Testing Website B Review
<img src="Images/USER_TESTING/UTW_US_logout.png" alt="Usability Problem on User Testing Website B Review" width="50%">

## Figure 22: Relational Database Model of the Final Website
<img src="Images/CONCLUSIONS_WEBSITE/BD_FINAL.png" alt="Relational Database Model of the Final Website" width="50%">

## Figure 23: Navbar Before Team Leader Login
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_navbar.png" alt="Navbar Before Team Leader Login" width="50%">
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_navbar_less.png" alt="Navbar After Team Leader Login" width="50%">

## Figure 24: Team Leader Signup
<img src="Images/CONCLUSIONS_WEBSITE/TL/signup.png" alt="Team Leader Signup" width="50%">

## Figure 25: Team Leader Signin
<img src="Images/CONCLUSIONS_WEBSITE/TL/login.png" alt="Team Leader Signin" width="50%">

## Figure 26: Team Leader Account Update
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_account.png" alt="Team Leader Account Update" width="50%">

## Figure 27: Project Update
<img src="Images/CONCLUSIONS_WEBSITE/TL/project_edit.png" alt="Project Update" width="50%">

## Figure 28: Project Creation
<img src="Images/CONCLUSIONS_WEBSITE/TL/project_create.png" alt="Project Creation" width="50%">

## Figure 29: Project Management
<img src="Images/CONCLUSIONS_WEBSITE/TL/projects.png" alt="Project Management" width="50%">

## Figure 30: Usability Test Upload
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_test_upload.png" alt="Usability Test Upload" width="50%">

## Figure 31: Usability Tests
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_tests.png" alt="Usability Tests" width="50%">

## Figure 32: Update Usability Test Video
<img src="Images/CONCLUSIONS_WEBSITE/TL/update_video.png" alt="Update Usability Test Video" width="50%">

## Figure 33: Split Usability Test into Tasks
<img src="Images/CONCLUSIONS_WEBSITE/TL/split_video_tasks.png" alt="Split Usability Test into Tasks" width="50%">

## Figure 34: Upload Usability Test Task
<img src="Images/CONCLUSIONS_WEBSITE/TL/edit_task.png" alt="Upload Usability Test Task" width="50%">

## Figure 35: Delete Usability Test Task
<img src="Images/CONCLUSIONS_WEBSITE/TL/tasks.png" alt="Delete Usability Test Task" width="50%">

## Figure 36: Usability Smells
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_smells.png" alt="Usability Smells" width="50%">

## Figure 37: Create Usability Smell
<img src="Images/CONCLUSIONS_WEBSITE/TL/create_usability_smell.png" alt="Create Usability Smell" width="50%">

## Figure 38: Edit Usability Smell
<img src="Images/CONCLUSIONS_WEBSITE/TL/edit_usability_smell.png" alt="Edit Usability Smell" width="50%">

## Figure 39: Project Invitations
<img src="Images/CONCLUSIONS_WEBSITE/TL/invitations.png" alt="Project Invitations" width="50%">

## Figure 40: Create Project Invitation
<img src="Images/CONCLUSIONS_WEBSITE/TL/create_invitation.png" alt="Create Project Invitation" width="50%">

## Figure 41: Managing Permissions for Results Consolidation
<img src="Images/CONCLUSIONS_WEBSITE/TL/permissions_results_cons.png" alt="Managing Permissions for Results Consolidation" width="50%">

## Figure 42: Viewing Team Members' Work Progress
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_cons_progress.png" alt="Viewing Team Members' Work Progress" width="50%">

## Figure 43: Usability Tests Results (Team Members)
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_consolidation.png" alt="Usability Tests Results (Team Members)" width="50%">

## Figure 44: Cumulative Frequency of Facial Emotions
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_cfd.png" alt="Cumulative Frequency of Facial Emotions" width="50%">

## Figure 45: Error Rate
<img src="Images/CONCLUSIONS_WEBSITE/TL/error_rate.png" alt="Error Rate" width="50%">

## Figure 46: Average Task Completion Time
<img src="Images/CONCLUSIONS_WEBSITE/TL/avg_task_time.png" alt="Average Task Completion Time" width="50%">

## Figure 47: Satisfaction Rate
<img src="Images/CONCLUSIONS_WEBSITE/TL/satisfaction_rate.png" alt="Satisfaction Rate" width="50%">

## Figure 48: Website Usability Survey
<img src="Images/CONCLUSIONS_WEBSITE/TL/survey.png" alt="Website Usability Survey" width="50%">

## Figure 49: Usability Test Analysis
<img src="Images/CONCLUSIONS_WEBSITE/TL/test_analysis.png" alt="Usability Test Analysis" width="50%">

## Figure 50: Export Usability Test Results
<img src="Images/CONCLUSIONS_WEBSITE/TL/export_results.png" alt="Export Usability Test Results" width="50%">

## Figure 51: Export Error Rate Results
<img src="Images/CONCLUSIONS_WEBSITE/TL/export_error_rate.png" alt="Export Error Rate Results" width="50%">

## Figure 52: Export Task Completion Time Results
<img src="Images/CONCLUSIONS_WEBSITE/TL/export_task_time.png" alt="Export Task Completion Time Results" width="50%">

## Figure 53: Export Satisfaction Rate Results
<img src="Images/CONCLUSIONS_WEBSITE/TL/export_satisfaction_rate.png" alt="Export Satisfaction Rate Results" width="50%">

## Figure 54: Export Cumulative Frequency of Facial Emotions
<img src="Images/CONCLUSIONS_WEBSITE/TL/export_cfd.png" alt="Export Cumulative Frequency of Facial Emotions" width="50%">

## Figure 55: Closing the Session
<img src="Images/CONCLUSIONS_WEBSITE/TL/closing_session.png" alt="Closing the Session" width="50%">
