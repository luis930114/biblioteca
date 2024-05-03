
# Project Title

A brief description of what this project does and who it's for


## API Reference

#### Get all items

```http
  GET /api/books
    OBTIENE TODOS LOS LIBROS CREADOS 
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  POST /api/books
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | **Required**. titulo del libro |
| `author`  | `string` | **Required**. author del libro  |
| `isbn`   | `string` | **Required**. codigo del libro |
| `genre`   | `string` | **Required**. genero del libro |




## Authors

- [@luis930114](https://github.com/luis930114)
