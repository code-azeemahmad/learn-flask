# Single Responsibility Principle


class StudentValidator:

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
            errors["name"] = [
                "Name is required."
            ]

        # validate age
        age = data.get("age")
        if age is None:
            errors["age"] = [
                "Age is required."
            ]       
        elif not isinstance(age, int):
            errors["age"] = [
                "Age must be an integer."
            ]
        elif age < 0:
            errors["age"] = [
                "Age cannot be negative."
            ]

        # validate email
        email = data.get("email")
        if not email or not email.strip():
            errors["email"] = [
                "Email is required."
            ]
        elif "@" not in email:
            errors["email"] = [
                "Invalid email address."
            ]

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