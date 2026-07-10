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