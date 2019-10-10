package main

const openapi = `openapi: "3.0.0"
info:
  version: 1.0.0
  title: Yours Truly
  license:
    name: MIT
paths:
  /pets:
    get:
      summary: List all pets
      operationId: listPets
      tags:
        - pets
      parameters:
        - name: limit
          in: query
          description: How many items to return at one time (max 100)
          required: false
          schema:
            type: integer
            format: int32
      responses:
        "200":
          description: A paged array of pets
          headers:
            x-next:
              description: A link to the next page of responses
              schema:
                type: string
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pets"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
    post:
      summary: Create a pet
      operationId: createPets
      tags:
        - pets
      responses:
        "201":
          description: Null response
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
  /characters:
    get:
      summary: List all characters
      operationId: listCharacters
      tags:
        - characters
      # parameters:
      #   - in: header
      #     name: X-Debug
      #     schema:
      #       type: string
      #     required: false
      responses:
        "200":
          description: A list of characters
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Characters"
  /pets/{petId}:
    get:
      summary: Info for a specific pet
      operationId: showPetById
      tags:
        - pets
      parameters:
        - name: petId
          in: path
          required: true
          description: The id of the pet to retrieve
          schema:
            type: string
      responses:
        "200":
          description: Expected response to a valid request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
components:
  schemas:
    Character:
      type: object
      required:
        - firstName
        - lastName
        - aliases
        - photoURL
        - photo
      properties:
        firstName:
          type: string
          example: Dade
        lastName:
          type: string
          example: Murphy
        aliases:
          type: array
          items:
            type: string
        photoURL:
          type: string
        photo:
          type: string
          example: 20897.jpg
    Characters:
      type: array
      items:
        $ref: "#/components/schemas/Character"
    Pet:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        tag:
          type: string
    Pets:
      type: array
      items:
        $ref: "#/components/schemas/Pet"
    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string`
