import streamlit as st
import openai
import uuid
import random


# In-memory storage
if 'patient_data' not in st.session_state:
    st.session_state.patient_data = {}

# Memory test words
memory_words = ["whale", "soccer", "purple", "thirteen", "apple", "chair", "sunset", "guitar"]

def process_health_data(data):
    user_input = f"""
This GPT specializes in making health-related diagnostics and creating appropriate rehabilitation plans based on user input about their health conditions, symptoms, and medical history. It provides personalized recommendations for exercises, therapy, and lifestyle adjustments to aid recovery and improve overall well-being. The GPT considers user preferences, existing medical conditions, and progress to tailor the rehabilitation plans effectively. It will avoid making definitive medical diagnoses and always recommend checking Braining's developments (https://www.brainingai.com/) for more information on serious concerns. BrainingDoc interacts in a friendly and quirky manner, ensuring a conversational and approachable tone. It provides technical and medical-grade diagnostics, offering insights and advice that go beyond common internet searches. When given answers to a questionnaire, BrainingDoc uses them to formulate the most appropriate diagnostic and cohesive treatment plan, referring to the games available at Braining's VR repository. It is also multilingual, providing responses in various languages as needed.

    BrainingDoc is an advanced AI assistant tasked with creating and managing a comprehensive health assessment bot. This bot conducts thorough analyses based on user responses to a wide-ranging questionnaire. BrainingDoc's primary goal is to design, implement, and continuously improve this bot to provide valuable insights into an individual's overall health status, including physical, cognitive, and mental well-being.

    Key Responsibilities:

    2. Data Collection and Analysis:
    - Securely collect and store user responses.
    - Analyze responses to identify potential health risks or areas of concern.
    - Generate a comprehensive health profile for each user.

    3. Risk Assessment:
    - Develop algorithms to assess various health risks based on user responses.
    - Consider factors such as age, gender, medical history, lifestyle choices, and cognitive/physical abilities.
    - Flag high-risk responses for further investigation or referring to Braining's developments.

    4. Personalized Recommendations:
    - Based on the analysis, provide a concise rehabilitation plan for improving health and well-being, including daily routines and VR games from Braining. Format the plan with clear sections: Daily Routine and VR Games to Try from Braining.
    - Refer all physical, cognitive, and linguistic exercises to Braining's VR games and encourage users to try them.
    - Suggest lifestyle changes, exercise routines, or dietary adjustments as appropriate.
    - Recommend further consultation with Braining when necessary.

    5. Cognitive and Physical Ability Evaluation:
    - Assess physical abilities through self-reported confidence in performing specific tasks.
    - Consider known physical disabilities when evaluating responses.

    6. Sensory Assessment:
    - Analyze responses to identify potential sensory issues.

    7. Mental Health Screening:
    - Flag responses indicating potential mental health concerns for further follow-up with Braining.

    8. Medication and Treatment Tracking:
    - Collect information on current medications and treatments.
    - Analyze potential interactions or side effects based on reported symptoms.

    9. Longitudinal Analysis:
    - Design the system to allow for repeated assessments over time.
    - Implement functionality to track changes in health status and identify trends.

    11. Data Privacy and Security:
    - Implement robust security measures to protect user data.
    - Ensure compliance with relevant health data protection regulations (e.g., HIPAA).

    12. Reporting and Visualization:
    - Generate clear, easy-to-understand reports summarizing the assessment results.
    - Use data visualization techniques to present information in an engaging manner.

    13. Integration with Healthcare Systems:
    - Develop APIs to allow integration with electronic health records (EHRs) and other healthcare systems.
    - Enable secure sharing of assessment results with Braining, with user consent.

    14. Continuous Improvement:
    - Regularly review and update the questionnaire based on user feedback and new medical research.
    - Implement machine learning algorithms to improve risk assessment and recommendations over time.

    15. Multilingual Support:
    - Develop the capability to offer the questionnaire in multiple languages to reach a diverse user base.

    BrainingDoc's task is to create a sophisticated, empathetic, and highly accurate health assessment bot that can provide valuable insights and encourage users to take proactive steps towards better health. The bot is capable of handling a wide range of health scenarios and provides appropriate guidance while clearly communicating its limitations and the importance of referring to Braining for more information. The output should be a concise, personalized rehabilitation plan without additional conclusions, following a structured format with clear sections: Daily Routine and VR Games to Try from Braining. The plan should be mentioned as a guideline for up to a month after the assessment. The first response should always be: 'Thank you for sharing your health details. Braining's AI is working on developing the most appropriate plan for you. Here we go:' The plan should always end with: 'Remember to consult with Braining's experts before starting any new exercise or therapy program. Your progress will be continuously monitored, and adjustments to your rehabilitation plan will be made as needed by our novel AI model.'

    Patient Information:
    {data}

    Instructions:
    1. Analyze the patient's data and provide a comprehensive health assessment.
    2. Provide insights on potential health implications based on the provided information.
    3. Suggest tailored recommendations for improving health and well-being based on the analysis.
    4. Pay special attention to the cognitive assessment, physical assessment, and sensory assessment sections.
    5. If the patient is taking medications, analyze potential interactions or side effects.
    6. If the patient has any physical disabilities, consider these in your assessment and recommendations.
    7. Evaluate the patient's lifestyle choices (sleep, diet, exercise, alcohol consumption, smoking) and their potential impact on health.

    Format the assessment output as follows:
    '''
    Health Assessment Report for {data.get('name', 'Patient')}
    ## Patient Information
    [Summary of patient data]
    ## Medical History Analysis
    [Analysis of medical conditions and medications]
    ## Lifestyle Analysis
    [Evaluation of sleep, diet, exercise, alcohol, and smoking habits]
    ## Cognitive Assessment
    [Analysis of cognitive responses]
    ## Physical Assessment
    [Evaluation of physical abilities and sensations]
    ## Sensory Assessment
    [Analysis of sensory capabilities]
    ## Health Insights
    [Comprehensive analysis based on all provided information]
    ## Recommendations
    [Tailored health recommendations]
    '''
    Provide a detailed plan based on the given information.
    """
    client = openai.OpenAI(api_key = "sk-svcacct-LhP5BHBX0wWVh25exxnzT3BlbkFJxSaggACt39jx60CP8Ge2")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2,
            top_p=0.95
        )
        #response_content = response['choices'][0]['message']['content'].strip()
        response_content = response.choices[0].message.content.strip()
    except Exception as e:
        response_content = f"An error occurred: {str(e)}"

    return response_content

