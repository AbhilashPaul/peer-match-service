# peer-match-service
This service offers a REST API endpoint that gnerates top 3 most suitable peer supporters for the adolescent based their condition, hobbies, and personal description.

## Running the application as a docker container (recommended)


1. **Install Docker Engine**:
   For instructions on how to install Docker Engine on your machine, see: https://docs.docker.com/engine/install/


2. **Build the image**:
    ```sh
    docker build -t peer-match-service .
    ```

3. **Create an '.env' file in the application root directory**

    ```
    ## gemini llm model version[Optional, if not specified 'gemini-2.0-flash' will be used]
    GOOGLE_LLM_MODEL=gemini-2.0-flash
    ## Gemini API key
    GOOGLE_API_KEY=
    APP_HOST=0.0.0.0
    ```
3. **Run the Application**:
    ```sh
    docker run -d --name peer-match-service-api -p 8080:8080 --env-file .env peer-match-service
    ```

## Running the application directly on your machine

1. **Ensure Pipenv is installed**
    
    If you don't have it on your machine, you can install it using:
    ```sh
        pip install pipenv
    ```


2. **Navigate to your project directory**

3. **Install dependencies**
    
    To install all the dependencies listed in the Pipfile, run:
    ```sh
        pipenv install --dev
    ```    

    This will create a virtual environment (if it doesn't already exist) and install the all therequired packages, including development dependencies (listed under [dev-packages] in the Pipfile).

4. **Sync with Pipfile.lock (optional)**
    If you want to ensure that the exact versions from the Pipfile.lock are installed, use:
    ```sh
        pipenv sync
    ```
    This is useful when you want to replicate an environment exactly as specified in the lock file

5. **Create an '.env' file in the application root directory**

    ```
        ## gemini llm model version[Optional, if not specified 'gemini-2.0-flash' will be used]
        GOOGLE_LLM_MODEL=gemini-2.0-flash
        ## Gemini API key
        GOOGLE_API_KEY=
    ```

6. **Run the application**
    ```sh
        python serve.py
    ```


## Invoking the api

Use a tool like Postman to invoke the model

```
Method: POST
```
```
url: http://127.0.0.1:8080/peer-match/invoke
```
```
request body example:
{
    "input": {
        "condition": "depression",
        "hobbies": "hiking,cycling",
        "about": "reserved but outdoorsy"
    }
}
```
```
response example:
{
    "output": {
        "matches": [
            {
                "peer_supporter_profile": {
                    "profile_id": 2,
                    "full_name": "Michael Rivera",
                    "age": 30,
                    "gender": "Male",
                    "selected_interests": [
                        "Sports",
                        "Fitness",
                        "Meditation"
                    ],
                    "mental_health_history": [
                        "Depression",
                        "Seasonal Affective Disorder (SAD)"
                    ],
                    "lived_experience_narrative": "During college, I faced severe depression that left me feeling isolated. Staying active through sports and practicing meditation helped me find balance. I want to help others discover the power of movement and mindfulness."
                },
                "reason_for_match": [
                    "Shares the same condition: Depression.",
                    "Interests align with the adolescent's hobbies: Both value physical activity (cycling/hiking vs. sports/fitness).",
                    "Michael's lived experience narrative highlights overcoming isolation through activity, which could resonate with a reserved adolescent."
                ]
            },
            {
                "peer_supporter_profile": {
                    "profile_id": 9,
                    "full_name": "Ethan Walker",
                    "age": 28,
                    "gender": "Male",
                    "selected_interests": [
                        "Fitness",
                        "Cooking",
                        "Traveling"
                    ],
                    "mental_health_history": [
                        "Depression",
                        "Substance Use Disorder (in recovery)"
                    ],
                    "lived_experience_narrative": "Recovering from depression and substance use was a transformative journey for me. Fitness and cooking became my outlets, and I want to inspire others to find their own paths to recovery."
                },
                "reason_for_match": [
                    "Shares the same condition: Depression.",
                    "Ethan's interest in fitness aligns with the adolescent's hobbies of hiking and cycling.",
                    "Ethan's narrative focuses on finding outlets for recovery, which could be beneficial for the adolescent."
                ]
            },
            {
                "peer_supporter_profile": {
                    "profile_id": 13,
                    "full_name": "Noah Kim",
                    "age": 23,
                    "gender": "Male",
                    "selected_interests": [
                        "Running",
                        "Reading",
                        "Volunteering"
                    ],
                    "mental_health_history": [
                        "Obsessive Compulsive Disorder (OCD)",
                        "Depression"
                    ],
                    "lived_experience_narrative": "Dealing with OCD and depression was overwhelming at times, but running and volunteering gave me purpose. I hope to inspire others to find strength in their passions."
                },
                "reason_for_match": [
                    "Shares the same condition: Depression.",
                    "Noah's interest in running is similar to the adolescent's interest in hiking and cycling, indicating a shared appreciation for physical activity.",
                    "Noah's narrative emphasizes finding purpose through passions, which could be helpful for an adolescent struggling with depression."
                ]
            }
        ]
    },
    "metadata": {
        "run_id": "d1b9ecea-c230-475b-9ec8-d50b5ce1f958",
        "feedback_tokens": []
    }
}
```