# Real Estate Rental SaaS Platform

As the lead developer, 
I architected and built the full-stack web application for a multi-platform SaaS real estate rental service.
This involved designing scalable database models for properties, users, and bookings, 
and implementing the entire backend and frontend using Django.

The platform features a complex booking calendar to manage availability, a robust user authentication system, and a dynamic property search.
The website is powered by a single, coherent Django codebase, 
utilizing its built-in ORM and templating engine to deliver a secure and responsive user experience.

## Key Features
- Complex booking calendar with availability management
- Property search and filtering system  
- User authentication and authorization
- Responsive design using Django templates

## Tech Stack
- **Backend:** Django, Django ORM
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite/PostgreSQL

## Project Structure
This project was part of a larger ecosystem that also included a mobile application powered by a Django REST Framework API.

## Key URLs
- `/login/` - User authentication and login
- `/signup/` - Create new user accounts
- `/gallery/` - Browse all real estate properties
- `/resProfile/<slug:slug>/` - Detailed view of specific real estate property

## Related Projects
- **[REVE Mobile Application Backend](https://github.com/Amr-Namora/REVE--application)** - The Django REST Framework API that powers the mobile app component of this real estate service