def main():
    st.image("https://static.wixstatic.com/media/217ee8_c97a3512166d43e9ad039620e8fbb7db~mv2.png/v1/crop/x_0,y_106,w_666,h_169/fill/w_426,h_108,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Prancheta_1-removebg-preview--LOGOPRETO.png")
    st.header("Check your health with BrainingDoc, Powered by BrainingAI.")

    # Memory test
    if 'memory_words' not in st.session_state:
        st.session_state.memory_words = random.sample(memory_words, 4)
    
    st.write("Please memorize these words for later recall:")
    st.write(", ".join(st.session_state.memory_words))

    # Create form
    with st.form("health_form"):
        name = st.text_input("What is your name?")
        age = st.number_input("What is your age?", min_value=0, max_value=120)
        gender = st.selectbox("What is your gender?", ["Male", "Female", "Other", "Prefer not to say"])

        st.subheader("Medical History")
        medical_conditions = st.multiselect(
            "Do you have or did you suffer from any of the following medical conditions?",
            ["Hypertension", "Diabetes", "Heart Disease", "Stroke", "None of the above"]
        )
        
        mental_health = st.radio(
            "Have you ever been diagnosed with a mental health disorder? (e.g., depression, anxiety)",
            ["Yes", "No"]
        )
        
        brain_meds = st.radio(
            "Are you currently taking any medications for brain health or mental health issues?",
            ["Yes", "No"]
        )
        
        if brain_meds == "Yes":
            med_conditions = st.multiselect(
                "Select all conditions for which you are taking medication.",
                ["Hypertension", "Diabetes", "Heart Disease", "Stroke", "Depression", "Anxiety", "Others"]
            )
            if "Others" in med_conditions:
                other_meds = st.text_input("Please specify other medications (comma separated)")

        st.subheader("Lifestyle")
        sleep = st.select_slider(
            "How many hours of sleep do you typically get per night?",
            options=["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"]
        )
        
        diet = st.selectbox(
            "How would you describe your diet?",
            ["Balanced", "High in sugar/fats", "Vegetarian/Vegan", "Other"]
        )
        
        exercise = st.select_slider(
            "How often do you exercise?",
            options=["Rarely/Never", "Once a week", "Several times a week", "Daily"]
        )
        
        alcohol = st.select_slider(
            "How often do you consume alcohol?",
            options=["Never", "Occasionally", "Frequently", "Daily"]
        )
        
        smoking = st.selectbox(
            "How often do you smoke?",
            ["Never", "Occasionally", "Frequently", "Daily", "Former smoker"]
        )
        if smoking == "Former smoker":
            quit_time = st.text_input("How long ago did you quit smoking?")

        st.subheader("Cognitive Assessment")
        breakfast = st.text_input("Can you recall what you had for breakfast yesterday?")
        recalled_words = st.text_input("Can you recall the 4 words we asked you to memorise in the beginning of the survey?")
        time_question = st.text_input("If you had to be somewhere at 3 PM and it takes 45 minutes to get there, what time should you leave?")

        st.subheader("Physical Assessment")
        physical_disabilities = st.multiselect(
            "Please note any known physical disabilities",
            ["Paraplegia", "Joint issues", "Amputation", "None", "Other"]
        )
        if "Other" in physical_disabilities:
            other_disabilities = st.text_input("Please specify other physical disabilities")

        stairs_ability = st.select_slider(
            "How would you describe your ability to climb a flight of stairs?",
            options=[
                "I cannot climb stairs by myself at all.",
                "I do some of the work, but my helper needs to cover most of it.",
                "I need assistance to cover roughly half of the effort.",
                "I need minimal assistance, but I do roughly all the work.",
                "I can do it, but with someone supervising me in case I fail.",
                "I can do it with the aid of a cane/walker or holding on to the bannister.",
                "I can do it independently."
            ]
        )

        bed_ability = st.select_slider(
            "How would you describe your ability to get out of bed?",
            options=[
                "I cannot get out of bed by myself at all.",
                "I do some of the work, but my helper needs to cover most of it.",
                "I need assistance to cover roughly half of the effort.",
                "I need minimal assistance, but I do roughly all the work.",
                "I can do it, but with someone supervising me in case I fail.",
                "I can do it by supporting myself on the bed.",
                "I can do it independently."
            ]
        )

        arm_pinch = st.radio(
            "Pinch both your arms, one at a time. Which one applies:",
            [
                "I feel both pinches are the same.",
                "I feel it more on the left arm.",
                "I feel it more on the right arm.",
                "Neither apply."
            ]
        )

        st.subheader("Sensory Assessment")
        smell_ability = st.radio(
            "Can you easily identify common smells (e.g., coffee)?",
            ["Yes", "No", "Sometimes"]
        )

        submitted = st.form_submit_button("Submit")

        if submitted:
            data = {
                "name": name,
                "age": age,
                "gender": gender,
                "medical_conditions": medical_conditions,
                "mental_health": mental_health,
                "brain_meds": brain_meds,
                "med_conditions": med_conditions if brain_meds == "Yes" else None,
                "other_meds": other_meds if brain_meds == "Yes" and "Others" in med_conditions else None,
                "sleep": sleep,
                "diet": diet,
                "exercise": exercise,
                "alcohol": alcohol,
                "smoking": smoking,
                "quit_time": quit_time if smoking == "Former smoker" else None,
                "breakfast": breakfast,
                "recalled_words": recalled_words,
                "time_question": time_question,
                "physical_disabilities": physical_disabilities,
                "other_disabilities": other_disabilities if "Other" in physical_disabilities else None,
                "stairs_ability": stairs_ability,
                "bed_ability": bed_ability,
                "arm_pinch": arm_pinch,
                "smell_ability": smell_ability
            }

            # Generate a unique ID for the patient data
            patient_id = str(uuid.uuid4())

            # Store data in session state
            st.session_state.patient_data[patient_id] = data

            # Process the health assessment
            assessment_result = process_health_data(data)

            st.success("Data submitted successfully!")
            st.subheader("Health Assessment Result")
            st.markdown(assessment_result)

    # Display stored patient data
    if st.session_state.patient_data:
        st.subheader("Stored Patient Data")
        for id, patient in st.session_state.patient_data.items():
            st.write(f"Patient ID: {id}")
            st.write(patient)
            st.write("---")

if __name__ == '__main__':
    main()
