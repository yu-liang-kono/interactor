# interactor
Interactor provides a common interface for performing complex user interactions. It's inspired by [collectiveidea's interactor gem](https://github.com/collectiveidea/interactor).

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

### Usage

```python
from somewhere import AuthenticateUser

ctx = AuthenticateUser.call(email='test@gmail.com', password='secret')
print ctx.user
print ctx.token
```
