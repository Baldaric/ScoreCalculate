import pandas as pd
import streamlit as st


def run():
    def FinalScorePhase1(GradedChallenge4=0, GradedChallenge5=0, GradedChallenge6=0, LiveCode4=0, Presentation1=0, Milestones2=0):
        CalcGC4 = GradedChallenge4 * 0.1
        CalcGC5 = GradedChallenge5 * 0.1
        CalcGC6 = GradedChallenge6 * 0.1
        CalcLC = LiveCode4 * 0.2
        CalcPr = Presentation1 * 0.15
        CalcMl = Milestones2 * 0.35

        FinalScore = CalcGC4 + CalcGC5 + CalcGC6 + CalcLC + CalcPr + CalcMl

        Data = {
            'Assessment': ['Graded Challenge 4', 'Graded Challenge 5', 'Graded Challenge 6', 'Live Code', 'Presentation', 'Milestone'],
            'Total Score': [GradedChallenge4, GradedChallenge5, GradedChallenge6, LiveCode4, Presentation1, Milestones2],
            'Weight (%)': [10, 10, 10, 20, 15, 35],
            'Score': [CalcGC4, CalcGC5, CalcGC6, CalcLC, CalcPr, CalcMl]
        }
        
        df2 = pd.DataFrame(Data)
        df2['Total Score'] = df2['Total Score'].round(3)
        df2['Score'] = df2['Score'].round(3)
        
        return df2, round(FinalScore, 3)

    # Streamlit app
    st.write("## Phase 1 Calculator")
    st.image('booo.png')
    st.write("Enter your scores for each assessment:")

    # User inputs for scores
    GradedChallenge4 = st.number_input("Graded Challenge 4", min_value=0.0, max_value=100.0, value=0.0)
    GradedChallenge5 = st.number_input("Graded Challenge 5", min_value=0.0, max_value=100.0, value=0.0)
    GradedChallenge6 = st.number_input("Graded Challenge 6", min_value=0.0, max_value=100.0, value=0.0)
    LiveCode4 = st.number_input("Live Code 4", min_value=0.0, max_value=100.0, value=0.0)
    Presentation1 = st.number_input("Presentation 1", min_value=0.0, max_value=100.0, value=0.0)
    Milestones2 = st.number_input("Milestone 2", min_value=0.0, max_value=100.0, value=0.0)

    # Calculate the final score and display the DataFrame
    df2, final_score = FinalScorePhase1(GradedChallenge4, GradedChallenge5, GradedChallenge6, LiveCode4, Presentation1, Milestones2)
    
    # Split layout into two columns
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Detailed Score Breakdown:")
        st.dataframe(df2, hide_index=True)
        calculate = st.button("Calculate")  # Button placed below the DataFrame

    # Display the results in the second column if the button is pressed
    if calculate:
        with col2:
            st.write('#### **Your Final Score Calculation is:**')
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50; 
                    border-radius: 10px; 
                    padding: 10px; 
                    background-color: #f9f9f9; 
                    text-align: center; 
                    font-size: 20px; 
                    font-weight: bold; 
                    color: #4CAF50;">
                    {final_score:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("*Note: This calculation is based solely on the scores provided. Other factors may influence the final outcome.*")

            # Feedback based on the final score
            if final_score < 70:
                st.write("### It's not a reason to give up")
                st.image('1.jpg')
            elif 70 <= final_score < 80:
                st.write("### Now we're talking")
                st.image('2.jpg')
            elif 80 <= final_score < 95:
                st.write("### How is it possible?")
                st.image('3.jpg')
            elif final_score >= 95: 
                st.write("### A Freakin' Genius!!!")
                st.image('4.jpg')

if __name__ == "__main__":
    run()
