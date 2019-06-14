package main

const swagger = `openapi: 3.0.0
info:
  version: 1.0.0
  title: 'Signed, Sealed, Delivered, I''m Yours!'
servers:
  -
    name: local
    url: 'http://localhost:8080'
paths:
  /flag:
    get:
      summary: 'Get the flag'
      operationId: getFlag
      security:
        -
          bearerAuth: []
      responses:
        '200':
          description: 'Got the flag'
          content:
            application/json:
              schema:
                properties:
                  flag:
                    type: string
                    example: 'BSidesPDXCTF{IV3_G0T_SW4G}'
                required:
                  - flag
        '401':
          $ref: '#/components/responses/unauthorized'
        '403':
          $ref: '#/components/responses/forbidden'
  /authenticate:
    post:
      summary: 'Get a JWT'
      operationId: authenticate
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                username:
                  type: string
                  example: frank
                password:
                  type: string
                  example: password
              required:
                - username
                - password
      responses:
        '200':
          description: 'Successfully authenticated'
          content:
            application/json:
              schema:
                properties:
                  jwt:
                    type: string
                    example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmcmFuayIsImJzaWRlc19pc19hZG1pbiI6ZmFsc2V9.b1MxSKajtSwFSJ29_zeT_Zg9DkXDUau25bmboMcK25E
                required:
                  - jwt
        '401':
          $ref: '#/components/responses/unauthorized'
        '403':
          $ref: '#/components/responses/forbidden'
        '422':
          $ref: '#/components/responses/unprocessableEntity'
        '500':
          $ref: '#/components/responses/internalServerError'
  /users:
    post:
      summary: 'Create a new user'
      operationId: register
      requestBody:
        required: true
        content:
          application/json:
            schema:
              properties:
                username:
                  type: string
                  example: frank
                password:
                  type: string
                  example: password
              required:
                - username
                - password
      responses:
        '201':
          description: 'Created user'
          headers:
            Location:
              schema:
                type: string
                example: /users/frank
        '401':
          $ref: '#/components/responses/unauthorized'
        '403':
          $ref: '#/components/responses/forbidden'
        '409':
          $ref: '#/components/responses/conflict'
        '422':
          $ref: '#/components/responses/unprocessableEntity'
        '500':
          $ref: '#/components/responses/internalServerError'
  '/users/{username}':
    get:
      summary: 'Get a user'
      operationId: getUser
      parameters:
        -
          in: path
          name: username
          required: true
          schema:
            type: string
            example: frank
      responses:
        '501':
          $ref: '#/components/responses/notImplemented'
components:
  responses:
    unauthorized:
      description: Unauthorized
      content:
        text/plain:
          schema:
            type: string
            example: Unauthorized
    unprocessableEntity:
      description: 'Unprocessable Entity'
      content:
        text/plain:
          schema:
            type: string
            example: 'Unprocessable Entity'
    forbidden:
      description: Forbidden
      content:
        text/plain:
          schema:
            type: string
            example: Forbidden
    internalServerError:
      description: 'Internal Server Error'
      content:
        text/plain:
          schema:
            type: string
            example: 'Internal Server Error'
    notImplemented:
      description: 'Not Implemented'
      content:
        text/plain:
          schema:
            type: string
            example: 'Not Implemented'
    conflict:
      description: Conflict
      content:
        text/plain:
          schema:
            type: string
            example: Conflict
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
`
