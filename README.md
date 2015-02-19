# interactor
Interactor provides a common interface for performing complex user interactions. It's inspired by ![https://github.com/collectiveidea/interactor](collectiveidea's interactor gem).

### An Example Interactor

```python
from interactor import Interactor

class AuthenticateUser(Interacotr):

    def run(self):

        user = User.authenticate(self.context.email, self.context.password)
        if user:
            self.context.user = user
            self.context.token = user.secret_token
        else:
            raise RuntimeError('Fail to authenticate user')
```
