# Emotionality

This website aims to assist in evaluating the usability of a system. Allows the creation of projects, creation of teams, attribution of usability tests carried out with users to the project and visualization of results. It has the particularity of analyzing the impact that facial emotions have when using traditional usability evaluation methods such as cognitive walkthrough and usability smells. 
Images/model1_acc_loss.png

## Indice
- [Facial Emotion Recognition Algorithm](#facial-emotion-recognition-algorithm)
- [User Testing Websites](#user-testing-websites)
  - [Functional requirements](#functional-requirements)
  - [Usability Smells](#usability-smells)
  - [Database description](#database-description)
  - [Examples](#examples)
- [The Emotionality Tool](#the-emotionality-tool)
  - [Emotinality functional requirements](#emotinality-functional-requirements)
    - [Common to All Stakeholders](#common-to-all-stakeholders)
    - [Team Leader Functional Requirements](#team-leader-functional-requirements)
    - [Team Member Functional Requirements](#team-member-functional-requirements)
  - [Emotinality non-functional requirements](#emotinality-non-functional-requirements)
  - [Emotionality database description](#emotionality-database-description)
  - [Stakeholders common views](#stakeholders-common-views)
  - [Team leader system functionalities](#team-leader-system-functionalities)
  - [Team member system functionalities](#team-leader-system-functionalities)

## Facial Emotion Recognition Algorithm

All models created are represented in the graphs below.

**Model 1**

<img src="Images/model1_acc_loss.png" alt="Accuracy of model 1." width="35%">
<img src="Images/model1_conf_matrix" alt="Loss of model 1." width="35%">

**Model 2**

<img src="Images/model2_acc_loss.png" alt="Accuracy of model 2." width="35%">
<img src="Images/model2_conf_matrix" alt="Loss of model 2." width="35%">

**Model 4**

<img src="Images/model4_acc_loss.png" alt="Accuracy of model 4." width="35%">
<img src="Images/model4_conf_matrix" alt="Loss of model 4." width="35%">

**Model 5**

<img src="Images/model5_acc_loss.png" alt="Accuracy of model 5." width="35%">
<img src="Images/model5_conf_matrix" alt="Loss of model 5." width="35%">

**Model 6**

<img src="Images/model6_acc_loss.png" alt="Accuracy of model 6." width="35%">
<img src="Images/model6_conf_matrix" alt="Loss of model 6." width="35%">



## User Testing Websites
To enhance the integration of strategic usability problems into a testable system, we've developed two websites, collectively named "TechIST," for buying and selling tech products. These sites, User Testing Website A and User Testing Website B differ in usability design. The development code for both websites can be found in the User Testing Websites folder in google drive.

User Testing Website A was created without intentional usability problems, while User Testing Website B was intentionally designed with strategic usability issues. These websites serve as a controlled environment for user testing, enabling a detailed comparative analysis of user experiences and the effects of strategic usability problems on interactions and overall satisfaction.

### Functional Requirements

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

### Usability Smells

The following list outlines the usability smells that were utilized for evaluation purposes:

- **No client validation:** This usability smell refers to the absence of validation checks on the client side when inputting data into forms. Without proper client validation, users may submit incorrect or incomplete information, leading to errors or difficulties down the line. For example, if a form does not validate email addresses or requires specific formats for certain inputs but does not provide feedback or error messages, users may encounter issues when submitting the form. 

- **Late validation:** refers to a usability smell where validation checks for user inputs or actions occur after a significant delay or at a later stage in the process. Instead of providing immediate feedback on errors or invalid inputs, the system waits until later in the user flow to validate the information. This can lead to confusion and frustration for users as they may not be aware of their mistakes until they have progressed further in the process.

- **Abandoned form:** This usability smell occurs when users start filling out a form but abandon it before completing the process. It suggests that users may encounter difficulties or frustrations while interacting with the form, leading to abandonment. Common reasons for abandoned forms include complex or confusing layouts, unclear instructions, excessive or irrelevant form fields, or technical issues. 

- **Go to wrong page/Misleading link:** This usability smell indicates situations where users are directed to the wrong page or misled by a link that does not accurately represent the content or destination. For example, clicking on a link that promises one thing but takes the user to an unrelated or unexpected page can cause confusion and disrupt the user's flow. Misleading links can lead to frustration and impact the user's trust in the website or application. 

- **Long-time request:** This usability smell refers to situations where user requests or actions take a long time to process or complete, causing delays and potential frustration. For example, if a page takes an excessively long time to load or a transaction processing request takes an extended period without any indication of progress, users may become impatient or assume that the system is unresponsive. 

- **Form field with short input:** This usability smell occurs when form fields restrict the length or format of user input without providing clear instructions or feedback. For instance, if a form field limits the number of characters that can be entered, but users are not informed about the limit or given real-time feedback, they may encounter issues when attempting to input their desired information. 

- **Search with few search results:** This usability smell refers to situations where a search form or function returns a limited or inadequate number of search results. Users expect search results to be relevant, comprehensive, and reflective of their query. If the search functionality consistently provides few or irrelevant results, users may experience frustration and difficulty in finding the information they need. 

- **Click action unresponsive element:** This usability smell occurs when users click on an element or perform an action, but the system or interface does not respond as expected or fails to provide feedback. Unresponsive elements can confuse users and give the impression that the system is unresponsive or malfunctioning. A lack of visual or interactive feedback can lead to uncertainty and affect the user's perception of the system's usability.

### Database description
The database consists of the following entities:

- **ShoppingCartItem:** This entity represents an item in the shopping cart. It includes an attribute for the quantity of the product and a reference to the Product model.

- **Product:** The Product model represents a technology product and includes attributes such as name, price, description, image, quantity, stock, brand, category, creation date, condition (new or used), and seller information. It is associated with the ShoppingCartItem template.

- **Promotion:** The Promotion template represents a product promotion and includes attributes like name, discount, description, and deadline. It is linked to the Product model.

- **Sold:** This model represents sold products and includes attributes for quantity, seller information, total amount, and the sale date. It has a reference to the Product model.

- **Comment:** The Comment model stores comments made by users on specific products. It includes attributes for description, rating, and the posting date. It is associated with the Product model.

- **PaymentMethod:** This model represents payment methods used to finalize product purchases. It includes attributes for card type and number.

- **ShoppingCart:** The ShoppingCart model contains the ID of the ShoppingCartItem model.

- **Payment:** The Payment model represents payment details, including address, total amount, available credits (if applicable), and payment date. It is associated with the PaymentMethod template.

These entities collectively form the structure of the system's database, facilitating the organization and management of data for the user testing website.

### Examples

**User Testing Website Navbar**

<img src="Images/USER_TESTING/user_testing_navbar.png" alt="User testing website navbar before the user has logged in." width="35%">
<img src="Images/USER_TESTING/user_testing_navbar_pos_login.png" alt="User testing website navbar after the user has logged in." width="35%">


**User Testing Website Signup**

<img src="Images/USER_TESTING/UTW_signup.png" alt="User testing website type A and B user register." width="35%">


**User Testing Website Signin**

<img src="Images/USER_TESTING/UTW_signin.png" alt="User testing website type A and B user authentication." width="35%">


**User Testing Website Account Update**

<img src="Images/USER_TESTING/UTW_account.png" alt="User testing website type A update account." width="35%">


**User Testing Website Type B Account Update**

<img src="Images/USER_TESTING/UTW_US_account.png" alt="User testing website type B update account." width="35%">


**Product Search on User Testing Website**

<img src="Images/USER_TESTING/UTW_search.png" alt="Search for products in the search bar on the User testing website type A and B." width="35%">


**Advanced Product Search on User Testing Website**

<img src="Images/USER_TESTING/UTW_search_.png" alt="Search for products by price range, categories, products in stock, new, used or in the promotion and by seller type in the User testing website type A and B." width="35%">


**Incomplete Product Search on User Testing Website Type B**

<img src="Images/USER_TESTING/UTW_US_search.png" alt="Incomplete product search on User testing website type B." width="35%">


**Add Product to Cart**

<img src="Images/USER_TESTING/UTW_add_prod_cart.png" alt="Option to add the product to cart on the User testing website type A and B." width="35%">


**Perform Product Purchase Checkout**

<img src="Images/USER_TESTING/shoppingCart_check_out.png" alt="Performing product purchase checkout on the User testing website type A and B." width="35%">


**Fill in Payment Details**

<img src="Images/USER_TESTING/payment.png" alt="Filling in the data required to pay for the purchase on the User testing website type A and B." width="35%">


**Payment Method Verification**

<img src="Images/USER_TESTING/payment_verification.png" alt="Payment method verification on the User testing website type A and B." width="35%">


**Fill out a Review on the User Testing Website**

<img src="Images/USER_TESTING/UTW_review.png" alt="Form for filling out a user testing website type A and B review." width="35%">


**Fill out a Review on User Testing Website Type A**

<img src="Images/USER_TESTING/UTW_review.png" alt="Form for filling out a user testing website type A review." width="35%">


**Fill out a Review on User Testing Website Type B**

<img src="Images/USER_TESTING/review_UP.png" alt="Form for filling out a user testing website type B review." width="35%">


**Go to Wrong Page/Misleading Link" Issue on User Testing Website Type B**

<img src="Images/USER_TESTING/UTW_US_logout.png" alt="Go to wrong page/Misleading link” usability problem on user testing website B review." width="35%">


## The Emotionality Tool

The Emotionality Tool was developed to address the absence of a comprehensive and freely available system for evaluating the usability of user testing websites, aligning with the objectives of this master's thesis focused on investigating the role of facial emotions in usability assessment. This tool offers functionalities for loading, storing, and extracting insights from pairs of videos recorded during usability tests. These video pairs include a webcam recording capturing the user's facial expressions and a monitor recording capturing the user's interactions with the target system. This dissertation provides a thorough exploration of the stakeholders, requirements, architecture, and potential of "The Emotionality Tool" system in fulfilling its intended purpose.

### Emotinality functional requirements

#### Common to All Stakeholders

- **User Registration (REQ-1):** The system must provide a user registration feature where users can create an account by providing their first name, last name, email address, and a password that meets specified requirements. The registration process should differentiate between team leaders and team members.
- **User Authentication (REQ-2):** The system should enable users to log in using their registered username (email) and password. The system must validate the provided credentials and display appropriate error messages if the login information is incorrect, such as an invalid email or password.
- **Update User Account (REQ-3):** The system should provide users with the capability to update their personal data securely. This feature allows users to modify their account information, such as name, email address, or password.
- **Logout (REQ-4):** The system must include a secure logout functionality that allows users to log out from their accounts when needed.

#### Team Leader Functional Requirements

- **Project Management (REQ-6)**
  - **Create Project Data (REQ-6.1):** The system must allow for the creation of new projects by defining their name, description, start date, and end date in a valid and formatted way.
  - **Read Project Data (REQ-6.2):** The system must allow for the presentation of data in a readable and organized format, and the filtering of the same from the name, description, start date, and end date of at least one project.
  - **Update Project Data (REQ-6.3):**  The system must allow editing of the already created date of a given project in a valid and formatted way.
  - **Delete Project Data (REQ-6.4):** he system must allow for deleting one or more projects by filtering for name, description, start date, and end date.

- **Project Data Management (REQ-7)**
  - **Upload Usability Testing Data (REQ-7.1):** The system must provide the functionality to upload both the webcam video recorder and the screen video recorder for a usability test. Additionally, it should allow assigning a usability testing name, user type (A or B), user ID, and the location where the test was performed.
  - **Usability Testing Data Storage (REQ-7.2):** When uploading videos for a usability test, the system should store only the screen video recorder in the designated database. The facial emotions detected by a classification algorithm on the webcam video recorder must also be stored securely and anonymously.
  - **Read Usability Testing Data (REQ-7.3):** The system must present usability testing data in a readable and organized format. Users should be able to filter the data by project name, project description, user type, user ID, location, and whether the screen video data has been divided into tasks.
  - **Update Usability Testing Data (REQ-7.4):** The system must allow valid and properly formatted editing of existing usability testing data within a given project.
  - **Delete Usability Testing Data (REQ-7.5):** Users should be able to delete one or more usability testing data based on filtering criteria such as project name, project description, user type, user ID, location, and whether the screen video data has been divided into tasks.
  - **Split Usability Testing Data (REQ-7.6):** The system should enable the splitting of each usability testing screen video into task-based sub-videos. These sub-videos should have the same duration and be associated with corresponding names and actions for use in the CW.
  - **Update Usability Testing Data (Split) (REQ-7.7):**Users should have the ability to edit already split usability testing data, ensuring the data remains valid and properly formatted.
  - **Delete Usability Testing Data (Split) (REQ-7.8):** The system must allow the deletion of split usability testing data associated with a specific usability test, considering appropriate filtering options.
  - **Create Usability Smells (REQ-7.9):** The system must provide the functionality to create a list of usability smells, including their names and descriptions.
  - **Read Usability Smells (REQ-7.10):** Usability smells data should be presented in a readable and organized format. Users should be able to filter the data based on usability smell names and descriptions.
  - **Update Usability Smells (REQ-7.11):** Users should have the ability to edit usability smells, ensuring the changes are valid and properly formatted.
  - **Delete Usability Smells (REQ-7.12):** The system must allow the deletion of one or more usability smells, providing filtering options based on name and/or description.
    
- **Project Invitations (REQ-8)**
  - **Create Project Invitation (REQ-8.1):** The system should enable the creation of project invitations by selecting one or more projects for a specific team member via their email.
  - **Read Project Invitation (REQ-8.2):** The system must present project invitations in a readable and organized format, allowing filtering by project name, team member name, team member email, start date, end date, and creation date.
  - **Delete Project Invitation (REQ-8.3):** The system must provide the capability to delete one or more project invitations based on filtering criteria such as project name, team member name, team member email, start date, end date, and creation date.
  
- **Conclusions (REQ-9)**
  - **Permission to Consolidate Usability Testing Results (REQ-9.1):** The system should display the usability evaluation progress of all tasks from all usability tests conducted by team members in a readable and organized format. Additionally, it should include a button to grant permission for consolidating the results.
  - **Read Team Members' Usability Testing Results (REQ-9.2):** The system must present the progress of usability evaluation for tasks from all usability tests conducted by team members. This information should be displayed in a readable and organized format, allowing the selection of a usability test to view the usability evaluation of each team member.
  - **Read Usability Testing Results (REQ-9.3):** For each task-based usability test associated with a specific usability test, the system should be capable of displaying the cumulative frequency and distribution of facial emotions. Additionally, it should present the consolidated usability testing results for each usability testing method.
  - **Search Usability Testing Results (REQ-9.4):** The system should allow filtering of usability testing results by user type for each task-based usability testing associated with a specific usability test.
  - **Usability Testing Results from Data Export (REQ-9.5):** The system must provide the functionality to export usability testing results in data in a CSV file format for one or both user types.

  - **Read Team Members' Overall Usability Testing Results (REQ-9.6):** The system should allow the presentation of quantitative end results from the consolidated results. This includes displaying the distribution of each emotion's cumulative frequency across all tasks in all usability tests, the distribution of usability problems across all tasks in all usability tests, and the number of usability problems encountered with or without the help of facial emotions for each task-based usability testing associated with a specific usability test.

  - **Search Overall Usability Testing Results (REQ-9.7):** For each overall usability test, the system must allow filtering of results by user type.

  - **Overall Usability Testing Results Data Export (REQ-9.8):** The system should enable the export of overall usability testing results from data in a \ac{CSV} file format for one or both user types.

#### Team Member Functional Requirements

- **Project Invitations (REQ-10)**
  - **Read Project Invitation (REQ-10.1):** The system must allow the presentation of project invitations in a readable and organized format. Users should be able to filter invitations by project name, team leader name, team leader email, start date, and end date.
  - **Accept Project Invitation (REQ-10.2):** The system should allow team members to accept project invitations sent by team leaders, indicating their participation in the given project.

    
- **Usability Evaluation Projects (REQ-11)**
  - **Access to Usability Evaluation Methods for Each Project (REQ-11.1):** The system should display all projects and their corresponding usability evaluation methods directly in the navigation bar, providing easy access to these options.
  - **Read Usability Tests (REQ-11.2):** For each usability test associated with a specific project and usability evaluation method, the system must present the data in a readable and organized format. Additionally, it should display the progress of usability evaluation tasks for all usability tests and allow the user to select a usability test for evaluation, with or without the assistance of facial emotions.
  
- **Usability Evaluation with CW (REQ-11.3):**
  - **Read Tasks-Based Usability Testing (REQ-11.3.1):** For each task-based usability test within a pre-selected usability test, the system should display information and actions related to each task in a readable format. It should indicate whether the usability evaluation of the task has already been performed and provide a button to initiate the evaluation process.
  - **Evaluate Task-Based Usability Testing (REQ-11.3.2):**     The system should present the actions associated with pre-selected task-based usability testing in a readable format. It should include the four CW questions and respective fields for answering them. A field for writing notes and a checkbox to indicate whether the task has been evaluated should also be provided.
 
- **Usability Evaluation with Usability Smells (REQ-11.4):**
  - **Read Tasks-Based Usability Testing (REQ-11.4.1):**    For each task-based usability test within a pre-selected usability test, the system should display information about each task in a readable format. It should indicate whether the usability evaluation of the task has already been performed and provide a button to initiate the evaluation process.
  - **Evaluate Task-Based Usability Testing (REQ-11.4.2):**     The system should present a list of usability smells in a readable format, allowing users to select relevant ones. It should include a field for writing notes and a checkbox to indicate whether the task has been evaluated.
  - **Usability Testing Results from Consolidation (REQ-12)**

- **Usability Evaluation with CW (REQ-12.1):**
  - **Read Usability Tests (REQ-12.1.1):**     The system should present information about the usability tests conducted for a specific project. This includes details such as the project end date, usability test name, user type, user ID, location, permission status for consolidating results with other team members, and the option to choose whether to consolidate usability testing results with or without the assistance of facial emotions.
  - **Read Tasks-Based Usability Testing (REQ-12.1.2):**     For each task-based usability test within a pre-selected usability test, the system must display information about each task in a clear and readable format. It should indicate whether the usability evaluation for the task has been conducted and provide a button to initiate the usability evaluation of the task with all associated team members.
  - **Usability Testing Results Consolidation (REQ-12.1.3):**     The system should present the actions associated with the pre-selected tasks-based usability testing in a readable format. It should include the four CW questions and provide fields for answering them. A field for writing notes and a checkbox to indicate whether the task has already been evaluated should also be available.
- **Usability Evaluation with Usability Smells (REQ-12.2):**
  - **Read Usability Tests (REQ-12.2.1):** Similar to the CW approach, the system should display information about the usability tests conducted for a specific project. This includes details such as the project end date, usability test name, user type, user ID, location, permission status for consolidating results with other team members, and the option to choose whether to consolidate usability testing results with or without the assistance of facial emotions.
  - **Read Tasks-Based Usability Testing (REQ-12.2.2):** For all tasks-based usability testing of a given usability test pre-selected by the user, the system must display the information of each task in a readable format, whether the usability evaluation of the task has already taken place and a button to evaluate the usability of the task in order to start the evaluation together with all team members.
  - **Evaluate Task-Based Usability Testing (REQ-12.2.3):** The system must present in a readable format a list of usability smells with the option to select them, a field to write notes, and a checkbox to mention if the task has already been evaluated.

### Emotinality non-functional requirements

- **Performance:** The system must demonstrate efficient performance by ensuring fast loading times, with pages loading within a maximum of 3 seconds. 
- **Availability:** The system should maintain a high level of availability, ensuring uninterrupted access to users. Scheduled maintenance activities and system downtime should be carefully planned and minimized to minimize disruptions to user accessibility.
- **Security:** The system should be secure, with measures to protect user data and prevent unauthorized access or attacks, such as SSL encryption.
- **Usability:** The system should prioritize usability, providing a user-friendly experience for individuals with varying levels of technical proficiency. It should feature an intuitive and well-organized interface, ensuring ease of navigation and smooth user interaction.

## Emotionality database description

- **TeamLeader:** A model that extends the built-in Django User model to represent a project leader.
- **TeamMember:** A model that extends the built-in Django User model to represent a project member.
- **Project:** A model representing a project, led by a team leader and involving multiple team members. It encompasses attributes such as name, description, start and end dates, and a reference to the leading team leader.
- **UsabilitySmells:** A model representing usability smells identified for a specific project. It includes a reference to the corresponding project and a description.
- **HeuristicEvaluation:** A model representing the results of a heuristic evaluation conducted on the project. It includes a reference to the associated project and a description of the evaluation.
- **Video:** A template representing a video recording of a usability test. It includes a reference to the relevant project, usability test name, user type, UID, location, and multiple video files.
- **Invitations:** A template representing invitations sent to team members to join a project. It includes references to the project and team members involved, along with a boolean field indicating the acceptance status of the invitation.
- **ResultsConsolidation Permission:** A model representing the authorization granted for consolidating usability test results. It includes a reference to the corresponding video and a boolean field indicating whether authorization was given.
- **SubVideoTask:** A model representing a subtask performed by a team member during a usability test. It includes a reference to the associated video and detailed information about the subtask, such as task number, task name, performed actions, and a reference to the UsabilitySmells model.
- **SubVideoTaskEmotionsPlot:** A model representing the user's emotional state during the subtask. It includes a reference to the corresponding SubVideoTask and the plot data.
- **UsabilityEval_CW_Smells_Emotion:** A model representing the results of a usability evaluation of the subtask considering emotions. It includes a reference to the associated subtask, the team member who conducted the evaluation, and the evaluation results, including answers to questions and selected usability smells.
- **UsabilityEval_CW_Smells_without_Emotion:** A model representing the results of a usability evaluation of the subtask without considering emotions. It includes a reference to the corresponding subtask, the team member who conducted the evaluation, and the evaluation results, including answers to questions and selected usability smells.
- **ResultsConsolidation:** A model representing the consolidation of all results from CW and Usability Smells evaluations, both with and without emotions.


## Stakeholders common views**

**Navbar Before Team Leader Login**
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_navbar.png" alt="Navbar Before Team Leader Login" width="30%">
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_navbar_less.png" alt="Navbar After Team Leader Login" width="30%">

**Team Leader Signup**
<img src="Images/CONCLUSIONS_WEBSITE/TL/signup.png" alt="Team Leader Signup" width="30%">

**Team Leader Sign in**
<img src="Images/CONCLUSIONS_WEBSITE/TL/login.png" alt="Team Leader Sign in" width="30%">

**Team Leader Account Update**
<img src="Images/CONCLUSIONS_WEBSITE/TL/TL_account.png" alt="Team Leader Account Update" width="30%">

**Results consolidation**
<img src="Images/CONCLUSIONS_WEBSITE/TM/con_results_CW_actions.png" alt="Results consolidation with cognitive walkthrough." width="30%">
<img src="Images/CONCLUSIONS_WEBSITE/TM/con_results_Smells_actions.png" alt="Results consolidation with usability smells." width="30%">

## Team leader system functionalities

**Project Update on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/project_edit.png" alt="Project Update on the Final Website" width="30%">

**Project Creation on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/project_create.png" alt="Project Creation on the Final Website" width="30%">

**Project Management on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/projects.png" alt="Project Management on the Final Website" width="30%">

**Uploading the Usability Test on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_test_upload.png" alt="Uploading the Usability Test on the Final Website" width="30%">

**Usability Tests on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_tests.png" alt="Usability Tests on the Final Website" width="30%">

**Uploading Usability Test on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/update_video.png" alt="Uploading Usability Test on the Final Website" width="30%">

**Usability Test Split into Tasks on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/split_video_tasks.png" alt="Usability Test Split into Tasks on the Final Website" width="30%">

**Uploading Usability Test Task on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/edit_task.png" alt="Uploading Usability Test Task on the Final Website" width="30%">

**Delete Usability Test Task on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/tasks.png" alt="Delete Usability Test Task on the Final Website" width="30%">

**Usability Smells on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/usability_smells.png" alt="Usability Smells on the Final Website" width="30%">

**Create Usability Smell on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/create_usability_smell.png" alt="Create Usability Smell on the Final Website" width="30%">

**Edit Usability Smell on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/edit_usability_smell.png" alt="Edit Usability Smell on the Final Website" width="30%">

**Project Invitations on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/invitations.png" alt="Project Invitations on the Final Website" width="30%">

**Create Project Invitations on the Final Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/create_invitation.png" alt="Create Project Invitations on the Final Website" width="30%">

**Managing Permissions for Team Leaders to Consolidate Results**
<img src="Images/CONCLUSIONS_WEBSITE/TL/permissions_results_cons.png" alt="Managing Permissions for Team Leaders to Consolidate Results" width="30%">

**Viewing of Team Members' Work Progress by the Team Leader**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_cons_progress.png" alt="Viewing of Team Members' Work Progress by the Team Leader" width="30%">

**Usability Tests Results by Team Members**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_consolidation.png" alt="Usability Tests Results by Team Members" width="30%">

**Cumulative Frequency of Facial Emotions and the Distribution of Facial Emotions**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_ind.png" alt="Cumulative Frequency of Facial Emotions and the Distribution of Facial Emotions" width="30%">

**Export All Results in .CSV Format by Selecting the Type of User Usability Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_consolidados_download.png" alt="Export All Results in .CSV Format by Selecting the Type of User Usability Website" width="30%">

**Consolidated Usability Evaluations (Focus on the Usability Problems Found)**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_num_usab_prob.png" alt="Consolidated Usability Evaluations (Focus on the Usability Problems Found)" width="30%">

**Quantitative End-Results from the Consolidated Results**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_consolidados.png" alt="Quantitative End-Results from the Consolidated Results" width="30%">

**Export Overall Results in .CSV Format by Selecting the Type of User Usability Website**
<img src="Images/CONCLUSIONS_WEBSITE/TL/results_consolidados_download1.png" alt="Export Overall Results in .CSV Format by Selecting the Type of User Usability Website" width="30%">


## Team member system functionalities

**Navbar before the team member has logged in**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/TM_navbar.png" alt="Navbar before the team member has logged in" width="30%">

**Navbar after the team member has logged in**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/TM_navbar_less.png" alt="Navbar after the team member has logged in" width="30%">

**Team member project invitations**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/tm_invitations.png" alt="Team member project invitations" width="30%">

**Team member usability evaluation methods choice**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/usability_eval_methods.png" alt="Team member usability evaluation methods choice" width="15%">

**Progress of each task evaluated**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/usability_eval_progress.png" alt="Progress of each task evaluated" width="30%">

**Usability evaluation using CW**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/TM_CW_eval_task.png" alt="Usability evaluation using CW" width="30%">

**Usability evaluation using usability smells**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/con_results_Smells_eval.png" alt="Usability evaluation using usability smells" width="30%">

**Usability evaluation results using CW**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/con_results_CW_eval.png" alt="Usability evaluation results using CW" width="30%">

**Usability evaluation results using usability smells**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/con_results_Smells_eval.png" alt="Usability evaluation results using usability smells" width="30%">

**Consolidation of results using CW between team members**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/con_results_CW.png" alt="Consolidation of results using CW between team members" width="30%">

**Consolidation of results using usability smells between team members**
<img src="./Images/CONCLUSIONS_WEBSITE/TM/con_results_Smells.png" alt="Consolidation of results using usability smells between team members" width="30%">

**The Emotionality Tool performance scores**
<img src="./Images/CONCLUSIONS_WEBSITE/final_performance.png" alt="The Emotionality Tool performance scores" width="24%">







## Functional Requirements


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
