# Single Responsibility Principle


class StudentValidator:

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
        
        # validate name
        name = data.get("name")
        if not name or not name.strip():
            StudentValidator.add_error(
                errors,
                "name",
                "name is required"
            )
        if len(name) > 16:
            StudentValidator.add_error(
                errors,
                "name",
                "name should have required length (<16 char)"
            )

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

        return errors


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