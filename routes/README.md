# Body Models request

```bash
{
 "username": "jnunz",
 "birth_date": "2009-10-10", 
 "email": "jason2@example.com",
 "phone": "6001-0099",
 "password_hash": "admin"
}

```
## Usuario es menor de 18 años
```bash
{
    "error": "You must be at least 18 years old"
}
```
## Usuario registrado correctamente
```bash
{
    "message": "Registered successfully"
}
```