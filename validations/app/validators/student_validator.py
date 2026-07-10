# Single Responsibility Principle


class StudentValidator:

    ''' Cleaning the data fro "   Azeem  " to "azeem"
    This process is called normalization
    app/normalizers/student_normalizer.py
    '''

    @staticmethod
    def normalize(data):
        if not data:
            return {}

        normalized = data.copy()

        # Normalize name
        if "name" in normalized and isinstance(normalized["name"], str):
            normalized["name"] = " ".join(
                normalized["name"].strip().split()
            )

        # Normalize email
        if "email" in normalized and isinstance(normalized["email"], str):
            normalized["email"] = normalized["email"].strip().lower()

        # Normalize age
        if "age" in normalized:
            age = normalized["age"]

            if isinstance(age, str):
                age = age.strip()

                if age.isdigit():
                    normalized["age"] = int(age)

        return normalized

    '''DRY Principle
    A field can have multiple validation messages
    Append errors.
    {
        "name": [
            "Name is required.",
            "Minimum length is 3."
        ]
    }'''

    @staticmethod
    def add_error(errors, field, message):
        errors.setdefault(field, []).append(message)    

    @staticmethod   # It doesn't store any state. It only processes the provided input.
    def validate(data):

        errors = {}

        if not data:
            errors["request"] = [
                "Request body is required."
            ]
            return errors   # guard clause
        
        '''Single Responsibility Principle (Applied to Methods)
        Leading Underscore (_)? This is an internal implementation detail.

        validate() is the public API.
        _validate_name() is only used internally.
        '''

        StudentValidator._validate_name(data, errors)
        StudentValidator._validate_age(data, errors)
        StudentValidator._validate_email(data, errors)
        
        return errors
    


    @staticmethod
    def _validate_name(data, errors):
        # validate name
        name = data.get("name")
        if not name or not name.strip():
            StudentValidator.add_error(
                errors,
                "name",
                "name is required"
            )
        if name:
            if len(name) > 16:
                StudentValidator.add_error(
                    errors,
                    "name",
                    "name should have required length (<16 char)"
                )
    

    @staticmethod
    def _validate_age(data, errors):
        # validate age
        age = data.get("age")
        if age is None:
            StudentValidator.add_error(
                errors,
                "age",
                "age is required"
            )    
        elif not isinstance(age, int):
            StudentValidator.add_error(
                errors,
                "age",
                "age is a number"
            )   
        elif age < 0:
            StudentValidator.add_error(
                errors,
                "age",
                "age should be positive"
            )   
    

    @staticmethod  
    def _validate_email(data, errors):
        # validate email
        email = data.get("email")
        if not email or not email.strip():
            StudentValidator.add_error(
                errors,
                "email",
                "email is required"
            )   
        elif "@" not in email:
            StudentValidator.add_error(
                errors,
                "email",
                "email should contain @example.com"
            )



'''
What is the responsibility of a route? A route should:

- receive HTTP request
- call the appropriate logic
- return HTTP response

That's it. It shouldn't know every validation rule.
'''

'''
Start
   ↓
Create empty errors collection
   ↓
Check name
   ↓
Check age
   ↓
Check email
   ↓
Return all collected errors
'''